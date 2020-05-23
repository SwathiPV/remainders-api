from django.db import models

# Create your models here.
class Remainder(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    mobile = models.CharField(max_length=10)

    def __str__(self):
        return self.title
    