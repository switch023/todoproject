from django.db import models

# Create your models here.
PRIORITY = (('danger','Q1(重要かつ緊急)'),('warning','Q2(重要)'),('info','Q3(緊急)'))
class TodoModel(models.Model):
  title = models.CharField(max_length = 100)
  content = models.TextField()
  priority = models.CharField(
    max_length = 50,
    choices = PRIORITY
  )
  duedate = models.DateField()
  def __str__(self):
    return self.title