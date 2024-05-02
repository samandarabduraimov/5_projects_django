from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        db_table='Category'
    def __str__(self) -> str:
        return self.name

class Countries(models.Model):
    Category = models.ForeignKey(to="Category", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=3, unique=True)
    image = models.ImageField( upload_to='countries/', blank=True , null=True)

    class Meta:
        db_table='countries'

    def __str__(self) -> str:
        return  f"{self.Category.name} {self.name}"
