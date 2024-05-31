from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.bag, name='bag'),
    path('add/<prints_id>', views.add_to_bag, name='add_to_bag')
]