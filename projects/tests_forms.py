from django.test import TestCase
from .forms import StartProjectForm


class TestProjectForm(TestCase):
    def test_project_title_is_required(self):
        form = StartProjectForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_project_category_is_required(self):
        form = StartProjectForm({'category': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('category', form.errors.keys())
        self.assertEqual(form.errors['category'][0], 'This field is required.')

    def test_project_description_is_required(self):
        form = StartProjectForm({'description': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors.keys())
        self.assertEqual(form.errors['description'][0], 'This field is required.')

    def test_project_backers_story1_is_required(self):
        form = StartProjectForm({'backers_story_option1': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('backers_story_option1', form.errors.keys())
        self.assertEqual(form.errors['backers_story_option1'][0], 'This field is required.')

    def test_project_backers_story2_is_required(self):
        form = StartProjectForm({'backers_story_option2': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('backers_story_option2', form.errors.keys())
        self.assertEqual(form.errors['backers_story_option2'][0], 'This field is required.')

    def test_project_backers_story3_is_required(self):
        form = StartProjectForm({'backers_story_option3': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('backers_story_option3', form.errors.keys())
        self.assertEqual(form.errors['backers_story_option3'][0], 'This field is required.')

    def test_project_goal_is_required(self):
        form = StartProjectForm({'goal': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('goal', form.errors.keys())
        self.assertEqual(form.errors['goal'][0], 'This field is required.')

    def test_project_end_date_is_required(self):
        form = StartProjectForm({'end_date': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('end_date', form.errors.keys())
        self.assertEqual(form.errors['end_date'][0], 'This field is required.')
