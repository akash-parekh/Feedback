from django.db import models

# Create your models here.

class Review(models.Model):
    user_name = models.CharField(max_length=200)
    review_text = models.TextField()
    rating = models.IntegerField()
    
    def __str__(self):
        return f"{self.id} {self.user_name}"