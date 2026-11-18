from django.test import TestCase
from django.urls import reverse
from .models import CustomUser

class AccountFeatureTests(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='homeuser', email='home@example.com', password='SafePass123!',
            full_name='Home User'
        )
        self.admin = CustomUser.objects.create_user(
            username='siteadmin', email='admin@example.com', password='SafePass123!',
            full_name='Site Admin', role=CustomUser.Role.ADMIN
        )

    def test_registration_creates_household_user(self):
        response = self.client.post(reverse('accounts:signup'), {
            'full_name': 'New Person', 'username': 'newperson',
            'email': 'new@example.com', 'contact_number': '',
            'password1': 'SafePass123!', 'password2': 'SafePass123!',
        })
        self.assertRedirects(response, reverse('accounts:login'))
        created = CustomUser.objects.get(username='newperson')
        self.assertEqual(created.role, CustomUser.Role.USER)
        self.assertTrue(created.check_password('SafePass123!'))

    def test_dashboard_requires_login(self):
        response = self.client.get(reverse('dashboard:home'))
        self.assertRedirects(response, f'{reverse("accounts:login")}?next={reverse("dashboard:home")}')

    def test_household_user_cannot_open_admin_dashboard(self):
        self.client.login(username='homeuser', password='SafePass123!')
        response = self.client.get(reverse('dashboard:admin_dashboard'))
        self.assertEqual(response.status_code, 403)

    def test_admin_can_open_admin_dashboard(self):
        self.client.login(username='siteadmin', password='SafePass123!')
        response = self.client.get(reverse('dashboard:admin_dashboard'))
        self.assertEqual(response.status_code, 200)

    def test_profile_is_current_users_profile(self):
        self.client.login(username='homeuser', password='SafePass123!')
        response = self.client.get(reverse('accounts:profile'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Home User')
