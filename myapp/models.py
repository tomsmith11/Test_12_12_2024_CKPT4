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
  age = models.IntegerField(null=True)
  teacher = models.ForeignKey(
      "Teacher",  # This is a foreign key that links the student to the teacher model
      on_delete=models.SET_NULL,  # This is the action to take when the teacher is deleted
      null=True,  # This allows the teacher to be null, which is useful for when the relationship is optional
      related_name="Teacher"  # This is the name of the relationship from the teacher model to the student model
  )

  def __str__(self):
        return f"Student: {self.name}"

"""
Define Teacher model
"""
class Teacher(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField(max_length=100, null=True, unique=True)
  subject = models.CharField(max_length=100, null=True)
  
  def __str__(self):
        return f"Teacher: {self.name}"

