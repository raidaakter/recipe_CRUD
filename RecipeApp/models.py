from django.db import models

# Create your models here.

class recipeModel(models.Model):
    Title = models.CharField(max_length=100)
    Description = models.TextField(max_length=100)
    Ingredients = models.TextField(max_length=150)
    Instructions = models.TextField(max_length=100)
    Image = models.ImageField(upload_to='media/recipe')
    
    
    def __str__(self):
        return self.Title
    