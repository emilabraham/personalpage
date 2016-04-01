from django.test import TestCase
from django.utils import timezone
from recipe.models import Recipe
from django.core.urlresolvers import reverse

#Factory method to create recipes
def create_recipe(title, slug, body):
  """ 
  Creates a recipe with the given info.
  """
  return Recipe.objects.create(title=title,slug=slug,body=body)

  class RecipeIndexViewTests(TestCase):
    def test_index_view_with_a_recipe(self):
      """ 
    The index view should create a link with the title as a link.
    """
    new_recipe = create_recipe(title="New Recipe", slug="new-recipe",
        body="This is the body")
    response = self.client.get(reverse('recipe:index'))
    self.assertQuerysetEqual(
        response.context['all_recipes'],
        ['<Recipe: New Recipe>']
        )   

    def test_index_view_without_recipes(self):
      """
      The index view should return No recipes available
      """
      response = self.client.get(reverse('recipe:index'))
      self.assertEqual(reponse.status_code, 200)
      self.assertContains(response, "No recipes are available")

