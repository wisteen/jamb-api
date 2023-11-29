from rest_framework import serializers

from .models import Question

class QuestionSerializer(serializers.ModelSerializer):
	my_options = serializers.SerializerMethodField(read_only=True)
	my_subject = serializers.SerializerMethodField(read_only=True)
	my_exam = serializers.SerializerMethodField(read_only=True)
	class Meta:
		model = Question
		fields = [
			'text',
			'my_options',
			'correct_option',
			'correct_answer',
			'correct_answer',
			'my_subject',
			'my_exam',

		]
	def get_my_options(self, obj):
		return obj.get_options()
	def get_my_subject(self, obj):
		return obj.get_subject()
	def get_my_exam(self, obj):
		return obj.get_exam()