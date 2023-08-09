"""
URL configuration for motorqtask project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from motorqtask import views
from motorqtask import tasks

urlpatterns = [
    path('admin/', admin.site.urls),
    path('coins/', views.get_coins),
    path('coins/price/<str:coinId>', views.get_coinprice),

]

# Initialize the scheduler
tasks.scheduler.add_job(tasks.update_coin_details, 'interval', minutes=1)
# tasks.scheduler.add_job(tasks.price_update, 'interval', minutes=1)
tasks.scheduler.start()