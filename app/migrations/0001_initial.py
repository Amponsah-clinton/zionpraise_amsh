# Generated by Django 5.1.7 on 2025-04-03 04:56

import app.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicCalendar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assessment_choice', models.CharField(choices=[('class_test', 'Class Test'), ('monthly_exam', 'Monthly Exam'), ('midterm_exam', 'Midterm Exam'), ('appraisal_exam', 'Appraisal Exam'), ('end_of_term_exam', 'End of Term Exam')], max_length=20)),
                ('student_id', models.CharField(default=app.models.generate_student_id, max_length=10, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('grade', models.CharField(choices=[('7a', '7A'), ('7b', '7B'), ('7c', '7C'), ('8a', '8A'), ('8b', '8B'), ('9', '9')], max_length=3)),
                ('parent_name', models.CharField(max_length=100)),
                ('parent_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('parent_phone', models.CharField(max_length=15, unique=True)),
                ('password', models.CharField(default=app.models.generate_password, max_length=10)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assessment_type', models.CharField(choices=[('class_test', 'Class Test'), ('monthly_exam', 'Monthly Exam'), ('midterm_exam', 'Midterm Exam'), ('appraisal_exam', 'Appraisal Exam'), ('end_of_term_exam', 'End of Term Exam')], max_length=20)),
                ('score', models.PositiveIntegerField()),
                ('date', models.DateField(auto_now_add=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scores', to='app.student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scores', to='app.subject')),
            ],
        ),
        migrations.CreateModel(
            name='AssessmentScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assessment_type', models.CharField(choices=[('class_test', 'Class Test'), ('monthly_exam', 'Monthly Exam'), ('midterm_exam', 'Midterm Exam'), ('appraisal_exam', 'Appraisal Exam'), ('end_of_term_exam', 'End of Term Exam')], default='class_test', max_length=100)),
                ('score', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assessment_scores', to='app.score')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assessmentscore', to='app.student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject_scores', to='app.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('subject', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to='app.subject')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
