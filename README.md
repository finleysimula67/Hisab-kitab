# Hisab-Kitab

**A personal finance tracker built with Django and Python.**

Hisab-Kitab is a web application for managing personal income and expenses. It helps users record transactions, organize spending by category, and review their monthly financial activity through a simple dashboard.

## Features

- **User Authentication** — Sign up, log in, and log out.
- **Transaction Management** — Create, view, edit, and delete transactions.
- **Income and Expenses** — Record and categorize financial transactions.
- **Dashboard** — View monthly income, expenses, and balance.
- **Search and Filtering** — Find transactions by keyword, type, and date range.
- **User Data Isolation** — Restrict access to each user's transactions.
- **Form Validation** — Validate transaction data before saving.
- **Automated Testing** — Test authentication and transaction ownership.
- **Continuous Integration** — Run automated checks and tests with GitHub Actions.

## Tech Stack

- **Language:** Python
- **Web Framework:** Django 5.2
- **Database:** SQLite for local development
- **Frontend:** HTML, CSS, Bootstrap 5
- **Dependency Management:** uv
- **Static File Serving:** WhiteNoise
- **Application Server:** Gunicorn
- **Version Control:** Git and GitHub

## Getting Started

### Prerequisites

- Git
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

### Installation

**1. Clone the repository**

```powershell
git clone https://github.com/finleysimula67/Hisab-kitab.git
cd Hisab-kitab
```

**2. Install dependencies**

```powershell
uv sync --locked
```

This command creates and synchronizes the project's virtual environment using `pyproject.toml` and `uv.lock`.

**3. Apply database migrations**

```powershell
uv run --locked python manage.py migrate
```

**4. Create an administrator account (optional)**

```powershell
uv run --locked python manage.py createsuperuser
```

**5. Start the development server**

```powershell
uv run --locked python manage.py runserver
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## Running Tests

Run the automated tests:

```powershell
uv run --locked python manage.py test transactions
```

## Project Checks

Check the Django configuration:

```powershell
uv run --locked python manage.py check
```

Verify that no new database migrations are required:

```powershell
uv run --locked python manage.py makemigrations --check --dry-run
```

Check dependency lockfile consistency:

```powershell
uv lock --check
```

## Project Structure

The project follows Django's standard structure. The `config/` directory contains project configuration and settings, while `transactions/` contains the transaction models, forms, views, templates, static assets, migrations, and tests.

Project dependencies are declared in `pyproject.toml`, with resolved versions recorded in `uv.lock`.

## Security

- Authentication is required to access transaction pages.
- Transaction operations are restricted to the authenticated owner.
- Logout uses a POST request.
- Production deployments require appropriate secret management, HTTPS, secure cookie settings, persistent database storage, and backups.

## Current Status

Hisab-Kitab is an ongoing personal project. Authentication, transaction management, dashboard summaries, filtering, database migrations, and automated tests are implemented.

GitHub Actions runs automated checks and tests on configured branches and pull requests.

## Planned Improvements

- Spending charts and financial reports
- Budget planning and spending limits
- CSV transaction export
- Improved financial summaries and reporting

## License

This project is licensed under the [MIT License](LICENSE).

---

**Hisab-Kitab** — A simple way to track your money.