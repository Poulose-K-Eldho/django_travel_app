from django.urls import path
from . import views
app_name='myapp'
urlpatterns=[
    path('',views.fun,name='fun'),
    path('foods/<int:foods_id>', views.detail, name='detail')
]