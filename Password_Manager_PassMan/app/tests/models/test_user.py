from ..test_base import TestBase
from ...models.user import User


class TestUser(TestBase):
    def test_create(self, client):
        with self.app.app_context():
            # Create a user
            username, password = 'Jane', 'Jane123'
            User.create(username, password)

            # Fetch the user object we created
            user = User.find_by_username_password(username, password)
            self.assertIsNotNone(user)
            self.assertEqual(user.username, username)

    def test_create_duplicate_username(self, client):
        with self.app.app_context():
            # Create a user
            username, password = 'Jane', 'Jane123'
            User.create(username, password)

            # Check that creating a user with the same username fails.
            try:
                User.create(username, password)
            except RuntimeError as ex:
                self.assertEqual(str(ex), f'Username {username} is already taken')

            # Check that creating a user with the same username fails,
            # even if the case is different (i.e. username is case-insensitive).
            username = username.swapcase()
            try:
                User.create(username, password)
            except RuntimeError as ex:
                self.assertEqual(str(ex), f'Username {username} is already taken')

    def test_find_by_username_password(self, client):
        with self.app.app_context():
            # Create a user
            username, password = 'Jane', 'Jane123'
            User.create(username, password)

            # Find the user by username/password
            user = User.find_by_username_password(username, password)
            self.assertIsNotNone(user)
            self.assertEqual(user.username, username)

            # Find the user by username/password; verify that username is case-insensitive
            user = User.find_by_username_password(username.swapcase(), password)
            self.assertIsNotNone(user)
            self.assertEqual(user.username, username)

    def test_find_by_id(self, client):
        with self.app.app_context():
            # Create a user
            username, password = 'Jane', 'Jane123'
            User.create(username, password)

            # Fetch the user object we created
            user = User.find_by_username_password(username, password)
            self.assertIsNotNone(user)

            # Find the user by id
            user = User.find_by_id(user.id)
            self.assertIsNotNone(user)
            self.assertEqual(user.username, username)
