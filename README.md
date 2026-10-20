# Hisab-Kitab

**A personal finance and expense tracker built with Python and Django.**

Hisab-Kitab helps users manage personal income and expenses, organize transactions by category, and review monthly financial activity through a simple dashboard.

**Live Demo:** [Hisab-Kitab](https://hisab-kitab-4i2p.onrender.com/)

> **Demo note:** This project is an ongoing personal project. The live demo uses SQLite on Render, whose free filesystem is not persistent. Do not use it to store real financial records.

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
- **Database:** SQLite
- **Frontend:** HTML, CSS, and Bootstrap 5
- **Dependency Management:** uv
- **Static File Serving:** WhiteNoise
- **Application Server:** Gunicorn
- **Deployment:** Render
- **Version Control:** Git and GitHub
- **CI:** GitHub Actions

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

This creates and synchronizes the project's virtual environment using `pyproject.toml` and `uv.lock`.

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

```powershell
uv run --locked python manage.py test transactions
```

## Project Checks

Check the Django configuration:

```powershell
uv run --locked python manage.py check
```

Check for missing migrations:

```powershell
uv run --locked python manage.py makemigrations --check --dry-run
```

Verify dependency lockfile consistency:

```powershell
uv lock --check
```

## Project Structure

The project follows Django's standard structure:

- `config/` — Project configuration, settings, and URL routing.
- `transactions/` — Transaction models, forms, views, templates, static assets, migrations, and tests.
- `pyproject.toml` — Project metadata and dependencies.
- `uv.lock` — Resolved dependency versions.
- `build.sh` — Production build and static-file collection.
- `render.yaml` — Render deployment configuration.

## Security

- Authentication is required to access transaction pages.
- Transaction operations are restricted to the authenticated owner.
- Logout uses a POST request.
- Production deployments use environment-based secret management and HTTPS settings.
- Persistent database storage and backups are important before using the application for real financial records.

## Current Status

Hisab-Kitab is an ongoing personal project. Authentication, transaction management, dashboard summaries, filtering, database migrations, and automated tests are implemented.

Email verification and persistent production database storage remain areas for improvement.

## Planned Improvements

- Spending charts and financial reports
- Budget planning and spending limits
- CSV transaction export
- Improved financial summaries and reporting
- Email verification
- Persistent PostgreSQL storage

## License

This project is licensed under the [MIT License](LICENSE).

---

**Hisab-Kitab** — A simple way to track your money.
