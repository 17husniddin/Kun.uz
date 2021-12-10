from django.db import models

class News(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField()
    date = models.DateField(auto_now_add=True)
    category = models.ForeignKey('Category', related_name="news", on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class Category(models.Model):
        name = models.CharField(max_length=300)

        def __str__(self):
              return self.name