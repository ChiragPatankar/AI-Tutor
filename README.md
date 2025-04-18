# AI Tutor 📚🤖

AI Tutor is an intelligent learning web application designed to help students access personalized educational resources including videos, PDFs, and website links. It allows students to select their stream and subject, then recommends content accordingly. Over time, it adapts to the user's preferred learning style and unlocks advanced features as they progress.

---

## 1. What the Project Actually Does

AI Tutor provides:
- 🎯 Personalized learning material recommendations (videos, PDFs, links).
- 👨‍🎓 Stream and subject-based content curation.
- 📊 Adaptive learning system that evolves with student engagement.
- 🔓 Unlockable Pro Mode features based on learning progress.

---

## 2. How the Components Work

The project consists of the following core components:

- **Frontend**: User interface built with HTML, CSS, JavaScript.
- **Backend (Flask)**: Manages routes, sessions, logic, and data processing.
- **Database (SQLite)**: Stores user credentials, progress, and content info.
- **Recommendation Logic**: Suggests materials based on stream and history.
- **Pro Mode Logic**: Unlocks advanced tools once 50% content is consumed.

---

## 3. Implementation Details of Each Module

- **User Module**: User registration, login, session management using Flask-Login.
- **Content Module**: Maintains the pool of video/PDF/link content tied to streams.
- **Dashboard Module**: Displays user-specific learning data and suggestions.
- **Adaptive Engine (Planned)**: Will track learning habits and recommend content accordingly.
- **Progress Tracker**: Measures how much content a student has completed.

---

## 4. API Endpoints and Their Functionality

| Endpoint       | Method | Description                                 |
|----------------|--------|---------------------------------------------|
| `/`            | GET    | Home page                                   |
| `/login`       | POST   | User login                                  |
| `/signup`      | POST   | Register new user                           |
| `/dashboard`   | GET    | Main dashboard with recommended resources   |
| `/logout`      | GET    | Logs out current user                       |
| `/progress`    | GET/POST | [Planned] Handle learning progress        |
| `/recommend`   | GET    | [Planned] Fetch AI-based recommendations    |

---

## 5. Authentication Mechanisms

AI Tutor uses `Flask-Login` for secure user authentication. It includes:
- Password hashing via `werkzeug.security`.
- Session-based login management.
- Login-required access protection for dashboard and other sensitive routes.

---

## 6. Dependencies Used

```txt
Flask               # Web framework
Flask-Login         # Authentication and session management
Jinja2              # HTML templating
SQLite              # Lightweight database
Werkzeug            # Secure password utilities
python-dotenv       # Environment variable management
```

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

## 📦 Installation

1. **Clone the repo:**

```bash
git clone https://github.com/ChiragPatankar/tutor_new.git
cd tutor_new
```

2. **Create a virtual environment:**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Run the app:**

```bash
python app.py
```

5. **Open in browser:**
```
http://localhost:5000
```

---

## 📸 Screenshots

> (Add relevant screenshots here)

---

## 🛠 Roadmap

- [x] Basic content recommendation
- [x] User login/signup system
- [ ] Adaptive ML-based recommendation engine
- [ ] Teacher/Admin panel
- [ ] Mobile-friendly UI
- [ ] Analytics dashboard

---

## 🙋‍♂️ Author

**Chirag Patankar**  
📧 chiragpatankar23@gmail.com  
🌐 [LinkedIn](https://linkedin.com/in/chiragpatankar)  
🌐 [Portfolio](https://thewebnect.in)

---

## ⭐ Contributing

Contributions are welcome! Fork the repo, make your changes, and submit a PR.  
Don't forget to star the repo if you like the project ⭐

---

## 📄 License

MIT License. Feel free to use, modify, and distribute this project.
```
