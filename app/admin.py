from django.contrib import admin
from .models import (
    Student, Teacher, Subject, Score, AssessmentScore,
    AcademicCalendar, Term
)

# ---------- Inlines ----------

class ScoreInline(admin.TabularInline):
    model = Score
    extra = 0

class AssessmentScoreInline(admin.TabularInline):
    model = AssessmentScore
    extra = 0


# ---------- Student Admin ----------

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'student_id', 'grade', 'parent_name', 'parent_email', 'parent_phone')
    search_fields = ('name', 'student_id', 'parent_name')
    list_filter = ('grade',)
    inlines = [ScoreInline]


# ---------- Teacher Admin ----------

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject')
    search_fields = ('name', 'email')
    list_filter = ('subject',)


# ---------- Subject Admin ----------

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


# ---------- Score Admin ----------

@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'assessment_type', 'score', 'date', 'term')
    search_fields = ('student__name', 'subject__name')
    list_filter = ('assessment_type', 'term', 'subject', 'date')


# ---------- AssessmentScore Admin ----------

@admin.register(AssessmentScore)
class AssessmentScoreAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'assessment_type', 'score')
    search_fields = ('student__name', 'subject__name')
    list_filter = ('assessment_type',)


# ---------- Academic Calendar Admin ----------

@admin.register(AcademicCalendar)
class AcademicCalendarAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    search_fields = ('title',)
    list_filter = ('date',)



@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date')
    search_fields = ('name',)
    list_filter = ('start_date', 'end_date')
