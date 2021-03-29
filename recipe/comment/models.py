from django.db import models
from recipe.models import Recipe 


class Comment(models.Model):
    content = models.TextField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, default=None, null=True)