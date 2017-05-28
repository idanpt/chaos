from django.db import models

# Create your models here.


class Mode(models.Model):
    mode = models.CharField(max_length=200)
    is_active = models.BooleanField()

    def __str__(self):
        return self.mode


class ResponseCode(models.Model):
    code = models.IntegerField(default=200)

    def __str__(self):
        return str(self.code)