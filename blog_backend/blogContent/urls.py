from django.conf.urls import url
from . import views

app_name = 'blogContent'

urlpatterns = [
    url(r'^gethomecontent/', views.showBlogList),
]

