from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    role = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.role
    
    class Meta:
        verbose_name='Пользователи'
        verbose_name_plural='Пользователи'
        ordering = ['-role', 'username']



class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title    


class Personal_Info(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    work_experience = models.PositiveIntegerField()
    position = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name} - {self.position}'


class Location(models.Model):
    country = models.CharField(max_length=100, verbose_name="Страна")
    city = models.CharField(max_length=100, verbose_name="Город")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
            return self.country
    
    class Meta:
        verbose_name='Локации'
        verbose_name_plural='Локации'


class Application(models.Model):
    status = models.CharField(max_length=20)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    location = models.ForeignKey('Location', on_delete=models.CASCADE, null=True)

    def __str__(self):
            return self.status


class Documents(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='documents/')
    application = models.ForeignKey('Application', on_delete=models.CASCADE)

    def __str__(self):
        return self.title   


class Check_list(models.Model):
    name = models.CharField(max_length=50)
    status = models.BooleanField()
    application = models.ForeignKey('Application', on_delete=models.CASCADE)

    def __str__(self):
        return self.name  


class Interview(models.Model):
    notes = models.TextField()
    link = models.URLField()
    application = models.ForeignKey('Application', on_delete=models.CASCADE)

    def __str__(self):
        return f"Interview ({self.id})"


class Review(models.Model):
    review = models.TextField()
    rating = models.IntegerField()
    application = models.ForeignKey('Application', on_delete=models.CASCADE)

    def __str__(self):
        return f"Review (id: {self.id}, rating: {self.rating})"    

       