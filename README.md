# Blog Project

## Overview
This is a **Django-based blog project** built collaboratively by **Rabin Shrestha, and Sarad Thapa**. The project allows users to read, create, and manage blog posts with features like tagging, search, likes, and views tracking.

## Features
- User authentication (Signup/Login/Logout)
- Create, read, update, and delete (CRUD) blog posts
- Tagging system for categorizing posts
- Post like feature
- View count tracking for popular posts
- Homepage with featured and recent blogs
- Search functionality
- Responsive UI with **Tailwind CSS**

## Tech Stack
- **Backend**: Django (Python)
- **Frontend**: Tailwind CSS, HTML, JavaScript
- **Database**: SQLite (default), can be switched to PostgreSQL
- **Version Control**: Git & GitHub

## Installation & Setup
### 1. Clone the repository
```bash
$ git clone https://github.com/saradjung/BlogSite.git
$ cd blog-project
```

### 2. Create a virtual environment
```bash
$ python -m venv venv
$ source venv/bin/activate   # On Windows use: venv\Scripts\activate
```

### 3. Install dependencies
```bash
$ pip install -r requirements.txt
```

### 4. Apply migrations
```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

### 5. Create a superuser (optional, for admin access)
```bash
$ python manage.py createsuperuser
```

### 6. Run the development server
```bash
$ python manage.py runserver
```
Visit `http://127.0.0.1:8000/` in your browser.

## Usage
- Register/Login to access full features.
- Explore and read blog posts.
- Like posts and track trending articles.
- Search posts by keywords.
- Create and manage your own blog posts.

## Folder Structure
```
blog-project/
│── blog/               # Main app containing models, views, templates
│── static/             # Static files (CSS, JavaScript, images)
│── templates/          # HTML templates
│── media/              # Uploaded images
│── db.sqlite3          # Database file (if using SQLite)
│── manage.py           # Django management script
│── requirements.txt    # Python dependencies
│── README.md           # Project documentation
```

## Contributors
- **Sarad Thapa**
- **Rabin Shrestha**

## Future Enhancements
- Dark mode UI
- Social media sharing integration

## License
This project is open-source and available under the **MIT License**.