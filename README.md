# HouseKeep — Household Maintenance Management System

A Django full-stack web application designed to help household users organize and manage their household maintenance activities. HouseKeep provides account management, role-based dashboards, and maintenance task tracking using PostgreSQL for data persistence.

## Implemented Features

### Project Development 1 — Account Management
- Account registration with required-field, email-format, unique username/email, and password confirmation validation.
- Secure password hashing using Django authentication.
- Login and logout with session handling and feedback messages.
- Two user roles: **Administrator** and **Household User**.
- Separate role-based dashboards with server-side access restrictions.
- Profile viewing and updating for the currently logged-in user.
- Optional profile photo upload.
- Django Admin for account administration.

### Project Development 2 — Maintenance Task Management
- Create maintenance tasks with task name, description, category, and due date.
- View a list of personally created maintenance tasks.
- View individual task details.
- Update existing maintenance tasks.
- Delete maintenance tasks.
- Mark maintenance tasks as completed.
- Automatically create a Maintenance History record when a task is completed.
- Store completion date and time, including optional completion notes.
- Validate required task information and display error messages.
- Restrict users to viewing and managing their own maintenance tasks.
- Display task summaries and completion rate on the Household User Dashboard.

## User Roles

| Role | Access |
|---|---|
| Administrator | Administrator Dashboard, account statistics, account administration, and own profile |
| Household User | Household Dashboard, profile management, and personal maintenance task management |

## Technologies Used

- Python 3.15.2
- Django 6.1.3
- PostgreSQL / Supabase
- psycopg
- HTML and CSS
- Bootstrap 5
- JavaScript

## Requirements

- Python 3.15.2
- PostgreSQL 15+ or a configured Supabase PostgreSQL database
- Git
- Internet connection for Bootstrap CDN styling

## Windows Setup (PowerShell or CMD)

1. Clone the repository:

   ```bash
   git clone https://github.com/StringMicoh/HouseKeep-Padin-JohnMicoh-G07.git
   cd HouseKeep-Padin-JohnMicoh-G07
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. Install the required dependencies:

   ```bash
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. Configure the database:

   - Create or use a PostgreSQL database.
   - Copy `.env.example` and rename the copy to `.env`.
   - Enter your database credentials and connection details in `.env`.
   - Do not commit `.env` to GitHub.

5. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

7. Open the application:

   `http://127.0.0.1:8000/`

## Main Routes

| Route | Purpose |
|---|---|
| `/accounts/signup/` | Create an account |
| `/accounts/login/` | Sign in |
| `/accounts/logout/` | Sign out |
| `/` | Household User Dashboard |
| `/admin-dashboard/` | Administrator Dashboard |
| `/accounts/profile/` | View and update own profile |
| `/maintenance/` | View personal maintenance tasks |
| `/maintenance/create/` | Create a maintenance task |
| `/maintenance/<id>/` | View task details |
| `/maintenance/<id>/edit/` | Update a maintenance task |
| `/maintenance/<id>/delete/` | Delete a maintenance task |
| `/maintenance/<id>/complete/` | Mark a task as completed |
| `/admin/` | Django Administration |

## Database Models

### CustomUser
Stores user account information, including username, full name, email, password, contact number, profile photo, and role.

### MaintenanceTask
Stores maintenance task information, including:
- Task name
- Description
- Category
- Status
- Due date
- Created and updated timestamps
- User ForeignKey identifying the task owner

### MaintenanceHistory
Stores completed maintenance task records, including:
- Task OneToOne relationship
- User ForeignKey
- Completion date and time
- Optional completion notes

## Business Rules and Validation

- Each registered user must have a unique email address and username.
- Passwords are securely hashed using Django authentication.
- Public registration assigns the Household User role.
- Only authenticated users can access protected pages.
- Users can only view, update, and delete their own maintenance tasks.
- Task name, category, and due date are required.
- Tasks can have Pending, Completed, or Overdue statuses.
- Completing a task automatically creates a corresponding Maintenance History record.
- A task can have only one Maintenance History record.
- Dashboard task statistics are calculated from actual database records.

## Important Implementation Notes

- `AUTH_USER_MODEL` is configured to use `accounts.CustomUser`.
- PostgreSQL credentials are loaded from environment variables using `.env`.
- The project uses Django migrations to manage database changes.
- Task ownership is enforced through user-specific database queries.
- Maintenance History is connected to MaintenanceTask through a OneToOne relationship.
- The administrator dashboard and Household User dashboard have separate access restrictions.
- Bootstrap 5 is loaded through a CDN.

## GitHub Repository and Branching

Repository:  
https://github.com/StringMicoh/HouseKeep-Padin-JohnMicoh-G07

The project follows a feature-branch workflow:

- `main` — stable project version.
- `develop` — integration branch.
- `feature/maintenance-tasks` — Maintenance Task CRUD implementation.
- `feature/task-history` — Task completion and Maintenance History implementation.

Completed feature branches were merged into `develop` through Pull Requests. The completed increment was subsequently merged from `develop` into `main`.

## Security and Configuration

- Keep `.env` and database credentials private.
- Do not commit `.venv/`, `__pycache__/`, or other local environment files.
- Use Django authentication and password hashing.
- Apply server-side role and ownership checks.
- Keep `requirements.txt` updated with project dependencies.

## Future Development

Additional HouseKeep modules planned for future increments include:

- Area Management
- Household Item Management
- Appliance Management
- Schedule Management
- House Reminders
- Expanded Maintenance History features
- Dashboard analytics improvements
