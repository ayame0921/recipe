from django.urls import path

from staffroom.views import (
    RecipeCreateView, RecipeDeleteView, RecipeUpdateView
)

app_name = "recipe"

urlpatterns = [
    path('create', RecipeCreateView.as_view(), name="create"),
    path('<int:pk>/update', RecipeUpdateView.as_view(), name="update"),
    path('<int:pk>/delete', RecipeDeleteView.as_view(), name="delete"),
]
