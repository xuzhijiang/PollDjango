from django.test import TestCase
from .models import Question
from django.utils import timezone
import datetime
from django.urls import reverse


def create_question(question_text, days):
    """
    :param question_text: Questionnaire content
    :param days: Current time offset days,
    negative values mean that publish date is in the past,
    otherwise is in the future.
    :return: a instance of Question
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionMethodTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        在未来发布的问卷应该返回False
        :return:
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        日期超过1天的将返回False
        :return:
        """
        time = timezone.now() - datetime.timedelta(days=30)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        最近一天内的将返回True。这里创建了一个1小时内发布的实例
        :return:
        """
        time = timezone.now() - datetime.timedelta(hours=1)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)


class QuestionViewTests(TestCase):

    def test_index_view_with_no_question(self):
        """
        If the questionnaire doesn't exist, give a corresponding prompt
        :return:
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_index_view_with_a_past_question(self):
        create_question(question_text='Past question.', days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
        response.context['latest_question_list'],
        ['<Question: Past question.>']
        )

    def test_index_view_with_a_future_question(self):
        create_question(question_text='Future question.', days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(
        response.context['latest_question_list'],
        []
        )

    def test_index_view_with_future_question_and_past_question(self):
        create_question(question_text='Past question.', days=-30)
        create_question(question_text='Future question.', days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
        response.context['latest_question_list'],
        ['<Question: Past question.>']
        )

    def test_index_view_with_two_past_question(self):
        create_question(question_text='Past question1.', days=-30)
        create_question(question_text='Past question2.', days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
        response.context['latest_question_list'],
        ['<Question: Past question2.>', '<Question: Past question1.>']
        )


class QuestionIndexDetailTests(TestCase):

    def test_detail_view_with_a_future_question(self):
        future_question = create_question(question_text="Future question", days=5)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_detail_view_with_a_past_question(self):
        past_question = create_question(question_text='Past question', days=-5)
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)
