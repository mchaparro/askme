from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from askme.users.models import *
from django.shortcuts import render

from django.http import HttpResponse
import json
User = get_user_model()

def home(request):
    count = Question.objects.filter(pending=True).count()
    data = {"count": count}
    return render(request,'pages/home.html',data )



def pending_questions(request):
    questions = Question.objects.filter(pending=True).order_by("-created_on")
    data = {"questions": questions,
            "count" : questions.count()}
    return render(request,'pages/about.html',data )

def create_question(request):
    question = request.GET.get('question','blank question')
    if request.user.is_authenticated:
         Question.objects.create(question=question, created_by = request.user)
    else:
        Question.objects.create(question=question)
    count = Question.objects.filter(pending=True).count()
    data = {"count": count}
    return HttpResponse(json.dumps(data), content_type='application/json')

def provide_answer(request):
    question = request.GET.get('question',None)
    q = Question.objects.get(id=question)
    q.pending=False
    q.save()
    count = Question.objects.filter(pending=True).count()
    data = {"count": count}
    return HttpResponse(json.dumps(data), content_type='application/json')

class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()


class UserListView(LoginRequiredMixin, ListView):

    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_list_view = UserListView.as_view()


class UserUpdateView(LoginRequiredMixin, UpdateView):

    model = User
    fields = ["name"]

    def get_success_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})

    def get_object(self):
        return User.objects.get(username=self.request.user.username)


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):

    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()
