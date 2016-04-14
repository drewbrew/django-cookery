'''Models for recipes and menus'''

from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Ingredient(models.Model):
    '''Basic ingredient class'''

    name = models.CharField(_('Name'), max_length=100, unique=True)
    notes = models.TextField(blank=True, null=True)
    # TODO add nutritional data? dry/liquid measure?

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    '''Through-field for many-to-many relationship between Ingredient and
    Recipe'''
    ingredient = models.ForeignKey('Ingredient', help_text=_('Ingredient'))
    recipe = models.ForeignKey('Recipe', help_text=_('Ingredient'))
    quantity = models.PositiveSmallIntegerField(
        _('Amount used'), blank=True, null=True)
    # TODO make this into a foreign key to minimize typos?
    unit_of_measure = models.CharField(
        _('Unit of measure'),
        help_text=_('pounds, ounces, cups, kilograms, ...'),
        max_length=50, blank=True, null=True)
    preparation_method = models.CharField(
        _('Means of preparation'),
        help_text=_('chopped, diced, julienned, etc.'),
        max_length=50, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        ret = '%s %s %s %s for recipe %s' % (
            self.quantity,
            self.unit_of_measure,
            self.preparation_method,
            self.ingredient,
            self.recipe)
        return ret.lstrip().rstrip()


class Recipe(models.Model):
    '''A guide used to create a food product.'''
    name = models.CharField(_('Name'), max_length=100, unique=True)
    author = models.CharField(
        _('Author'), max_length=100, blank=True, null=True)
    preparation_time = models.TimeField(
        _('Time required in active preparation'), blank=True,
        null=True)
    idle_time = models.TimeField(
        _('Waiting time required'), blank=True, null=True,
        help_text=_('e.g. marinating time, standing time'))
    cook_time = models.TimeField(
        _('Time spent actively cooking/baking/grilling'),
        blank=True, null=True)
    outdoor_cooking_friendly = models.BooleanField(
        _('Whether the meal is suitable for outdoor cooking'),
        default=False)
    tags = models.ManyToManyField(
        'RecipeTag', help_text=_('Tags'), blank=True)
    ingredients = models.ManyToManyField(
        'Ingredient', help_text=_('Ingredients'),
        through='RecipeIngredient',
        related_name='recipes')
    instructions = models.TextField(_('Instructions'))
    notes = models.TextField(blank=True, null=True)
    # TODO add timestamp/last modified by

    class Meta:
        ordering = ('name', 'author', )

    def __str__(self):
        return self.name


class RecipeTag(models.Model):
    '''Tag used to describe a recipe, e.g. Asian or Appetizer'''
    name = models.CharField(_('Name'), max_length=100, unique=True)

    def __str__(self):
        return self.name
