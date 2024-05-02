from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        db_table='Category'
    def __str__(self) -> str:
        return self.name

class Pets(models.Model):
    Category = models.ForeignKey(to="Category", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50)
    breed = models.CharField(max_length=100, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table='pets'

    def __str__(self) -> str:
        return  f"{self.Category.name} {self.name}"