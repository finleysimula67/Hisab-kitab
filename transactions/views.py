from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.utils.dateparse import parse_date
from django.views.decorators.http import require_POST

from .auth_forms import SignUpForm
from .forms import TransactionForm
from .models import Transaction


def signup(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(
                request,
                "Your account has been created successfully.",
            )
            return redirect("dashboard")
    else:
        form = SignUpForm()

    return render(
        request,
        "registration/signup.html",
        {"form": form},
    )


def user_login(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            login(request, form.get_user())
            messages.success(request, "Welcome back!")
            return redirect("dashboard")
    else:
        form = AuthenticationForm(request)

    for field in form.fields.values():
        field.widget.attrs.update({"class": "form-control"})

    return render(
        request,
        "registration/login.html",
        {"form": form},
    )


@login_required
@require_POST
def user_logout(request):
    logout(request)
    messages.success(request, "You have logged out successfully.")
    return redirect("login")


@login_required
def dashboard(request):
    # Users can only see their own transactions.
    transactions = Transaction.objects.filter(owner=request.user)

    search_query = request.GET.get("q", "").strip()
    transaction_type = request.GET.get("type", "")
    start_date = request.GET.get("start_date", "")
    end_date = request.GET.get("end_date", "")

    if search_query:
        transactions = transactions.filter(
            Q(category__icontains=search_query)
            | Q(note__icontains=search_query)
        )

    valid_types = [
        choice[0]
        for choice in Transaction.TransactionType.choices
    ]

    if transaction_type in valid_types:
        transactions = transactions.filter(type=transaction_type)

    parsed_start_date = parse_date(start_date) if start_date else None
    parsed_end_date = parse_date(end_date) if end_date else None

    if parsed_start_date:
        transactions = transactions.filter(date__gte=parsed_start_date)

    if parsed_end_date:
        transactions = transactions.filter(date__lte=parsed_end_date)

    today = timezone.localdate()

    monthly_transactions = transactions.filter(
        date__year=today.year,
        date__month=today.month,
    )

    monthly_income = sum(
        transaction.amount
        for transaction in monthly_transactions
        if transaction.type == Transaction.TransactionType.INCOME
    )

    monthly_expenses = sum(
        transaction.amount
        for transaction in monthly_transactions
        if transaction.type == Transaction.TransactionType.EXPENSE
    )

    context = {
        "recent_transactions": transactions[:5],
        "monthly_income": monthly_income,
        "monthly_expenses": monthly_expenses,
        "monthly_balance": monthly_income - monthly_expenses,
        "search_query": search_query,
        "selected_type": transaction_type,
        "start_date": start_date,
        "end_date": end_date,
    }

    return render(request, "transactions/dashboard.html", context)


@login_required
def transaction_create(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)

        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.owner = request.user
            transaction.save()

            messages.success(
                request,
                "Transaction added successfully.",
            )
            return redirect("dashboard")
    else:
        form = TransactionForm(
            initial={"date": timezone.localdate()}
        )

    return render(
        request,
        "transactions/transaction_form.html",
        {"form": form},
    )


@login_required
def transaction_edit(request, pk):
    transaction = get_object_or_404(
        Transaction,
        pk=pk,
        owner=request.user,
    )

    if request.method == "POST":
        form = TransactionForm(request.POST, instance=transaction)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Transaction updated successfully.",
            )
            return redirect("dashboard")
    else:
        form = TransactionForm(instance=transaction)

    return render(
        request,
        "transactions/transaction_form.html",
        {
            "form": form,
            "is_edit": True,
        },
    )


@login_required
def transaction_delete(request, pk):
    transaction = get_object_or_404(
        Transaction,
        pk=pk,
        owner=request.user,
    )

    if request.method == "POST":
        transaction.delete()
        messages.success(
            request,
            "Transaction deleted successfully.",
        )
        return redirect("dashboard")

    return render(
        request,
        "transactions/transaction_confirm_delete.html",
        {"transaction": transaction},
    )


@login_required
def transaction_detail(request, pk):
    transaction = get_object_or_404(
        Transaction,
        pk=pk,
        owner=request.user,
    )

    return render(
        request,
        "transactions/transaction_detail.html",
        {"transaction": transaction},
    )
