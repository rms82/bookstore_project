from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

USER = get_user_model()

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    created_by = models.ForeignKey(USER, on_delete=models.CASCADE, related_name='books')
    text = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    cover = models.ImageField(upload_to='covers/', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', args=[self.pk])


class Comment(models.Model):
    user = models.ForeignKey(USER, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()

    datetime_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
