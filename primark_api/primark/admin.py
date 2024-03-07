from django.contrib import admin
from .models import AuthUser,UserProfile,Produit,Category,Favorite
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Produit)
admin.site.register(Category)
admin.site.register(Favorite)