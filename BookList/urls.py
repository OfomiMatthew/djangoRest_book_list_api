
from django.contrib import admin
from django.urls import path,include

# api endpoints
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('BookListApi.urls')),
    path('__debug__/',include('debug_toolbar.urls')),
]
