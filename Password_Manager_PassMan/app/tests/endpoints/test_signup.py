from ..test_base import TestBase
from ...models.user import User


class TestSignup(TestBase):
    def test_signup_renders(self, client):
        res = client.get(
            '/registrations/new'
        )
        res_data = res.get_data(as_text=True)
        self.assertIn('Create your account', res_data)

    def test_signup_empty_username(self, client):
        res = client.post(
            '/registrations/create', data={'username': '', 'password': '', 'retype_password': ''}
        )
        res_data = res.get_data(as_text=True)
        self.assertIn('Please enter a username', res_data)

    def test_signup_empty_password(self, client):
        res = client.post(
            '/registrations/create', data={'username': 'John', 'password': '', 'retype_password': ''}
        )
        res_data = res.get_data(as_text=True)
        self.assertIn('Please enter a password', res_data)

    def test_signup_password_missing_capital_letter(self, client):
        res = client.post(
            '/registrations/create',
            data={'username': 'John', 'password': 'john', 'retype_password': ''},
        )
        res_data = res.get_data(as_text=True)
        self.assertIn('Password must include a capital letter', res_data)

    def test_signup_password_missing_small_letter(self, client):
        res = client.post(
            '/registrations/create',
            data={'username': 'John', 'password': 'JOHN', 'retype_password': ''},
        )
        res_data = res.get_data(as_text=True)
        self.assertIn('Password must include a small letter', res_data)

    def test_signup_password_missing_digit(self, client):
        res = client.post(
            '/registrations/create',
            data={'username': 'John', 'password': 'John', 'retype_password': ''},
        )
        res_data = res.get_data(as_text=True)
        self.assertIn('Password must include a digit', res_data)

    def test_signup_password_too_short(self, client):
        res = client.post(
            '/registrations/create',
            data={'username': 'John', 'password': 'John1', 'retype_password': ''},
        )
        res_data = res.get_data(as_text=True)
        self.assertIn('Password must be at least 6 characters long', res_data)

    def test_signup_password_too_long(self, client):
        password = "A" * 10 + "a" * 10 + "1" * 6
        res = client.post(
            '/registrations/create',
            data={'username': 'John', 'password': password, 'retype_password': ''},
        )
        res_data = res.get_data(as_text=True)
        self.assertIn('Password must be at most 25 characters long', res_data)

    def test_signup_empty_retype_password(self, client):
        res = client.post(
            '/registrations/create',
            data={'username': 'John', 'password': 'John123', 'retype_password': ''},
        )
        res_data = res.get_data(as_text=True)
        self.assertIn('Please retype your password', res_data)

    def test_signup_mismatched_retype_password(self, client):
        res = client.post(
            '/registrations/create',
            data={
                'username': 'John',
                'password': 'John123',
                'retype_password': 'John12',
            },
        )
        res_data = res.get_data(as_text=True)
        self.assertIn('Passwords must match', res_data)

    def test_signup_success(self, client):
        res = client.post(
            '/registrations/create',
            data={
                'username': 'Jane',
                'password': 'Jane123',
                'retype_password': 'Jane123',
            },
        )
        res_data = res.get_data(as_text=True)
        self.assertIn('Account created!', res_data)

        # Make sure the account is in the database
        user = User.find_by_username_password('Jane', 'Jane123')
        self.assertIsNotNone(user)

    def test_signup_taken_username(self, client):
        # Create a user first
        self.test_signup_success(client)

        # Now try to create another user with the same username
        res = client.post(
            '/registrations/create',
            data={
                'username': 'Jane',
                'password': 'Jane123',
                'retype_password': 'Jane123',
            },
        )
        res_data = res.get_data(as_text=True)
        self.assertIn('Username Jane is already taken', res_data)
