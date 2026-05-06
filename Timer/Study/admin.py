from django.contrib import admin
from .models import Subject, StudyRecord

# Register your models here.
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject_name')
    search_fields = ('subject_name',)


@admin.register(StudyRecord)
class StudyRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'subject', 'hours', 'date_studied', 'created_at')
    list_filter = ('subject', 'date_studied')
    search_fields = ('user',)