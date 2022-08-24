import json
import os
import unittest

from flask_sqlalchemy import SQLAlchemy

from backend.flaskr import create_app
from backend.models import setup_db


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = os.getenv('DATABASE_NAME') or "trivia"
        self.database_user = os.getenv('DATABASE_USER') or 'postgres'
        self.database_password = os.getenv('DATABASE_PASSWORD') or 'postgres'
        self.database_path = f'postgresql://{self.database_user}:{self.database_password}@localhost:5432/{self.database_name}'
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

            self.new_question = {
                'question': 'test question',
                'answer': 'test answer',
                'category': 1,
                'difficulty': 1,
            }
            self.quiz = {'previous_questions': [], 'quiz_category': {'id': '1', 'type': 'Science'}}

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_should_get_categories_and_respond_with_200(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['categories'])
        self.assertTrue(len(data['categories']))

    def test_should_get_questions_by_valid_category_id_and_respond_200(self):
        res = self.client().get('categories/5/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertIsNotNone(data['categories'])

    def test_should_not_get_questions_by_invalid_category_id_and_respond_404(self):
        res = self.client().get('categories/-1/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_should_add_question_and_respond_200(self):
        res = self.client().post('/questions', json=self.new_question)

        self.assertTrue(res.status_code, 200)
        data = json.loads(res.data)
        self.assertTrue(data['success'])
        self.assertIsNotNone(data['result'])

    def test_should_delete_question_by_id_and_respond_200(self):
        res = self.client().delete('/questions/2')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_should_not_delete_with_invalid_question_id(self):
        res = self.client().delete('/questions/25')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)

    def test_should_search__match_question_and_respond_200(self):
        res = self.client().post('/questions', json={'searchTerm': 'title'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertIsNotNone(data['result'])

    def test_should_get_quiz_and_respond_200(self):
        res = self.client().post('/quizzes', json=self.quiz)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertIsNotNone(data['question'])
        self.assertEqual(data['question']['category'], 1)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
