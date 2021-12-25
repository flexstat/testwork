from django.urls import path

from core import views

urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    path('details/<int:pk>', views.HomeDetailView.as_view(), name='details_page'),
    path('editpage', views.ArticleCreateView.as_view(), name='editpage'),
    path('update_page/<int:pk>', views.ArticleUpdateView.as_view(), name='update_page'),
    path('delete-page/<int:pk>', views.ArticleDeleteView.as_view(), name='delete_page'),
    path('login', views.MyprojectLoginView.as_view(), name='login_page'),
    path('registr', views.RegistrUserView.as_view(), name='registr_page'),
    path('logout', views.MyprojectLogOut.as_view(), name='logout_page'),
     
     
    ]
