from django.urls import path
from . import views

app_name = 'quiz_app'

urlpatterns = [
    path('start/', views.start_quiz, name='start'),
    path('question/', views.get_question, name='question'),
    path('submit/', views.submit_answer, name='submit'),
    path('results/', views.quiz_results, name='results'),
]
