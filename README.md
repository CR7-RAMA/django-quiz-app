# Django Quiz App

A simple Django-based quiz application where users can:
1. Start a new quiz session.
2. Answer 3 random multiple-choice questions without repetition.
3. View the results, including:
   - Correct answers
   - Incorrect answers
   - Score percentage
4. Restart the quiz after completing it.

---

## Setup Instructions

### Prerequisites
- Python
- Django

### Steps
1. Clone the repository:
   git clone <repository-url>
2. Install Django:
   pip install django
3. Navigate to the `quiz_app` folder:
   cd quiz_app
4. Set up the database:
   python manage.py makemigrations,
   python manage.py migrate
5. Add quiz questions:
   - Open the Django shell:
     python manage.py shell
   - Execute the following commands to add questions:
     from quiz_app.models import Question
     
     Question.objects.bulk_create([
         Question(text="What is the capital of France?", option_a="Paris", option_b="London", option_c="Berlin", option_d="Madrid", correct_option="A"),
         # Add more questions here
     ])
6. Run the project:
   python manage.py runserver

---
