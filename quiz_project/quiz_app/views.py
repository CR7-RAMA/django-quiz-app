from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Question, QuizSession
import random

def start_quiz(request):
    # Clear old session data
    request.session.pop('quiz_session_id', None)
    request.session.pop('answered_questions', None)
    request.session.pop('current_question_id', None)

    # Start a new quiz session
    session = QuizSession.objects.create()
    request.session['quiz_session_id'] = session.id
    return redirect('quiz_app:question')



def get_question(request):
    session_id = request.session.get('quiz_session_id')
    session = QuizSession.objects.get(id=session_id)

    if session.completed:
        return redirect('quiz_app:results')

    answered_questions = request.session.get('answered_questions', [])
    remaining_questions = Question.objects.exclude(id__in=answered_questions)

    if remaining_questions.exists():
        question = random.choice(remaining_questions)
        request.session['current_question_id'] = question.id
        return render(request, 'quiz_app/question.html', {'question': question})
    else:
        session.completed = True
        session.save()
        return redirect('quiz_app:results')


def submit_answer(request):
    session_id = request.session.get('quiz_session_id')
    session = QuizSession.objects.get(id=session_id)

    question_id = request.session.get('current_question_id')
    question = Question.objects.get(id=question_id)

    user_answer = request.POST.get('answer')
    answered_questions = request.session.get('answered_questions', [])
    answered_questions.append(question_id)
    request.session['answered_questions'] = answered_questions

    if user_answer == question.correct_option:
        session.correct_count += 1
    else:
        session.incorrect_count += 1
    session.save()

    if len(answered_questions) == 3:  # Stop after 3 questions
        session.completed = True
        session.save()
        return redirect('quiz_app:results')
    
    return redirect('quiz_app:question')


def quiz_results(request):
    session_id = request.session.get('quiz_session_id')
    session = QuizSession.objects.get(id=session_id)

    total_questions = session.correct_count + session.incorrect_count
    score_percentage = (session.correct_count / total_questions) * 100 if total_questions > 0 else 0

    context = {
        'correct_count': session.correct_count,
        'incorrect_count': session.incorrect_count,
        'score_percentage': score_percentage
    }

    return render(request, 'quiz_app/results.html', context)
