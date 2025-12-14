from django.contrib.auth.models import User
from django.db import models
from PIL import Image
from django.db.models import CASCADE


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)


# from django.db import models
#
#
# class Compensation(models.Model):
#     name = models.CharField(max_length=255)
#
#
# class Department(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField()
#
#
# class Employee(models.Model):
#     first_name = models.CharField(max_length=20)
#     last_name = models.CharField(max_length=20)
#     age = models.PositiveIntegerField(default=18)
#     job_title = models.CharField(max_length=20)
#     speciality = models.CharField(max_length=100)
#     from_date = models.DateField()
#     department = models.ForeignKey(Department, on_delete=models.CASCADE)
#     compensations = models.ManyToManyField(Compensation)
#

# class Contact(models.Model):
#     phone = models.CharField(max_length=20)
#     email = models.EmailField()
#     address = models.CharField(max_length=255)
#     employee = models.OneToOneField(Employee,on_delete=models.CASCADE)
