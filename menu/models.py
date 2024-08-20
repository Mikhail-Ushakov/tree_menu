from django.db import models


class Menu(models.Model):
    """
    Модель хранит названия меню
    """
    name = models.CharField(max_length=255, verbose_name='Название меню')

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    """
    Модель хранит элементы меню, с указателем на конкретное меню
    """
    name = models.CharField(max_length=255, verbose_name='Текст ссылки')
    menu = models.ForeignKey(Menu, blank=True, null=True, 
                             related_name='items',
                             on_delete=models.CASCADE)
    parent = models.ForeignKey('self', null=True, blank=True, 
                               related_name='children',
                               on_delete=models.CASCADE)
    url = models.CharField(max_length=255, verbose_name='Ссылка')

    def __str__(self):
        return self.name