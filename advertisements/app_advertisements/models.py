from django.db import models


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