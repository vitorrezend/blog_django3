from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    sub_title = models.CharField(max_length=30)
    content = models.TextField()

    def __str__(self):
        return self.title

    def full_name(self):
        return self.title + self.sub_title
    
    full_name.admin_order_field = 'title'
