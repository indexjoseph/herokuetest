from django.urls import path

from . import views
app_name = 'code_journals'
urlpatterns = [
    #Home page
    path('', views.index, name = "index"),

    #Show all topics.
    path('topics/<int:topic_id>', views.topics, name='topics'),
]