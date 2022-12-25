from apps.api.services import get_path_upload_avatar, validate_size_image
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.db import models


class AuthUser(AbstractUser):
    """
    Модель кастомного пользователя
    """
    email = models.EmailField(max_length=150, unique=True)
    first_name = models.CharField(
        max_length=150,
        verbose_name='Имя'
    )

    last_name = models.CharField(
        max_length=150,
        verbose_name='Фамилия'
    )
    join_date = models.DateTimeField(auto_now=True)
    country = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    bio = models.TextField(max_length=2000, blank=True, null=True)
    display_name = models.CharField(max_length=30, blank=True, null=True)
    avatar = models.ImageField(
        upload_to=get_path_upload_avatar,
        blank=True,
        null=True,
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg']),
            validate_size_image
        ]
    )

    class Meta:
        ordering = ['-date_joined']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        constraints = [
            models.CheckConstraint(
                check=~models.Q(username='me'),
                name='not_me'
            )
        ]

    @property
    def is_authenticated(self):
        """
        Проверка аутентификации
        """
        return True

    def __str__(self):
        return self.username


class Follower(models.Model):
    """
    Модель подписчиков
    """
    user = models.ForeignKey(
        AuthUser,
        on_delete=models.CASCADE,
        related_name='owner'
    )
    subscriber = models.ForeignKey(
        AuthUser,
        on_delete=models.CASCADE,
        related_name='subscribers'
    )

    def __str__(self):
        return f'{self.subscriber} подписан на {self.user}'


class SocialLinks(models.Model):
    """
    Модель ссылок на соц сети пользователя
    """
    user = models.ForeignKey(
        AuthUser,
        on_delete=models.CASCADE,
        related_name='social_links'
    )
    link = models.URLField(max_length=100)

    def __str__(self):
        return f'{self.user}'
