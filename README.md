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
   git clone 'repo_url'

2. Navigate to the project folder:
   cd quiz_app

3. Create a virtual environment:
   python -m venv venv

4. Activate the virtual environment:
     .\venv\Scripts\activate

5. Install Django:
   pip install django

6. Navigate to the `quiz_project` folder:
   cd quiz_project

7. Set up the database:
   python manage.py makemigrations
   python manage.py migrate

8. Add quiz questions:
   - Open the Django shell:
     python manage.py shell
   - Execute the following commands to add questions:
     from quiz_app.models import Question
     
     Question.objects.bulk_create([
         Question(text="What is the capital of France?", option_a="Paris", option_b="London", option_c="Berlin", option_d="Madrid", correct_option="A"),
         # Add more questions here
     ])

9. Run the project:
   python manage.py runserver

---

## UI Screenshots
![image](https://github.com/user-attachments/assets/e34c42b1-0b75-4995-bb99-a480df2fc9ab)
![image](https://github.com/user-attachments/assets/1e171fda-2d88-4a6a-8e54-850ba6a28a77)


