import json
import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseForbidden, HttpResponse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

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

    def get_context_data(self, **kwargs):
        obj = Lesson(self.get_object()).id
        context = super(LessonDetailView, self).get_context_data(**kwargs)

        date_list = []
        date = datetime.datetime(obj.start_date.year, obj.start_date.month, obj.start_date.day)
        end_date = datetime.datetime(obj.end_date.year, obj.end_date.month, obj.end_date.day)

        while date <= end_date:
            date_list.append(date)
            date = date + datetime.timedelta(days=obj.frequency)

        extra_context = {'dates': date_list}

        context.update(extra_context)
        return context


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


class LessonSubscribeView(LoginRequiredMixin, DetailView):
    model = Lesson
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        user = User(self.request.user)
        user = user.id
        lesson = self.model(self.get_object())
        lesson = lesson.id

        if lesson in user.subscribed_lessons.all():
            user.subscribed_lessons.remove(lesson)
            is_sub = False
        else:
            user.subscribed_lessons.add(lesson)
            is_sub = True

        ctx = {'is_sub': is_sub}

        return HttpResponse(json.dumps(ctx), content_type='application/json')

