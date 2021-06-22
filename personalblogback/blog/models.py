from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=55)
    content = models.TextField(max_length=2000)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['date', ]
