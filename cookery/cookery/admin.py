'''Admin setup for our models'''

from django.contrib import admin

from . import models


for model in [
        models.Recipe, models.Ingredient, models.RecipeIngredient,
        models.RecipeTag]:
    admin.site.register(model)
