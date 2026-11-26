from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView
from django.utils import timezone
from accounts.models import CustomUser
from maintenance.models import MaintenanceTask


class HomeDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = timezone.localdate()
        tasks = MaintenanceTask.objects.filter(user=self.request.user)

        total_count = tasks.count()
        completed_count = tasks.filter(
            status=MaintenanceTask.Status.COMPLETED
        ).count()
        overdue_count = tasks.exclude(
            status=MaintenanceTask.Status.COMPLETED
        ).filter(due_date__lt=today).count()
        pending_count = tasks.filter(
            status=MaintenanceTask.Status.PENDING,
            due_date__gte=today
        ).count()

        context['total_count'] = total_count
        context['pending_count'] = pending_count
        context['completed_count'] = completed_count
        context['overdue_count'] = overdue_count
        context['completion_rate'] = round(
            (completed_count / total_count) * 100, 1
        ) if total_count else 0

        return context


class AdminDashboardView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'dashboard/admin_dashboard.html'

    def test_func(self):
        return self.request.user.role == CustomUser.Role.ADMIN

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['account_count'] = CustomUser.objects.count()
        context['household_user_count'] = CustomUser.objects.filter(
            role=CustomUser.Role.USER
        ).count()
        return context
