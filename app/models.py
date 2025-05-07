from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.db.models import Sum, Avg, Max
import random
import string

# ---------- Constants ----------

ASSESSMENT_CHOICES = [
    ('class_test', 'Class Test'),
    ('monthly_exam', 'Monthly Exam'),
    ('midterm_exam', 'Midterm Exam'),
    ('appraisal_exam', 'Appraisal Exam'),
    ('end_of_term_exam', 'End of Term Exam'),
]

GRADE_CHOICES = [
    ('7a', '7A'), ('7b', '7B'), ('7c', '7C'),
    ('8a', '8A'), ('8b', '8B'),
    ('9', '9')
]

# ---------- Utility Functions ----------

def generate_student_id():
    return f'ZPEC{random.randint(100, 999)}'

def generate_password():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=10))


from django.db import models
from datetime import date

class Term(models.Model):
    TERM_CHOICES = [
        ('term1', 'Term 1'),
        ('term2', 'Term 2'),
        ('term3', 'Term 3'),
    ]

    name = models.CharField(max_length=10, choices=TERM_CHOICES, unique=True)
    start_date = models.DateField()
    end_date = models.DateField()

    def includes(self, date):
        return self.start_date <= date <= self.end_date

    def is_end_of_term(self):
        """
        Returns True if the current date is the last day of the term.
        """
        today = date.today()
        return today == self.end_date

    def __str__(self):
        return self.get_name_display()

    def promote_students_at_end(self):
        """
        Promotes students at the end of the term (if the term ends).
        This can be triggered manually or automatically.
        """
        if self.is_end_of_term():
            # Get all students who are in the current term and promote them
            students = Student.objects.filter(scores__term=self)
            for student in students:
                student.promote()



# ---------- Subject Model ----------

class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


from django.contrib.auth.models import User
from django.db import models

class Student(models.Model):
    assessment_choice = models.CharField(max_length=20, choices=ASSESSMENT_CHOICES)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="student_profile", null=True, blank=True)
    student_id = models.CharField(max_length=10, default=generate_student_id, unique=True)
    name = models.CharField(max_length=255)
    grade = models.CharField(max_length=3, choices=GRADE_CHOICES)
    parent_name = models.CharField(max_length=100, blank=True, null=True)  # Made optional
    parent_email = models.EmailField(blank=True, null=True)  # Made optional
    parent_phone = models.CharField(max_length=15, blank=True, null=True)  # Made optional
    password = models.CharField(max_length=10, default=generate_password)

    def delete(self, *args, **kwargs):
        # Delete associated User before deleting Student
        self.user.delete()
        super(Student, self).delete(*args, **kwargs)
    
    def promote(self):
        """
        Promote the student based on their current grade.
        """
        if self.grade.startswith('7'):
            self.grade = '8a'  # Or logic to move from 7a -> 8a
        elif self.grade.startswith('8'):
            self.grade = '9'
        elif self.grade == '9':
            self.grade = 'graduated'
        self.save()

    def save(self, *args, **kwargs):
        if not self.user:
            username = self.parent_email if self.parent_email else self.parent_phone
            
            # Attempt to get the user by username (either parent email or phone)
            parent_user, created = User.objects.get_or_create(
                username=username,
                defaults={'email': self.parent_email}
            )
            
            # If it's a new user, set their password
            if created:
                parent_user.set_password(self.password)
                parent_user.save()

            self.user = parent_user

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.student_id})"



# ---------- Score Model ----------
from django.utils.timezone import now
class Score(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='scores')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='scores')
    assessment_type = models.CharField(max_length=20, choices=ASSESSMENT_CHOICES)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    term = models.ForeignKey('Term', on_delete=models.SET_NULL, null=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.term:
            today = self.date or now().date()  # Use the score date or today's date
            term = Term.objects.filter(start_date__lte=today, end_date__gte=today).first()
            if term:
                self.term = term
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student.name} - {self.subject.name} - {self.assessment_type} ({self.term}): {self.score}"



from django.db import models
from django.contrib.auth.models import User
from .models import Subject  # Make sure you have a Subject model

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="teacher_profile")
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    subject = models.OneToOneField(Subject, on_delete=models.CASCADE, related_name="teacher")

    def save(self, *args, **kwargs):
        if not self.user_id:
            teacher_user, created = User.objects.get_or_create(
                username=self.email,
                defaults={
                    'email': self.email,
                    'password': self.password  # Save plain text
                }
            )
            self.user = teacher_user

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.subject.name}"



class AssessmentScore(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="assessmentscore")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="subject_scores")
    assessment_type = models.CharField(max_length=100, choices=ASSESSMENT_CHOICES, default='class_test')
    score = models.ForeignKey(Score, on_delete=models.CASCADE, related_name="assessment_scores")

    def __str__(self):
        return f"{self.student.name} - {self.subject.name} ({self.assessment_type}): {self.score}"



class AcademicCalendar(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    description = models.TextField(blank=True, null=True)


    def __str__(self):
        return f"{self.title} - {self.date}"
