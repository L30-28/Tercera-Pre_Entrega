
from django.urls import path, include
from .views import*

urlpatterns = [
    #______________________________________Menu principal
    path('',home, name='home'),
    path('Nike/',nike, name='Nike'),
    path('Adidas/',adidas, name='Adidas'),
    path('Puma/',puma, name='Puma'),
    path('Remeras/',remeras, name='Remeras'),
    
    #______________________________________Formularios
    path('zapatilla_form/',zapatillaForm,name="zapatilla_form"),
    path('nike_form/',nikeform,name="nike_form"),
    path('puma_form/',pumaform,name="puma_form"),
    path('remeras_form/',remerasform,name="remeras_form"),
    
    #_____________________________________Busqueda
    path('buscar/',buscar,name="buscar"),
    path('encontrar/',encontrar,name="encontrar"),
    
     #_____________________________________Nike
    #path('nike/',NikeList.as_view(),name="Nike"),
    #path('nike_create/',NikeCreate.as_view(),name="nike_create"),
    #path('nike_update/<int:pk>',NikeUpgrade.as_view(),name="nike_update"),
    #path('nike_delete/<int:pk>',NikeDelete.as_view(),name="nike_delete"),
    
]
