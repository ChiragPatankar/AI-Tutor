# AI Tutor 📚🤖

1. What the Project Actually Does
AI Tutor is an intelligent learning web application designed to help students access personalized educational resources including videos, PDFs, and website links. It allows students to select their stream and subject, then recommends content accordingly. Over time, it adapts to the user's preferred learning style and unlocks advanced features as they progress.

# 2. How the Components Work

The project consists of several core components:
•	**Frontend**: Provides the user interface for students to interact with the platform.
•	**Backend (Flask)**: Handles business logic, data management, and routes.
•	**Database (SQLite)**: Stores user data, content metadata, and user progress.
•	**Recommendation Logic**: Suggests personalized learning materials based on selected subjects and engagement history.
•	**Pro Mode Logic**: Unlocks additional features after 50% completion of course.

# 3. Implementation Details of Each Module

Below is a brief overview of how each module is implemented:
• **User Module**: Handles user signup, login, session management using Flask-Login.
• **Content Module**: Manages educational resources (video, PDF, and link-based) linked to streams and subjects.
• **Dashboard Module**: Displays user progress and available learning materials.
• **Adaptive Engine (Planned)**: Will use usage patterns to suggest more personalized content dynamically.
• **Progress Tracker**: Monitors how much content a student has consumed and unlocks features accordingly.

# 4. API Endpoints and Their Functionality

The Flask backend contains the following endpoints:
• `/` – Home page of the platform.
• `/login` – Handles user login.
• `/signup` – Handles new user registration.
• `/dashboard` – Displays the student dashboard with personalized content.
• `/logout` – Logs out the user and ends the session.
• `/progress` – (Planned) Updates and retrieves user progress.
• `/recommend` – (Planned) Fetches content recommendations based on learning patterns.

# 5. Authentication Mechanisms

Authentication is implemented using the Flask-Login extension. It includes secure password hashing, user session management, and access control to ensure only authenticated users can access restricted routes like the dashboard.

# 6. Dependencies Used
s
Below are the major dependencies used in this project:
• Flask – Web framework
• Flask-Login – User authentication and session management
• SQLite – Lightweight relational database
• Jinja2 – Templating engine for rendering HTML with dynamic data
• Werkzeug – Password hashing utilities
• Python-dotenv – For managing environment variables
