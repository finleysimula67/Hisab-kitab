# Hisab-Kitab

**A personal finance tracker built with Django and Python.**

Hisab-Kitab is a web application for managing personal income and expenses. It helps users record transactions, organize spending by category, and review their monthly financial activity through a simple dashboard.

## Features

- **User Authentication** — Sign up, log in, and log out securely.
- **Transaction Management** — Create, view, edit, and delete transactions.
- **Income and Expenses** — Record and categorize financial transactions.
- **Dashboard** — View monthly income, expenses, and balance.
- **Search and Filtering** — Find transactions by keyword, type, and date range.
- **User Data Isolation** — Keep each user's transactions separate.
- **Form Validation** — Validate transaction data before saving.
- **Automated Testing** — Test authentication and transaction ownership.

## Tech Stack

- **Language:** Python
- **Framework:** Django 5.2
- **Database:** SQLite for local development
- **Frontend:** HTML, CSS, Bootstrap 5
- **Version Control:** Git and GitHub

## Getting Started

### Prerequisites

- Python 3.12 or another Python version supported by Django 5.2
- Git

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/finleysimula67/Hisab-kitab.git
cd Hisab-kitab
```

**2. Create and activate a virtual environment**

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Linux or macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**3. Install dependencies**

```bash
python -m pip install "Django>=5.2,<5.3"
```

**4. Apply database migrations**

```bash
python manage.py migrate
```

**5. Create an administrator account (optional)**

```bash
python manage.py createsuperuser
```

**6. Start the development server**

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

## Running Tests

Run the automated tests:

```bash
python manage.py test transactions
```

Check the project configuration:

```bash
python manage.py check
```

## Project Structure

The project follows Django's standard structure. The `config/` directory contains project configuration, while `transactions/` contains the transaction models, forms, views, templates, static assets, migrations, and tests.

## Security

- Authentication is required to access transaction pages.
- Transaction operations are restricted to the authenticated owner.
- Logout uses a POST request.
- Production deployment requires appropriate secret management, HTTPS, secure cookie settings, and a persistent production database.

## Current Status

Hisab-Kitab is an ongoing personal project. Authentication, transaction management, dashboard summaries, filtering, database migrations, and initial automated tests are implemented.

## Planned Improvements

- Spending charts and financial reports
- Budget planning and spending limits
- CSV transaction export
- Expanded automated test coverage

## License

No license has been specified yet. All rights remain with the copyright holder unless a license is added to the repository.

---

**Hisab-Kitab** — A simple way to track your money.