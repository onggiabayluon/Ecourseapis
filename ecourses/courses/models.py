from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomBaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True
        

class User(AbstractUser):
    avatar = models.ImageField(upload_to='users/%Y/%m')


class Category(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)

    def __str__(self):
        return self.name


class Course(CustomBaseModel):
    class Meta:
        # cùng 1 category thì subject không được trùng tên
        unique_together = ('subject', 'category')
        ordering = ["-id"]

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    subject = models.CharField(max_length=255, null=False)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='courses/%Y/%m', default=None)

    def __str__(self):
        return self.subject
