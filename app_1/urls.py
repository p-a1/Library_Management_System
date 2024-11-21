from django.urls import path
from .views import index,books,update,delet,delet_cata
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',index,name='index'),
    path('page/books',books,name='books'),
    path('books/update/<int:id>',update,name='update'),
    path('books/delete/<int:id>',delet,name='delete'),
    path('books/delete_cata/<int:id>',delet_cata,name='delete_cata')
    
]+ static(settings.MEDIA_URL,document_root =settings.MEDIA_ROOT)
