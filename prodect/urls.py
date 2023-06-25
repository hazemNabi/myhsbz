
from django.urls import path,include
from prodect.views import add_prodect,show_product,delete,manage_prodect,update_product,manage_sections,add_sections,update_section,remov_section
from prodect import views


urlpatterns = [
    path('addprodect/', views.add_prodect, name='addprodect'),
    path('show_product/<int:id>', views.show_product,name='show_product'),
    path('manage_prodect/', views.manage_prodect,name='manage_prodect'),
    path('manage_sections/', views.manage_sections,name='manage_sections'),
    path('addsections/', views.add_sections,name='addsections'),
    # path('commission/<int:id>',commission,name='commission'),
    path('update/<int:id>', views.update_product,name='update_product'),
    path('delete/<int:id>', views.delete,name='delete'),
    path('updateSe/<int:id>', views.update_section,name='update_section'),
    path('deleteSe/<int:id>', views.remov_section,name='remov_section'),
    
]