from django.db import models

# Create your models here.


class Kind(models.Model):
    class Meta:
        verbose_name = "種別"
        verbose_name_plural = "種別一覧"
    name = models.CharField(max_length=64)
    isShow = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Ingredients(models.Model):
    class Meta:
        verbose_name = "原料"
        verbose_name_plural = "原料一覧"
    name = models.CharField(max_length=64)
    kind = models.ForeignKey(Kind, on_delete=models.CASCADE)
    alc_percent = models.PositiveIntegerField(default=0)
    isShow = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Construction(models.Model):
    class Meta:
        verbose_name = "製法"
        verbose_name_plural = "製法一覧"
    name = models.CharField(max_length=64)
    isShow = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    class Meta:
        verbose_name = "カテゴリ"
        verbose_name_plural = "カテゴリ一覧"
    name = models.CharField(max_length=128)
    isShow = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Cocktail(models.Model):
    class Meta:
        verbose_name = "カクテル"
        verbose_name_plural = "カクテル一覧"
    name = models.CharField(max_length=256)
    ingredients = models.ManyToManyField(Ingredients, through="Recipe")
    category = models.ManyToManyField(Category, through="CocktailCategory")
    construction = models.ForeignKey(Construction, on_delete=models.CASCADE)
    alc_percent = models.PositiveIntegerField()
    isShow = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    class Meta:
        verbose_name = "レシピ"
        verbose_name_plural = "レシピ一覧"
    ingredients = models.ForeignKey(Ingredients, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    cocktail = models.ForeignKey(Cocktail, on_delete=models.CASCADE)
    # mesure

    def __str__(self):
        return self.cocktail + " <-- " + self.ingredients


class CocktailCategory(models.Model):
    class Meta:
        verbose_name = "カクテル - カテゴリ関連付"
        verbose_name_plural = "カクテル - カテゴリ関連付一覧"
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    cocktail = models.ForeignKey(Cocktail, on_delete=models.CASCADE)

    def __str__(self):
        return self.cocktail + " --> " + self.category
