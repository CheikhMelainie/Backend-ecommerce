from django.urls import path
from  primark import views 
from .views import UserCreate,LoginView

urlpatterns = [
    path('produits/',views.Produit_List),
    path('produits/<int:pk>',views.Produit_List_pk),
    path('categories/',views.Categoy_List),
    path('categories/<int:pk>',views.Categoy_List_pk),
    path("users/", UserCreate.as_view(), name="user_create"),
    path("login/", LoginView.as_view(), name="login"),
]