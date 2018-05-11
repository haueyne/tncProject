from django.db import models

# Create your models here.


class Kind(models.Model):
    """カクテル原料の種別"""
    name = models.CharField(max_length=32, unique=True, verbose_name='種別名')
    is_show = models.BooleanField(default=True, verbose_name='表示可否')

    class Meta:
        verbose_name = "種別"
        verbose_name_plural = "種別一覧"

    def __str__(self):
        return self.name


class Material(models.Model):
    """カクテル原料"""
    name = models.CharField(max_length=128, unique=True, verbose_name='原料名')
    kind = models.ForeignKey('Kind',
                             on_delete=models.CASCADE,
                             verbose_name='カクテル種別')
    is_show = models.BooleanField(default=True, verbose_name='表示可否')

    class Meta:
        verbose_name = "原料"
        verbose_name_plural = "原料一覧"

    def __str__(self):
        return self.name


class HowToMake(models.Model):
    """カクテルの作り方"""
    name = models.CharField(max_length=16, unique=True, verbose_name='製法名')
    is_show = models.BooleanField(default=True, verbose_name='表示可否')

    class Meta:
        verbose_name = "製法"
        verbose_name_plural = "製法一覧"

    def __str__(self):
        return self.name


class Cocktail(models.Model):
    """カクテル"""
    IMP_CHOICES = tuple(zip(range(1, 6), range(1, 6)))

    name = models.CharField(max_length=128, unique=True, verbose_name='カクテル名')
    materials = models.ManyToManyField(Material,
                                       through='Recipe',
                                       through_fields=('cocktail', 'material'),
                                       related_name='recipe_materials',
                                       verbose_name='原料名')
    alc_percent = models.FloatField(default=0.0, null=True, verbose_name='度数(%)')
    how_to_make = models.ForeignKey('HowToMake',
                                    on_delete=models.CASCADE,
                                    verbose_name='製法')
    base_material = models.ForeignKey('Material',
                                      on_delete=models.CASCADE,
                                      null=True,
                                      related_name='base_material',
                                      verbose_name='ベース原料')
    importance = models.PositiveIntegerField(choices=IMP_CHOICES, default=IMP_CHOICES[0][0],
                                             verbose_name='頻出度合い')
    is_show = models.BooleanField(default=True, verbose_name='表示可否')

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
        # ('pq', '適量'),
    )

    cocktail = models.ForeignKey('Cocktail', on_delete=models.CASCADE,
                                 verbose_name='カクテル')
    material = models.ForeignKey('Material', on_delete=models.CASCADE,
                                 verbose_name='原料')
    quantity = models.PositiveIntegerField(default=0, verbose_name='分量')
    unit_of_quantity = models.CharField(
        max_length=4,
        null=True,
        choices=UNIT_OF_QUANTITY_CHOICES,
        default=UNIT_OF_QUANTITY_CHOICES[0][0],
        verbose_name='分量単位',
    )

    class Meta:
        verbose_name = "レシピ"
        verbose_name_plural = "レシピ一覧"

    def __str__(self):
        return '{coc} <=== {mat}'.format(coc=self.cocktail, mat=self.material)
