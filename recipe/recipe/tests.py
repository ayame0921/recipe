from django.test import TestCase
from django.urls import reverse_lazy
from recipe.models import Recipe


class TestRecipe(TestCase):

    fixtures = ["recipe.json", "user.json", ]

    def setUp(self):
        self.recipe_list = Recipe.objects.all()

    def test_top_page(self):
        res = self.client.get("/")
        self.assertEqual(res.status_code, 200)

    def test_recipe_top(self):
        res = self.client.get("/recipe/")
        self.assertEqual(res.status_code, 200)

    def test_recipe_detail(self):
        for recipe in self.recipe_list:
            res = self.client.get(reverse_lazy("recipe:detail", kwargs={"pk": recipe.id}))
            self.assertEqual(res.status_code, 200)