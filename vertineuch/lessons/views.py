from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseForbidden
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

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
