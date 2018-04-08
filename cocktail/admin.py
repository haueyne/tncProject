from django.contrib import admin
from .models import Cocktail, Kind, Ingredients, Category, Recipe, CocktailCategory, Construction

# Register your models here.


class RecipeInline(admin.TabularInline):
    model = Recipe
    extra = 2


class CategoryInline(admin.TabularInline):
    model = CocktailCategory
    extra = 0


class KindAdmin(admin.ModelAdmin):
    list_display = ("name", "isShow")


class IngredientsAdmin(admin.ModelAdmin):
    list_display = ("name", "isShow")


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "isShow")


class CocktailAdmin(admin.ModelAdmin):
    list_display = ("name", "isShow")
    inlines = [RecipeInline, CategoryInline]


admin.site.register(Construction)
admin.site.register(Kind, KindAdmin)
admin.site.register(Ingredients, IngredientsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Cocktail, CocktailAdmin)
