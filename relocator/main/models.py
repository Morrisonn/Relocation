from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    role = models.CharField(verbose_name="Роль (Сотрудник-0, Hr-1)", max_length=50, blank=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "Пользователи"
        verbose_name_plural = "Пользователи"
        ordering = ["-role", "username"]


class News(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=200)
    content = models.TextField(verbose_name="Текст")
    created_at = models.DateTimeField(verbose_name="Дата создания", default=timezone.now)
    image = models.ImageField(verbose_name="Изображение", upload_to="news_images", default='default_image.jpg')
    # user = models.ForeignKey("User", on_delete=models.CASCADE)

    def __str__(self):
        # return self.title
        return f"{self.title} {self.content} {self. created_at} {self.image}"

    
    class Meta:
        verbose_name = "Новости"
        verbose_name_plural = "Новости"


class Personal_Info(models.Model):
    first_name = models.CharField(max_length=50, blank=False, null=True)
    last_name = models.CharField(max_length=50, blank=False, null=True)
    middle_name = models.CharField(max_length=50, blank=False, null=True)
    photo = models.ImageField(upload_to="photos/", blank=True, null=True)
    gender = models.CharField(
        max_length=10,
        choices=[("male", "Мужской"), ("female", "Женский")],
        blank=False,
        null=True,
    )
    rate = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=True)
    date_of_birth = models.DateField(blank=False, null=True)
    work_experience = models.PositiveIntegerField(blank=False, null=True)
    position = models.CharField(max_length=50, blank=False, null=True)
    email = models.EmailField(blank=False, null=True)
    phone_number = models.CharField(max_length=20, blank=False, null=True)
    user = models.ForeignKey(
        "User", related_name="personal_info", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.middle_name} {self.work_experience} {self.position} {self.email} {self.phone_number} {self.user}"


class Location(models.Model):
    country = models.CharField(max_length=100, verbose_name="Страна")
    city = models.CharField(max_length=100, verbose_name="Город")
    description = models.TextField(verbose_name="Описание")
    latitude = models.FloatField(verbose_name="Широта", null=True)
    longitude = models.FloatField(verbose_name="Долгота", null=True)

    def __str__(self):
        return self.country

    class Meta:
        verbose_name = "Локации"
        verbose_name_plural = "Локации"


class Application(models.Model):
    status = models.CharField(max_length=20)
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    location = models.ForeignKey("Location", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.status} {self.user} {self.location}"


class Documents(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to="documents/")
    application = models.ForeignKey("Application", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} {self.file} "


class Check_list(models.Model):
    name = models.CharField(max_length=50)
    status = models.BooleanField()
    application = models.ForeignKey("Application", on_delete=models.CASCADE)

    def __str__(self):
        return f"Interview ({self.id}, {self.name}, {self.status})"


class Interview(models.Model):
    notes = models.TextField()
    link = models.URLField()
    application = models.ForeignKey("Application", on_delete=models.CASCADE)
    datetime = models.DateTimeField(null=True)

    def __str__(self):
        return f"Interview ({self.id}, {self.notes})"


class Review(models.Model):
    RATING_CHOICES = (
        ('1', '★'),  
        ('2', '★ ★'),   
        ('3', '★ ★ ★'),  
        ('4', '★ ★ ★ ★'),  
        ('5', '★ ★ ★ ★ ★'),  
    )

    review = models.TextField()
    rating = models.CharField(max_length=5, choices=RATING_CHOICES)
    created_at = models.DateTimeField(default=timezone.now)
    application = models.ForeignKey("Application", on_delete=models.CASCADE)

    def __str__(self):
        return f"Review (id: {self.id}, rating: {self.rating}, {self.review}, {self.created_at})"
