from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# Task model imported from the same directory

class Task(models.Model):

    # use models module and inherit Model class to create own database model class.
    title = models.CharField(max_length=200)

    # foreign key relationship with User model.
    # on_delete=models.CASCADE will delete the task if the associated User is deleted.

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True )
    


    def __str__(self):
        return self.title
    # __str__ method is used to return a string representation of the object.


