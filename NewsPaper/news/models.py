from django.db import models


class Article(models.Model):
    title = models.CharField(
        max_length=50
    )
    text = models.TextField()
    date = models.DateField(
        auto_now_add=True
    )

    def __str__(self):
        return f'{self.title.title()}: {self.text[:30]}'


class Author(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
    )
    articles = models.ForeignKey(
        to='Article',
        on_delete=models.CASCADE,
        related_name='article'
    )

    def __str__(self):
        return f'{self.name.title()}'
