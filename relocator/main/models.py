from django.db import models

class User(models.Model):
    login = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)
    role = models.IntegerField()
    
    def __str__(self):
        return self.login


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


class Application(models.Model):
    status = models.CharField(max_length=20)
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
            return self.status


class Location(models.Model):
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    description = models.TextField()
    application = models.ForeignKey('Application', on_delete=models.CASCADE)

    def __str__(self):
            return self.country


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

       