# 📝 Django ToDo App

A clean and user-focused **ToDo web application** built with **Django**.  
The app includes user authentication and allows each user to manage their own personal tasks through a simple, modern interface.

---

## ✨ Features

- User authentication (Signup / Login / Logout)
- Create, edit, and delete tasks
- Tasks are private to each authenticated user
- Clean and responsive UI using HTML & CSS
- Django admin panel for management

---

## 🧰 Tech Stack

- **Python** 3.10+
- **Django** (latest stable)
- **SQLite** (development database)
- **HTML & CSS** (Django Templates)
- Minimal JavaScript

---

## ⚡ Installation & Setup

```bash
# 1. Clone the repository
git clone https://github.com/Akki-06/django-todo-app.git
cd django-todo-app

# 2. Create and activate a virtual environment
python -m venv venv

# PowerShell
venv\Scripts\Activate.ps1

# Command Prompt
venv\Scripts\activate

# 3. Install dependencies
pip install django

# 4. Apply database migrations
python manage.py migrate

# 5. (Optional) Create admin user
python manage.py createsuperuser

# 6. Run the development server
python manage.py runserver

# 7. Open the app in your browser

===Signup: http://127.0.0.1:8000/
===Login: http://127.0.0.1:8000/login/
===ToDo Dashboard: http://127.0.0.1:8000/todo/
===Admin Panel: http://127.0.0.1:8000/admin/
```
## 🧭 Usage

1.Register a new account using the signup page.
2.Log in with your credentials.
3.Add tasks from the dashboard.
4.Edit or delete tasks as needed.
5.Each user can only see and manage their own tasks.

📸 Screenshot

<img width="1224" height="855" alt="Screenshot 2026-01-01 221226" src="https://github.com/user-attachments/assets/6368c939-0fc2-41b5-87ea-8e7355756dc6" />

<img width="1203" height="862" alt="Screenshot 2026-01-01 221236" src="https://github.com/user-attachments/assets/02b29b70-dd5a-42fc-b946-2f7401c24eee" />

<img width="1314" height="849" alt="Screenshot 2026-01-01 221314" src="https://github.com/user-attachments/assets/8071b87c-fd67-47bc-bc62-7b9b9dc2013a" />

## 🚀 Future Improvements

1.Add requirements.txt for dependency management
2.Implement task completion status (completed / pending)
3.Add pagination and search functionality
4.Improve mobile responsiveness
5.Add password reset and email verification
6.Write automated tests

## 🤝 Contributing
Contributions are welcome.
Please open an issue to discuss changes before submitting a pull request.

## 📄 License
This project is open source.

## 👤 Maintainer
Akhil
GitHub: @Akki-06 : https://github.com/Akki-06


