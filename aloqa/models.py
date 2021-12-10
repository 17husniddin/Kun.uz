from django.db import models





class Aloqa(models.Model):
    name = models.CharField(max_length=100)
    Email = models.EmailField()
    subject = models.CharField(max_length=300)
    massage = models.TextField(default=0)

    class Meta():
        ordering = ['name']

    def str(self):
        return self.name