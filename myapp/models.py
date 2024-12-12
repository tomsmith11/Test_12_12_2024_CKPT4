from django.db import models

# Create your models here.

"""
The models we have, student and teacher, should be a many to many relationship.
This means that a student can have many teachers and a teacher can have many students.
"""

"""
Define Student model
"""
class Student(models.Model):
  name = models.CharField(max_length=100)
  teachers = models.ManyToManyField('Teacher', related_name='students')

  def __str__(self):
        return f"Student: {self.name}"

"""
Define Teacher model
"""
class Teacher(models.Model):
  name = models.CharField(max_length=100)
  
  def __str__(self):
        return f"Teacher: {self.name}"
