from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Recipe(models.Model):
    title = models.CharField(verbose_name="タイトル", max_length=200)
    content = models.TextField(verbose_name="内容")
    description = models.TextField(blank=True, default="")
    image = models.ImageField(upload_to="images/uploaded/", default=None, null=True, blank=True)
    detail_main = ImageSpecField(
        source="image",
        processors=[ResizeToFill(640, 480)],
        format="jpg",
        options={"quality": 80}
    )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "レシピ"
        verbose_name_plural = "レシピ"

    def __str__(self):
        return self.title


# Create your models here.
