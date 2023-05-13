from django.db import models
import uuid

# Create your models here.
class Token(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    token_number = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return str(self.token_number)
