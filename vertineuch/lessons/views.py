from django.core.urlresolvers import reverse_lazy
from vanilla import ListView, CreateView, DetailView, UpdateView, DeleteView
from .forms import courForm
from .models import lesson


class courList(ListView):
    model = lesson
    paginate_by = 20


class courCreate(CreateView):
    model = lesson
    form_class = courForm
    success_url = reverse_lazy('lessons:list')


class courDetail(DetailView):
    model = lesson


class courUpdate(UpdateView):
    model = lesson
    form_class = courForm
    success_url = reverse_lazy('lessons:list')


class courDelete(DeleteView):
    model = lesson
    success_url = reverse_lazy('lessons:list')
