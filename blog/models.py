from django.db import models

class BlogMessage(models.Model):
    title = models.CharField(max_length = 100)
    date = models.DateField()
    blog_message = models.TextField()

    def __str__(self):
        return self.title
