import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseForbidden, HttpResponse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, View
from django.views.generic.detail import SingleObjectMixin

from vertineuch.users.models import User
from .forms import LessonCreationForm, LessonChangeForm
from .models import Lesson


class LessonListView(ListView):
    model = Lesson
    paginate_by = 20


class LessonCreateView(LoginRequiredMixin, CreateView):
    model = Lesson
    form_class = LessonCreationForm
    success_url = reverse_lazy('lessons:list')

    def form_valid(self, form):
        form.instance.teacher = self.request.user
        return super(LessonCreateView, self).form_valid(form)


class LessonDetailView(DetailView):
    model = Lesson


class LessonUpdateView(LoginRequiredMixin, UpdateView):
    model = Lesson

    form_class = LessonChangeForm
    success_url = reverse_lazy('lessons:list')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.teacher != self.request.user:
            return HttpResponseForbidden("You are not allowed to update this Post")
        return super(LessonUpdateView, self).dispatch(request, *args, **kwargs)


class LessonDeleteView(LoginRequiredMixin, DeleteView):
    model = Lesson
    success_url = reverse_lazy('lessons:list')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.teacher != self.request.user:
            return HttpResponseForbidden("You are not allowed to delete this Post")
        return super(LessonDeleteView, self).dispatch(request, *args, **kwargs)


class LessonSubscribeView(LoginRequiredMixin, SingleObjectMixin, View):
    model = Lesson

    def dispatch(self, request, *args, **kwargs):
        user = User(self.request.user)
        user = user.id
        lesson = self.model(self.get_object())
        lesson = lesson.id
        if user.subscribed_lessons.filter(subscribed_lessons__id=lesson.pk).exists():
            user.subscribed_lessons.remove(lesson)
            message = 'UNSUB'
        else:
            user.subscribed_lessons.add(lesson)
            message = 'SUB'

        ctx = {'message': message}

        return HttpResponse(json.dumps(ctx), content_type='application/json')

