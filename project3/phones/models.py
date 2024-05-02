from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        db_table='Category'
    def __str__(self) -> str:
        return self.name

class Phones(models.Model):
    Category = models.ForeignKey(to="Category", on_delete=models.CASCADE)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10)
    image = models.ImageField( upload_to='phones/', blank=True , null=True)

    class Meta:
        db_table='phones'

    def __str__(self) -> str:
        return  f"{self.Category.name} {self.brand}"
