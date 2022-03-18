from django.test import TestCase


from django.urls import reverse
import datetime
from django.utils import timezone
from .models import Question

class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        time=timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
    def test_was_published_recently_with_old_question(self):
        time= timezone.now() - datetime.timedelta(days=1, seconds=1)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
    def test_was_published_recently_with_new_question(self):
        time= timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), True)

def create_question(text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=text, pub_date = time)
class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No polls availble')
        self.assertQuerysetEqual(response.context['latest_question_list'],[])
    def test_future_question(self):
        create_question('my_question', days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code,200)
        self.assertQuerysetEqual(response.context['latest_question_list'],[])
    def test_past_question(self):
        question = create_question('my_text',-30)
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code,200)
        self.assertQuerysetEqual(response.context['latest_question_list'],[question])
    def future_and_past_question(self):
        question = create_question('my_text2', days=-30)
        create_question('my_text1', days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertEquals(response.status_code, 200)
        self.assertQuerysetEqual(response.context['latest_question_list'],[question])
    def test_two_past_questions(self):
        question1 = create_question(text="Past question 1.", days=-30)
        question2 = create_question(text="Past question 2.", days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'],[question2, question1])

class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        future_question = create_question(text='Future question.', days=5)
        response = self.client.get(reverse('polls:detail', args=(future_question.id,)))
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        past_question = create_question(text='Past Question.', days=-5)
        response = self.client.get(reverse('polls:detail', args=(past_question.id,)))
        self.assertContains(response, past_question.question_text)
