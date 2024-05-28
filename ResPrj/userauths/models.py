
from email.headerregistry import Group
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100)
    bio = models.CharField(max_length=100)
    
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    # groups = models.ManyToManyField(Group, verbose_name=_('groups'), blank=True, related_name='user_groups')
    # user_permissions = models.ManyToManyField(
    #     Permission,
    #     verbose_name=_('user permissions'),
    #     blank=True,
    #     related_name='user_permissions',
    #     help_text=_('Specific permissions for this user.'),
    # )

    # class Meta:
    #     swappable = 'AUTH_USER_MODEL'


    def __str__(self):
        return self.username