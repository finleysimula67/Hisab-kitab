
from decimal import Decimal

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Transaction


class AuthenticationTests(TestCase):
    def test_signup_creates_account_and_logs_user_in(self):
        response = self.client.post(
            reverse("signup"),
            {
                "username": "newuser",
                "email": "newuser@example.com",
                "password1": "TestPassword!928",
                "password2": "TestPassword!928",
            },
        )

        self.assertRedirects(response, reverse("dashboard"))
        self.assertTrue(
            User.objects.filter(username="newuser").exists()
        )
        self.assertTrue(
            response.wsgi_request.user.is_authenticated
        )

    def test_dashboard_requires_login(self):
        response = self.client.get(reverse("dashboard"))

        self.assertRedirects(
            response,
            f"{reverse('login')}?next={reverse('dashboard')}",
        )


class TransactionOwnershipTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="owner",
            password="TestPassword!928",
        )
        self.other_user = User.objects.create_user(
            username="other",
            password="TestPassword!928",
        )
        self.transaction = Transaction.objects.create(
            owner=self.user,
            type=Transaction.TransactionType.EXPENSE,
            amount=Decimal("250.00"),
            category="Food",
            date="2026-10-10",
            note="Lunch",
        )

    def test_dashboard_shows_only_current_users_transactions(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse("dashboard"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Food")
        self.assertEqual(
            list(response.context["recent_transactions"]),
            [self.transaction],
        )

    def test_user_cannot_view_another_users_transaction(self):
        self.client.force_login(self.other_user)

        response = self.client.get(
            reverse(
                "transaction_detail",
                kwargs={"pk": self.transaction.pk},
            )
        )

        self.assertEqual(response.status_code, 404)
