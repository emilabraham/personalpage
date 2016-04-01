from django.shortcuts import render, get_object_or_404
from recipe.models import Recipe

def index(request):
  all_recipes = Recipe.objects.order_by('-title')
  context = {'all_recipes': all_recipes}
  return render(request, 'recipe/index.html', context)

def detail(request, slug):
  context = {'selected_recipe': get_object_or_404(Recipe,slug=slug)}
  return render(request, 'recipe/detail.html', context)
