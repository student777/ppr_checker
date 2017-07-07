from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name


class Goods(models.Model):
    name = models.CharField(max_length=45)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Unit(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name


class Deal(models.Model):
    price = models.PositiveIntegerField()
    content = models.CharField(max_length=255)
    is_available = models.BooleanField(default=True)
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.goods.name + str(self.price) + self.unit.name
