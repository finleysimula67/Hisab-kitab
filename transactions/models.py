from django.conf import settings
from django.db import models


class Transaction(models.Model):
    class TransactionType(models.TextChoices):
        INCOME = "INCOME", "Income"
        EXPENSE = "EXPENSE", "Expense"

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="transactions",
        null=True,
        blank=True,
    )

    type = models.CharField(
        max_length=7,
        choices=TransactionType.choices,
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    category = models.CharField(
        max_length=100,
    )

    date = models.DateField()

    note = models.TextField(
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["-date", "-created_at"]

    def __str__(self):
        return f"{self.get_type_display()} - {self.amount} ({self.category})"
