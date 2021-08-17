from django.urls import path
from .views import (
    ClassListView,
    AssignmentDetailView,
    AssignmentCreateView,
    AssignmentUpdateView,
    AssignmentDeleteView,
    QuizDetailView,
    QuizCreateView,
    QuizUpdateView,
    QuizDeleteView
)
from . import views

urlpatterns = [
    # path('', views.schoolHome, name='school-home'),
    path('', ClassListView.as_view(), name='school-home'),
    path('<int:class_id>/', views.classView, name='school-classes'),
    path('<int:class_id>/<int:subject_id>/', views.subView, name='class-subjects'),
    # blank
    path('class-assignments/<int:pk>/', AssignmentDetailView.as_view(), name='assignment-detail'),
    path('class-assignments/new/', AssignmentCreateView.as_view(), name='assignment-create'),
    path('class-assignments/<int:pk>/update/', AssignmentUpdateView.as_view(), name='assignment-update'),
    path('class-assignments/<int:pk>/delete/', AssignmentDeleteView.as_view(), name='assignment-delete'),
    # blank
    path('class-quizzes/<int:pk>/', QuizDetailView.as_view(), name='quiz-detail'),
    path('class-quizzes/new/', QuizCreateView.as_view(), name='quiz-create'),
    path('class-quizzes/<int:pk>/update/', QuizUpdateView.as_view(), name='quiz-update'),
    path('class-quizzes/<int:pk>/delete/', QuizDeleteView.as_view(), name='quiz-delete')
]