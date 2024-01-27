from django.db import models

class Client(models.Model):

    STATUS_CHOICES = [
        ('active', 'Активен'),
        ('booking', 'Бронь'),
        ('sold', 'Куплено'),
        ('barter', 'Бартер'),
        ('installment', 'Рассрочка'),
        ('canceled', 'Отмена'),
    ]

    name = models.CharField(max_length=50, verbose_name = "ФИО")
    number = models.CharField(max_length=50,verbose_name = "Номер телефона")
    deal = models.CharField(max_length=255,verbose_name = "Договор")
    status = models.CharField(max_length=50, choices=STATUS_CHOICES,verbose_name = 'Статус')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Клиент"  
        verbose_name_plural = "Клиенты"

class City(models.Model):
    name = models.CharField(max_length=50,unique= True, verbose_name = "Город")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"


class Apartment(models.Model):

    STATUS_CHOICES = [
        ('Активен', 'Активен'),
        ('Бронь', 'Бронь'),
        ('Куплено', 'Куплено'),
        ('Бартер', 'Бартер'),
        ('Рассрочка', 'Рассрочка'),
        ('Отмена', 'Отмена'),
    ]

    num_apartment = models.IntegerField(verbose_name = "№ квартиры")
    location = models.ForeignKey(City, on_delete=models.CASCADE,verbose_name = "Обьект")
    floor = models.IntegerField(verbose_name = "Этаж")
    square = models.DecimalField(max_digits=10, decimal_places=2,verbose_name = "КВ")
    date = models.DateField(verbose_name = "Дата")
    price = models.IntegerField(verbose_name = "Цена")
    clients = models.ForeignKey(Client,on_delete=models.CASCADE,verbose_name = "Клиент")
    status = models.CharField(max_length=50, choices=STATUS_CHOICES,verbose_name = "Cтатус")

    
    def __str__(self):
        return f"Apartment {self.num_apartment}: {self.status}"
    
    
    class Meta:
        verbose_name = "Квартира"
        verbose_name_plural = "Квартиры"
