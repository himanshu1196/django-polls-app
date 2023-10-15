from django.test import TestCase
from django.utils import timezone
from polls.models import Question


# Create your tests here.
class QuestionTestCase(TestCase):
    def setUp(self):
        Question.objects.create(
            question_text="Is this a test question?", pub_date=timezone.now()
        )

    def test_animals_can_speak(self):
        """Question should be returned with the query"""
        # q = Question.objects.get(question_text = "Is this a test question?")
        # self.assertTrue(q is not None)
        return True
