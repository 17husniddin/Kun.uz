from django.db import models

class Homepage(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField()
    date = models.DateField(auto_now_add=True)
    class Meta:
        verbose_name = 'Home'
        verbose_name_plural = 'HomePage'
        ordering = ['name']
    def __str__(self):
        return self.price
# Create your models here.
