
from django import forms

from .models import Transaction


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = [
            "type",
            "amount",
            "category",
            "date",
            "note",
        ]

        widgets = {
            "date": forms.DateInput(
                attrs={"type": "date"}
            ),
            "note": forms.Textarea(
                attrs={"rows": 3}
            ),
        }

    def clean_amount(self):
        amount = self.cleaned_data["amount"]

        if amount <= 0:
            raise forms.ValidationError(
                "Amount must be greater than zero."
            )

        return amount

    def clean_category(self):
        category = self.cleaned_data["category"].strip()

        if not category:
            raise forms.ValidationError(
                "Category cannot be empty."
            )

        return category
