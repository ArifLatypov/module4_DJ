from django.db import models
from django.contrib import admin
from django.utils.html import format_html

class Advertisement(models.Model):
    
    # строковое поле для небольших размеров
    # 'заголовок' - verbose_name - название поля извне
    title = models.CharField('заголовок', max_length=128)

    # Описание товара/информация о товаре
    # большое текстовое поле, для больших размеров
    description = models.TextField('описание')
    
    
    # Цена
    # специальный тип данных с фиксированной точкой
    price = models.DecimalField('цена', max_digits=10, decimal_places=2)
    
    # Актуальность обьявления
    # логический тип, два значения - правда/ложь
    auction = models.BooleanField('торг', help_text='Отметьте, уместен ли торг')
    
    # Дата публикакции
    # поле записывается при создании объявления.
    created_at = models.DateTimeField(auto_now_add=True)

    # Дата изменения/обновления
    # поле записывается при каждом обновлении
    updated_at = models.DateTimeField(auto_now=True)

    @admin.display(description='Дата создания')
    def created_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():
            created_date = self.created_at.strftime("%H:%M:%S")
            return format_html(
                '<span style="color:green">Сегодня в {} </span>', 
                created_date
                )
        
        return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")

    @admin.display(description='Дата изменения')
    def updated_date(self):
        from django.utils import timezone
        if self.updated_at.date() == timezone.now().date():
            updated_at = self.updated_at.strftime("%H:%M:%S")
            return format_html(
                '<span style="color:red">Сегодня в {} </span>', 
                updated_at
                )
        
        return self.updated_at.strftime("%d.%m.%Y в %H:%M:%S")
    
    def __str__(self):
        return f"Advertisement: Advertisement(id={self.id}, title={self.title}, price={self.price})"

    class Meta:
        db_table = 'advertisements' 
    # Имя продавца + контакты

    # Количество товара

    # Уместен ли торг

    # Возможен ли обмен 

    # Адрес продажи/осмотре

    # Б/У или 