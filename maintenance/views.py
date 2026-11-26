from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.utils import timezone

from .models import MaintenanceTask
from .forms import MaintenanceTaskForm
from django.contrib.auth.mixins import UserPassesTestMixin
from accounts.models import CustomUser

class HouseholdUserRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.role == CustomUser.Role.USER


class TaskListView(HouseholdUserRequiredMixin, ListView):
    model = MaintenanceTask
    template_name = 'maintenance/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return MaintenanceTask.objects.filter(
            user=self.request.user
        ).order_by('due_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = timezone.localdate()
        return context


class TaskCreateView(HouseholdUserRequiredMixin, CreateView):
    model = MaintenanceTask
    form_class = MaintenanceTaskForm
    template_name = 'maintenance/task_form.html'
    success_url = reverse_lazy('maintenance:task_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Maintenance task created successfully.')
        return super().form_valid(form)


class TaskDetailView(HouseholdUserRequiredMixin, DetailView):
    model = MaintenanceTask
    template_name = 'maintenance/task_detail.html'
    context_object_name = 'task'

    def get_queryset(self):
        return MaintenanceTask.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = timezone.localdate()
        return context


class TaskUpdateView(HouseholdUserRequiredMixin, UpdateView):
    model = MaintenanceTask
    form_class = MaintenanceTaskForm
    template_name = 'maintenance/task_form.html'
    success_url = reverse_lazy('maintenance:task_list')

    def get_queryset(self):
        return MaintenanceTask.objects.filter(user=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, 'Maintenance task updated successfully.')
        return super().form_valid(form)


class TaskDeleteView(HouseholdUserRequiredMixin, DeleteView):
    model = MaintenanceTask
    template_name = 'maintenance/task_confirm_delete.html'
    success_url = reverse_lazy('maintenance:task_list')

    def get_queryset(self):
        return MaintenanceTask.objects.filter(user=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, 'Maintenance task deleted successfully.')
        return super().form_valid(form)
