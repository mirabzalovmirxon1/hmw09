from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=150)
    price = models.IntegerField()
    published_year = models.IntegerField()
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="books"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
