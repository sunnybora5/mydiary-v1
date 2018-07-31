import unittest
from app.request import validate, ValidationException


class EmailRuleTestCase(unittest.TestCase):

    def test_passes_if_field_is_a_valid_email(self):
        """
        Passes if the field is valid.
        :return:
        """
        request = {'test_field': 'mutaimwiti@code.com'}
        rules = {'test_field': 'required|email'}
        self.assertEqual(request, validate(request, rules))

    def test_fails_if_field_is_not_a_valid_email(self):
        """
        Fails if field length is greater than that specified by argument.
        """
        request = {'test_field': 'fake.com'}
        rules = {'test_field': 'required|email'}
        with self.assertRaises(ValidationException) as context:
            validate(request, rules)
        self.assertTrue(
            'The test_field field [fake.com] is not a valid email address.' in str(context.exception.errors)
        )
