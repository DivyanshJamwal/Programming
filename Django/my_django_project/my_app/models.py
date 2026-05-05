from django.db import models

class NewsArticle(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=50)
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title