# Django Models and ORM

**Project:** Hisab-Kitab
**Topic:** Models, relationships, form saving, and database persistence

## 1. What Is a Django Model?

A Django model is a Python class that defines the structure and behavior of database-backed data.

```python
class Transaction(models.Model):
    category = models.CharField(max_length=100)
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )
```

Django's ORM maps model instances to database records and provides an API for querying and saving data.

**Java comparison:** A Django model has a role similar to a JPA entity, although Django models also provide ORM behavior directly.

## 2. Model Fields

| Django field | Purpose | Java comparison |
|---|---|---|
| `CharField` | Stores short text | `String` |
| `TextField` | Stores longer text | `String` |
| `DecimalField` | Stores decimal values with defined precision | `BigDecimal` |
| `DateField` | Stores a calendar date | `LocalDate` |
| `DateTimeField` | Stores date and time | `LocalDateTime` or an appropriate date-time type |
| `ForeignKey` | Defines a relationship to another model | Similar to a JPA `@ManyToOne` relationship |

## 3. Choices with `TextChoices`

Hisab-Kitab defines transaction types like this:

```python
class TransactionType(models.TextChoices):
    INCOME = "INCOME", "Income"
    EXPENSE = "EXPENSE", "Expense"
```

Each choice contains a stored value and a display label.

- `INCOME` stores `"INCOME"` and displays `Income`.
- `EXPENSE` stores `"EXPENSE"` and displays `Expense`.

**Why it matters:** Defined choices make the accepted values consistent across the application.

**Java comparison:** Similar in purpose to using an enum.

## 4. Understanding the Owner Relationship

```python
owner = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,
    related_name="transactions",
    null=True,
    blank=True,
)
```

This relationship connects a transaction to its user.

- `settings.AUTH_USER_MODEL`: references Django's configured user model.
- `on_delete=models.CASCADE`: deleting the referenced user deletes related transactions.
- `related_name="transactions"`: allows access through `user.transactions`.
- `null=True`: permits a database `NULL` for the relationship.
- `blank=True`: allows the relationship to be omitted during form validation.

**Important design note:** Hisab-Kitab currently permits transactions without an owner at the model/database level. For a multi-user finance application, new transactions should be assigned to the authenticated user, and ownership must be enforced when accessing existing records.

## 5. Understanding `form.is_valid()`

```python
if form.is_valid():
    # Process validated form data.
    ...
```

Django validates submitted data using the form's validation rules. If validation fails, the application should return the form with its errors instead of saving invalid data.

**Java comparison:** Conceptually similar to validating a request DTO before processing it in a Spring Boot application.

## 6. Understanding `form.save(commit=False)`

Hisab-Kitab uses this pattern when creating transactions:

```python
if form.is_valid():
    transaction = form.save(commit=False)
    transaction.owner = request.user
    transaction.save()
```

### What happens?

1. `form.is_valid()` validates the submitted data.
2. `form.save(commit=False)` creates a model instance without saving it to the database yet.
3. `transaction.owner = request.user` assigns the authenticated user.
4. `transaction.save()` saves the transaction with its owner assigned.

### Why use `commit=False`?

The application needs to assign the owner before the transaction is saved. `commit=False` gives us the opportunity to set additional fields first.

### What if we omit `commit=False`?

Consider this alternative:

```python
if form.is_valid():
    transaction = form.save()
    transaction.owner = request.user
    transaction.save()
```

In the current model, where `owner` can be `NULL`, this can work:

1. `form.save()` inserts the transaction without an owner.
2. The owner is assigned to the in-memory instance.
3. The second `transaction.save()` updates the existing database record.

This performs two database writes instead of one. If the owner were required, the initial save could fail.

**Key takeaway:** Use `commit=False` when you need to modify a model instance before saving it.

## 7. The Purpose of `transaction.save()`

```python
transaction.save()
```

This persists the model instance to the database. For a new instance, Django normally inserts a record. For an existing instance, it normally updates the record.

**Java comparison:** Similar in purpose to persisting an entity through a JPA repository, though the APIs and exact persistence behavior differ.

## 8. Default Ordering

```python
class Meta:
    ordering = ["-date", "-created_at"]
```

The minus sign means descending order.

Transactions are ordered by:

1. Date, newest first.
2. Creation timestamp, newest first when dates match.

This is similar in purpose to:

```sql
ORDER BY date DESC, created_at DESC
```

## 9. The `__str__()` Method

```python
def __str__(self):
    return (
        f"{self.get_type_display()} - "
        f"{self.amount} ({self.category})"
    )
```

This provides a human-readable representation of a transaction, useful in Django Admin and debugging.

For example:

`Expense - 250.00 (Food)`

**Java comparison:** Similar in purpose to overriding `toString()`.

## 10. Quick Revision

Before moving on, make sure you can explain these questions without reading the notes:

1. What does inheriting from `models.Model` provide?
2. What is the purpose of `ForeignKey`?
3. What is the difference between `null=True` and `blank=True`?
4. What does `form.is_valid()` do?
5. What is the difference between `form.save()` and `form.save(commit=False)`?
6. Why does the application assign `request.user` before saving?
7. What does `transaction.save()` do?
8. What does the minus sign in Django's default ordering mean?

## 11. Practical Lesson

A good backend implementation should validate input, assign required relationships, and persist data in a controlled way.

For Hisab-Kitab, transaction ownership is particularly important because financial records must remain separated between users.

**Revision principle:** Understand what each operation does, why it is needed, and what would happen if it were removed or moved.