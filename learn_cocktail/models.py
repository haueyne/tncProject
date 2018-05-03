from django.db import models

# Create your models here.


class Kind(models.Model):
    """カクテル原料の種別"""
    name = models.CharField(max_length=32, unique=True)
    is_show = models.BooleanField(default=True)

    class Meta:
        verbose_name = "種別"
        verbose_name_plural = "種別一覧"

    def __str__(self):
        return self.name


class Material(models.Model):
    """カクテル原料"""
    name = models.CharField(max_length=128, unique=True)
    kind = models.ForeignKey('Kind', on_delete=models.CASCADE)
    is_show = models.BooleanField(default=True)

    class Meta:
        verbose_name = "原料"
        verbose_name_plural = "原料一覧"

    def __str__(self):
        return self.name


class HowToMake(models.Model):
    """カクテルの作り方"""
    name = models.CharField(max_length=16, unique=True)
    is_show = models.BooleanField(default=True)

    class Meta:
        verbose_name = "製法"
        verbose_name_plural = "製法一覧"

    def __str__(self):
        return self.name


class Cocktail(models.Model):
    """カクテル"""
    name = models.CharField(max_length=128, unique=True)
    materials = models.ManyToManyField(Material,
                                       through='Recipe',
                                       through_fields=('cocktail', 'material'),
                                       related_name='recipe_materials')
    alc_percent = models.PositiveIntegerField(default=0)
    how_to_make = models.ForeignKey('HowToMake', on_delete=models.CASCADE)
    base_material = models.ForeignKey('Material', on_delete=models.CASCADE,
                                      related_name='base_material')
    is_show = models.BooleanField(default=True)

    class Meta:
        verbose_name = "カクテル"
        verbose_name_plural = "カクテル一覧"

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """カクテルレシピ"""
    UNIT_OF_QUANTITY_CHOICES = (
        ('ml', 'ml'),
        ('tsp', 'ティースプーン'),
        ('pq', '適量'),
    )

    cocktail = models.ForeignKey('Cocktail', on_delete=models.CASCADE)
    material = models.ForeignKey('Material', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(blank=True, null=True)
    unit_of_quantity = models.CharField(
        max_length=4,
        choices=UNIT_OF_QUANTITY_CHOICES,
        default=UNIT_OF_QUANTITY_CHOICES[0][0],
    )

    class Meta:
        verbose_name = "レシピ"
        verbose_name_plural = "レシピ一覧"

    def __str__(self):
        return '{coc} <=== {mat}'.format(coc=self.cocktail, mat=self.material)
