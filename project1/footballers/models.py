from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        db_table='Category'
    def __str__(self) -> str:
        return self.name

class Footballers(models.Model):
    Category = models.ForeignKey(to="Category", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    country = models.CharField(max_length=100)
    club = models.CharField(max_length=100)
    image = models.ImageField( upload_to='footballers/', blank=True , null=True)

    class Meta:
        db_table='footballers'

    def __str__(self) -> str:
        return  f"{self.Category.name} {self.first_name}"
