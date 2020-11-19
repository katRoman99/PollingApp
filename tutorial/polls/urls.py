from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('latest_polls/', views.latest, name='latest'),
    path('<int:question_id>', views.detail, name='detail'),
    path('about_random_polls/', views.about, name='about'),
    path('create_poll/', views.createPoll, name='create_poll'),
    path('create_poll/new_poll/', views.newPoll, name='new_poll'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('process_choice/', views.process_choice, name='process_choice')

    # path('<int:question_id>/vote/', views.vote, name='vote'),
]