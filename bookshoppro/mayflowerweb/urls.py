from django.urls import path
from mayflowerweb import views


urlpatterns=[
    path('', views.homepage, name="homepage"),
    path('aboutpage/', views.aboutpage, name="aboutpage"),
    path('contactpage/', views.contactpage, name="contactpage"),
    path('discategory/<itemcatg>', views.discategory, name="discategory"),
    path('disauther/<itemcat>', views.disauther, name="disauther"),
    path('bookdetails/<int:dataid>/', views.bookdetails, name="bookdetails"),
    path('pagelogin/', views.pagelogin, name="pagelogin"),
    path('consave/', views.consave, name="consave"),
    path('logindata/', views.logindata, name="logindata"),
    path('registerdata', views.registerdata, name="registerdata"),
    path('logout/', views.logout, name="logout")


]