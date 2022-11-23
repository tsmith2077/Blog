from django.db import models
from django.contrib.auth.models import User


class BlogPost(models.Model):
    """A class for creating blog posts."""
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        """Return a string representation of the title and text."""
        return (f"{self.title}:\n{self.text}")