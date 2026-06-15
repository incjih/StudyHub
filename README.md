# StudyHub 
### Study Group Finder & Collaboration Platform
*Diploma Project — Computer Science*

---

## What is StudyHub?
StudyHub is a web application that allows university students to find study partners, create and join subject-based study groups, schedule sessions, share resources, and rate collaborators.

---

## Tech Stack
- **Backend:** Python 3.12 + Django 4.2
- **Real-time chat:** Django Channels (WebSockets)
- **Database:** SQLite (dev) / PostgreSQL (production)
- **REST API:** Django REST Framework
- **Frontend:** Django Templates + HTML/CSS + JavaScript

---

## Project Structure
```
studyhub/
├── core/               # Main Django project (settings, urls, asgi)
├── users/              # Custom User model, auth, profiles
├── groups/             # StudyGroup, Subject, Membership, Resource models
├── study_sessions/     # StudySession and Review models
├── chat/               # Real-time WebSocket chat (Django Channels)
├── templates/          # HTML templates (to be created)
├── static/             # CSS, JS, images (to be created)
├── manage.py
└── requirements.txt
```

---

## Setup Instructions

### 1. Clone & install dependencies
```bash
git clone <your-repo>
cd studyhub
pip install -r requirements.txt
```

### 2. Run migrations
```bash
python manage.py migrate
```

### 3. Create superuser (admin)
```bash
python manage.py createsuperuser
```

### 4. Start the development server
```bash
python manage.py runserver
```

Then open http://127.0.0.1:8000 in your browser.

---

## Data Models

| Model | Description |
|---|---|
| User | Extended Django user with university, bio, study style, rating |
| Subject | Academic subject (Math, CS, Physics…) |
| StudyGroup | A group with members, subject, description, tags |
| Membership | Links users to groups with roles (member/admin) |
| Resource | Files uploaded to a group |
| StudySession | Scheduled meeting with time, location, attendees |
| Review | Rating + comment left after a session |
| Message | Chat message in a group (stored via WebSocket) |

