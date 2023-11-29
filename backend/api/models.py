from django.db import models

# Create your models here.

class Exam(models.Model):
	
    title = models.CharField(max_length=255, choices = [
        ('JAMB', 'JAMB (Joint Admissions and Matriculations Board)'),
        ('WAEC', 'WAEC (West African Examinations Council)'),
    ])
    year = models.PositiveIntegerField()
    subjects = models.ManyToManyField('Subject')

    def __str__(self):
        return f'{self.title} {self.year}'

class Subject(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Question(models.Model):

    text = models.TextField()
    optionsA = models.CharField(max_length=255, blank=True, null=True)
    optionsB = models.CharField(max_length=255,blank=True, null=True)
    optionsC = models.CharField(max_length=255, blank=True, null=True)
    optionsD = models.CharField(max_length=255, blank=True, null=True)
    optionsE = models.CharField(max_length=255, blank=True, null=True)

    correct_option = models.CharField(max_length=255,blank=True, null=True, choices=[
    	(0, 'A'),
        (1, 'B'),
        (2, 'C'),
        (3, 'D'),
        (4, 'E'),
    	])
    correct_answer = models.TextField(blank=True, null=True)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def get_options(self):
    	return [self.optionsA, self.optionsB, self.optionsC, self.optionsD, self.optionsE]

    def get_subject(self):
    	return self.subject.name

    def get_exam(self):
    	return [self.exam.title, self.exam.year]