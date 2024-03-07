from unicodedata import category
from django.db import models
from django.contrib.auth.models import User as AuthUser

class UserProfile(models.Model):
    user = models.OneToOneField(AuthUser, on_delete=models.CASCADE)
    prenom = models.CharField(max_length=150)
    telephone = models.CharField(max_length=200)
    adresse = models.CharField(max_length=150)
    def __str__(self):
         return self.user.username

class Category(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nom

class Produit(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    prix = models.DecimalField(max_digits=10,decimal_places=2)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return self.nom

class Favorite(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user.user.username}'s favorite - {self.product.name}"