from django.urls import path
from mayflower import views

urlpatterns=[
    path('indexpage/', views.indexpage, name="indexpage"),
    path('adminpage/', views.adminpage, name="adminpage"),
    path('savedata/', views.savedata, name="savedata"),
    path('display/', views.display, name="display"),
    path('editpage/<int:dataid>/', views.editpage, name="editpage"),
    path('updatepage/<int:dataid>/', views.updatepage, name="updatepage"),
    path('deletepage/<int:dataid>/', views.deletepage, name="deletepage"),
    path('catpage/',views.catpage,name="catpage"),
    path('datasave/', views.datasave, name="datasave"),
    path('catdisplay/', views.catdisplay, name="catdisplay"),
    path('cateditpage/<int:dataid>/', views.cateditpage ,name="cateditpage"),
    path('catupdate/<int:dataid>/', views.catupdate, name="catupdate"),
    path('catdelete/<int:dataid>/', views.catdelete, name="catdelete"),
    path('bookpage/', views.bookpage, name="bookpage"),
    path('booksave/', views.booksave, name="booksave"),
    path('bookdisplay/',views.bookdisplay,name="bookdisplay"),
    path('bookedit/<int:dataid>/', views.bookedit, name="bookedit"),
    path('bookupdate/<int:dataid>/', views.bookupdate, name="bookupdate"),
    path('bookdelete/<int:dataid>/', views.bookdelete, name="bookdelete"),
    path('contactsave/', views.contactsave, name="contactsave"),
    path('adminloginpage', views.adminloginpage, name="adminloginpage"),
    path('adminlog/', views.adminlog, name="adminlog")
]

