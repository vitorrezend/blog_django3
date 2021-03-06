from django.db import models

class Categorias(models.TextChoices):
    RPG = 'RP', 'Role Playing Game'
    CR = 'CR', 'Curiosidades'
    GR = 'GR', 'Geral'
    

class Post(models.Model):
    title = models.CharField(max_length=30)
    sub_title = models.CharField(max_length=30)
    content = models.TextField()
    categories = models.CharField(
        max_length=2,
        choices=Categorias.choices,
        default=Categorias.GR,
    )
    deleted = models.BooleanField(default=True)


    def __str__(self):
        return self.title

    def full_name(self):
        return self.title + self.sub_title
    
    def get_category_label(self):
        return self.get_categories_display()
    
    full_name.admin_order_field = 'title'
