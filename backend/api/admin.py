from django.contrib import admin

from .models import Exam, Question, Subject

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('title', 'year')
    filter_horizontal = ('subjects',)

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
	list_display = ('text', 'get_subject_name', 'correct_option')
	def get_subject_name(self, obj):
		return obj.subject.name
	get_subject_name.short_description = 'Subject Name'
