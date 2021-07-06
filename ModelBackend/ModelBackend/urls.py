from django.contrib import admin
from django.urls import path
from firstPage import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('admin/', admin.site.urls),
    path('scoreJson',csrf_exempt(views.scoreJson),name="Score Application"),
    path('scoreFile',csrf_exempt(views.scoreFile), name ="Score FIle"),
]
