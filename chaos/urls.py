from django.conf.urls import url

from . import views

app_name = 'chaos'
urlpatterns = [
    # ex: /chaos/
    url(r'^response/$', views.response, name='response'),
    # ex: /chaos/5/
    url(r'^select/', views.select, name='select'),
    # ex: /chaos/5/results/
    url(r'^set_mode/', views.set_mode, name='set_mode'),
]
