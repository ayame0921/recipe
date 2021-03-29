from django.urls import path
from recipe.views import (
    RecipeCreateView, RecipeDeleteView, RecipeUpdateView,
    RecipeListView, RecipeDetailView
)
app_name = "recipe"

urlpatterns = [
    path('', RecipeListView.as_view(), name="index"),
    path('<int:pk>', RecipeDetailView.as_view(), name="detail"),
]
