from ..test_base import TestBase


class TestLogin(TestBase):
    def setUp(self, client):
        super().setUp(client)  # setup base
        self.seed_db()  # seed the database

    def test_login_renders(self, client):
        res = client.get(
            '/sessions/new'
        )
        res_data = res.get_data(as_text=True)
        self.assertIn('Log in to continue', res_data)

    def test_login_empty_username(self, client):
        res = client.post(
            '/sessions/create', data={'username': '', 'password': 'John123'}
        )
        res_data = res.get_data(as_text=True)
        self.assertIn('Please enter a username', res_data)

    def test_login_empty_password(self, client):
        res = client.post(
            '/sessions/create', data={'username': 'John', 'password': ''}
        )
        res_data = res.get_data(as_text=True)
        self.assertIn('Please enter a password', res_data)

    def test_login_wrong_username(self, client):
        res = client.post(
            '/sessions/create', data={'username': 'William', 'password': 'John123'}
        )
        res_data = res.get_data(as_text=True)
        self.assertIn('Invalid username or password', res_data)

    def test_login_wrong_password(self, client):
        res = client.post(
            '/sessions/create', data={'username': 'John', 'password': 'John1234'}
        )
        res_data = res.get_data(as_text=True)
        self.assertIn('Invalid username or password', res_data)

    def test_login_success(self, client):
        res = client.post(
            '/sessions/create', data={'username': 'John', 'password': 'John123'}
        )
        res_data = res.get_data(as_text=True)
        self.assertIn(
            'You should be redirected automatically to target URL: <a href="/vaults">/vaults</a>.',
            res_data,
        )

    def test_login_case_insensitive_username(self, client):
        res = client.post(
            '/sessions/create', data={'username': 'jOHN', 'password': 'John123'}
        )
        res_data = res.get_data(as_text=True)
        self.assertIn(
            'You should be redirected automatically to target URL: <a href="/vaults">/vaults</a>.',
            res_data,
        )
