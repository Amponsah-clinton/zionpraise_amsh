from django import forms
from django.contrib.auth.models import User
from .models import Student

class ParentRegistrationForm(forms.ModelForm):
    """Form for parent registration (creating a user account)."""
    username = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


from django import forms
from .models import Student

class StudentRegistrationForm(forms.ModelForm):
    """Form for registering students while auto-creating the parent account."""

    class Meta:
        model = Student
        fields = ['name', 'grade', 'parent_name', 'parent_email', 'parent_phone']

    def clean(self):
        """Ensure at least one contact method (email or phone) is provided."""
        cleaned_data = super().clean()
        email = cleaned_data.get("parent_email")
        phone = cleaned_data.get("parent_phone")

        if not email and not phone:
            raise forms.ValidationError("At least one of Parent Email or Phone is required.")

        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Adding Bootstrap classes to the form fields
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'  # Apply Bootstrap form-control class

            # If the field is required, add a class to highlight that
            if field.required:
                field.widget.attrs['class'] += ' is-required'




from django import forms
from .models import Student
from django.db.models import Q

class ParentLoginForm(forms.Form):
    username = forms.CharField(label="Parent Email or Phone")
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        # Search students using parent's email or phone
        students = Student.objects.filter(Q(parent_email=username) | Q(parent_phone=username))
        
        if not students.exists():
            raise forms.ValidationError("No student found with this parent contact.")
        
        # Check if the password matches for all the students
        for student in students:
            if student.password == password:
                self.cleaned_data["students"] = students  # Store all found students
                return self.cleaned_data
        raise forms.ValidationError("Incorrect password for the provided parent contact.")




from django import forms
class StudentCSVUploadForm(forms.Form):
    csv_file = forms.FileField(label='Upload CSV file')




from django import forms
from .models import Teacher, Score

class TeacherRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=False
    )

    class Meta:
        model = Teacher
        fields = ['name', 'email', 'password', 'subject']

    def __init__(self, *args, hide_password=False, **kwargs):
        super().__init__(*args, **kwargs)
        
        if hide_password:
            self.fields.pop('password')

        for field_name, field in self.fields.items():
            if not isinstance(field.widget, forms.PasswordInput):
                field.widget.attrs.update({'class': 'form-control'})



class ScoreForm(forms.ModelForm):
    """Form for entering student scores (Restricted to teacher's subject)."""
    class Meta:
        model = Score
        fields = ['student', 'assessment_type', 'score']



from django import forms

class TeacherLoginForm(forms.Form):
    email = forms.EmailField(max_length=255, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(max_length=10, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


from django import forms
from .models import AcademicCalendar

class AcademicCalendarForm(forms.ModelForm):
    class Meta:
        model = AcademicCalendar
        fields = ['title', 'description', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].required = False  # <- make field optional in form



















