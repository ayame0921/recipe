from django.urls import path
from comment.views import comment_create

app_name = "comment"

urlpatterns = [
    path('create', comment_create, name="create"),
]