from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='home'),
    path('add-student/', views.add_student, name='add_student'),
    path('parent-login/', views.parent_login, name='parent_login'),
    path('teacher-register/', views.teacher_register, name='teacher_register'),
    path('teacher-dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('teacher-login/', views.teacher_login, name='teacher_login'),
    path("export-scores/", views.export_scores_csv, name="export_scores_csv"),
    path("students/", views.student_list, name="student_list"),
    path("students/export-csv/", views.export_students_csv, name="export_students_csv"),
    path("analysis/", views.analysis_view, name="analysis"),
    path("export-analysis-csv/", views.export_analysis_csv, name="export_analysis_csv"),
    path("analysis/", views.analysis_view, name="analysis_view"),
    path('assessment-details/', views.assessment_details_view, name="assessment_details"),
    path('student/<int:student_id>/', views.student_detail, name='student_detail'),
    path('add-event/',  views.add_event, name='add_event'),        
    path('teachers/', views.teacher_list, name='teacher_list'),  # List of teachers
    path('edit/<int:pk>/', views.teacher_edit, name='teacher_edit'),  # Edit teacher
    path('delete/<int:pk>/', views.teacher_delete, name='teacher_delete'),  # Delete teacher
    path('logout/', views.logout_view, name='logout'),
    path('teacher-logout/', views.teacher_logout, name='teacher_logout'),
    path('performance/', views.performance_view, name='performance'),
    path('upload-students/', views.upload_students, name='upload_students'),
    path("export_scores/", views.export_student_scores, name="export_student_scores"),
    path("upload_scores/", views.upload_student_scores, name="upload_student_scores"),
    path('student/<int:student_id>/download/', views.download_student_scores, name='download_student_scores'),











]




