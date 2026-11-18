# HouseKeep — Account Feature (Project Development 1)

A Django full-stack implementation of the HouseKeep account feature. The project follows the structure and Django authentication approach demonstrated in the supplied CampusConnect tutorial, adapted to the HouseKeep Software Design Document.

## Included in this phase

- Registration with required-field, email-format, unique username/email, and password confirmation validation.
- Django password hashing and built-in authentication.
- Login/logout with session handling and feedback messages.
- Two roles: **Administrator** and **Household User**.
- Separate role dashboards; the administrator dashboard is protected server-side (non-admin users receive HTTP 403).
- Login-required dashboard and profile pages.
- Profile view/update for the currently logged-in user, including optional profile photo.
- PostgreSQL configuration through environment variables.
- Django Admin user management.

The household task, area, appliance, schedule, reminder, history, and analytics modules are not implemented in this first account-feature phase; the user dashboard indicates these future modules.

## Requirements

- Python 3.15.2 (this project uses Django 6.1.3 or newer in the 6.1 series)
- PostgreSQL 15+ (required by Django 6.1)

## Windows setup (PowerShell or CMD)

This ZIP is prepared for **Python 3.15.2**. It uses Django 6.1.3+ because Django 5.2 does not support Python 3.15.

1. Extract the ZIP and open a terminal in the `housekeep` project folder (the folder containing `manage.py`).
2. Create and activate a virtual environment:

   ```powershell
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. Install dependencies:

   ```powershell
   python -m pip install --upgrade pip
   pip install -r requirements.txt

   The requirements install Django 6.1.3 or a later 6.1 patch release, which supports Python 3.15.
   ```

4. Create a PostgreSQL database named `housekeep_db` (or choose another name).
5. Copy `.env.example` to `.env`, then enter your local PostgreSQL username, password, host, and database name. Do not commit `.env`.
6. Run migrations:

   ```powershell
   python manage.py makemigrations accounts
   python manage.py migrate
   ```

7. Create the administrator account:

   ```powershell
   python manage.py createsuperuser
   ```

   Then open `/admin/`, sign in, edit that account, and set **Role** to **Administrator**. New public registrations are always assigned the Household User role; users cannot choose or grant themselves administrator access.

8. Start the server:

   ```powershell
   python manage.py runserver
   ```

9. Open `http://127.0.0.1:8000/`.

## Main routes

| Route | Purpose |
|---|---|
| `/accounts/signup/` | Create account |
| `/accounts/login/` | Sign in |
| `/accounts/logout/` | Sign out (POST) |
| `/` | Household User dashboard (login required) |
| `/admin-dashboard/` | Administrator dashboard (admin role required) |
| `/accounts/profile/` | View and update own profile |
| `/admin/` | Django administration |

## Important implementation notes

- `AUTH_USER_MODEL` is configured before the first migration. Do not migrate first and then change the user model.
- Passwords are handled by Django's `UserCreationForm` and authentication system; plain-text passwords are never stored.
- The role field is excluded from public registration. Set administrator roles through Django Admin only.
- Profile updates use `request.user` as the form instance, so a user cannot submit another user's ID to edit someone else's profile.
- The PostgreSQL database is configured in `housekeep/settings.py` and reads credentials from `.env`.
- Bootstrap 5 is loaded from its CDN; an internet connection is needed for Bootstrap styling.

## GitHub checklist

- Create a **Public** repository named according to your instructor's required pattern, for example `HouseKeep-Padin-JohnMicoh-GXX` (replace `GXX` with your actual section).
- Commit progress regularly.
- Keep `.env`, `.venv/`, `venv/`, `__pycache__/`, and local database/media files out of Git.
- Include `requirements.txt`.
- Test the public repository link in an incognito/private browser before submission.
