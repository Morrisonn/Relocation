from django.db import models

class Personal_Info(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    work_experience = models.PositiveIntegerField()
    position = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name} - {self.position}'