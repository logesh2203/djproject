from django.contrib import admin
from django.urls import path, include   # ✅ path is imported here

urlpatterns = [
    path('', include('blog.urls')),
    path('admin/', admin.site.urls),
]
