from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView
from accounts.models import CustomUser

class HomeDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/home.html'

class AdminDashboardView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'dashboard/admin_dashboard.html'

    def test_func(self):
        return self.request.user.role == CustomUser.Role.ADMIN

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['account_count'] = CustomUser.objects.count()
        context['household_user_count'] = CustomUser.objects.filter(role=CustomUser.Role.USER).count()
        return context
