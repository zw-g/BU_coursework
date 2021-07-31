from ..test_base import TestBase


class TestAuthenticationCheck(TestBase):
    def setUp(self, client):
        super().setUp(client)  # setup base
        self.seed_db()  # seed the database

    def test_vaults(self, client):
        res = client.get('/vaults')
        self.assertStatus(res, 302)

    def test_items(self, client):
        res = client.get('/vaults/1/items')
        self.assertStatus(res, 302)

    def test_item(self, client):
        res = client.get('/vaults/1/items/1')
        self.assertStatus(res, 302)
