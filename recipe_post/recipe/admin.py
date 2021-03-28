from django.contrib import admin

from .models import Recipe  # 追加

# Register your models here.
admin.site.register(Recipe)  # 追加
