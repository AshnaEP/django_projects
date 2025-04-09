from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
    recipe_name=models.CharField(max_length=50)
    ingredients=models.CharField(max_length=50)
    instructions=models.TextField()
    cuisine=models.CharField(max_length=50)
    meal_type=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)  #not mandatory
    updated_at=models.DateTimeField(auto_now=True)      #not mandatory
    image=models.ImageField(upload_to='images',null=True,blank=True)

    def __str__(self):
        return self.recipe_name


class Reviews(models.Model):
    recipe=models.ForeignKey(Recipe,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.TextField()
    rating=models.IntegerField(default=1,validators=[MinValueValidator(1),MaxValueValidator(5)])
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.recipe.recipe_name

