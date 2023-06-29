from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название блюда')
    picture = models.ImageField(null=True, blank=True)
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'Меню'
        verbose_name = 'Меню'

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=50, verbose_name='Размер')

    class Meta:
        verbose_name_plural = 'Размеры'
        verbose_name = 'Размер'

    def __str__(self):
        return self.name


class Price(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='prices', verbose_name='Блюдо')
    size = models.ForeignKey(Size, on_delete=models.CASCADE, verbose_name='Размер')
    price = models.IntegerField(verbose_name='Цена')

    class Meta:
        verbose_name_plural = 'Цены'
        verbose_name = 'Цена'

    def __str__(self):
        return f"{self.menu.name} - {self.size.name}: {self.price} руб."


class Reservation(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    date = models.DateField(verbose_name='Дата')
    phone = models.CharField(max_length=11, verbose_name='Телефон клиента')

    class Meta:
        verbose_name_plural = 'Бронирование'
        verbose_name = 'Бронирование'

    def __str__(self):
        return self.name

class PizzaRestaurant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=200)
    image = models.ImageField(upload_to='restaurant_images', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'ПиццаРестораны'
        verbose_name = 'ПиццаРесторан'

    def __str__(self):
        return self.name