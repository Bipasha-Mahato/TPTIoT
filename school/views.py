from django.shortcuts import render, HttpResponse
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *

# Create your views here.
class ClassListView(ListView):
    model = Class
    classes = Class.objects.all()
    template_name = 'school/school-home.html' # default: <app>/<model>_<view_type>.html

    def get_context_data(self, *args, **kwargs):
        class_list = Class.objects.all()
        context = super(ClassListView, self).get_context_data(*args, **kwargs)
        context["class_list"] = class_list
        return context

def classView(request, class_id):
    subject_list = Subject.objects.filter(course=Class.objects.filter(id=class_id).first())

    return render(request, 'school/school-classes.html', {'subject_list':subject_list})

def subView(request, class_id, subject_id):
    assignment_list = reversed(Assignment.objects.filter(subject=Subject.objects.filter(id=subject_id).first()).filter(course=Class.objects.filter(id=class_id).first()))
    quiz_list = reversed(Quiz.objects.filter(subject=Subject.objects.filter(id=subject_id).first()).filter(course=Class.objects.filter(id=class_id).first()))

    return render(request, 'school/class-subjects.html', {'assignment_list':assignment_list, 'quiz_list':quiz_list})

#####

class AssignmentDetailView(DetailView):
    model = Assignment
    
class AssignmentCreateView(LoginRequiredMixin, CreateView):
    model = Assignment
    fields = ['title', 'course', 'subject', 'desc', 'file']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class AssignmentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Assignment
    fields = ['title', 'course', 'subject', 'desc', 'file']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        assignment = self.get_object()
        if self.request.user == assignment.author:
            return True
        return False

class AssignmentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Assignment
    success_url = '/'

    def test_func(self):
        assignment = self.get_object()
        if self.request.user == assignment.author:
            return True
        return False

#####

class QuizDetailView(DetailView):
    model = Quiz
    
class QuizCreateView(LoginRequiredMixin, CreateView):
    model = Quiz
    fields = ['title', 'course', 'subject', 'desc', 'file']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class QuizUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Quiz
    fields = ['title', 'course', 'subject', 'desc', 'file']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        quiz = self.get_object()
        if self.request.user == quiz.author:
            return True
        return False

class QuizDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Quiz
    success_url = '/'

    def test_func(self):
        quiz = self.get_object()
        if self.request.user == quiz.author:
            return True
        return False
