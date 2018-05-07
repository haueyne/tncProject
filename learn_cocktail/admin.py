from django.contrib import admin
from .models import Cocktail
from .models import HowToMake
from .models import Kind
from .models import Material
from .models import Recipe

# Register your models here.


class RecipeInline(admin.TabularInline):
    model = Recipe
    extra = 2


class CocktailAdmin(admin.ModelAdmin):
    inlines = [RecipeInline]
    list_display = ('name',
                    'base_material',
                    'alc_percent',
                    'how_to_make',
                    'is_show')


class KindAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_show')


class HowToMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_show')


class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name', 'kind', 'is_show')


admin.site.register(Kind, KindAdmin)
admin.site.register(HowToMake, HowToMakeAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(Cocktail, CocktailAdmin)
