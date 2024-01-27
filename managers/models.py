from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from .usermanager import CustomUserManager

class Manager(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=40,unique=True, verbose_name = "ФИО",)
    number = models.CharField(max_length=13, verbose_name = "Номер телефона")
    email = models.EmailField(unique = True,verbose_name="Почта")
    created_at = models.DateField(auto_now_add = True,verbose_name="Дата создание")
    amount_of_trade = models.IntegerField(verbose_name ="Количество сделок",null= True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = CustomUserManager()

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = "Менеджеры"
        verbose_name_plural = verbose_name

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
