from dataclasses import dataclass
from datetime import datetime
from ..helpers import application_helper
from ..db import get_db


@dataclass
class VaultItem:
    id: int
    title: str
    website: str
    username: str
    password: str
    created_on: datetime
    updated_on: datetime

    @staticmethod
    def make_empty():
        return VaultItem(
            id=0,
            title='',
            website='',
            username='',
            password='',
            created_on=None,
            updated_on=None,
        )

    @staticmethod
    def _from_row(row, encryption_key: bytes):
        data = application_helper.decrypt(row['data'], encryption_key)
        return VaultItem(
            row['id'],
            data['title'],
            data['website'],
            data['username'],
            data['password'],
            row['created_on'],
            row['updated_on'],
        )

    @staticmethod
    def find_by_vault(user_id, vault_id, encryption_key: bytes):
        query = (
            'SELECT id, data, created_on, updated_on '
            'FROM vault_item '
            'WHERE vault_id = :vault_id '
            'AND :user_id = (SELECT user_id from vault where id = :vault_id LIMIT 1) '
            'ORDER BY created_on ASC '
        )
        params = {
            'user_id': user_id,
            'vault_id': vault_id,
        }
        with get_db() as db:
            rows = db.execute(query, params).fetchall()
            return [VaultItem._from_row(row, encryption_key) for row in rows]

    @staticmethod
    def find_by_id(user_id, vault_id, item_id, encryption_key: bytes):
        query = (
            'SELECT id, data, created_on, updated_on '
            'FROM vault_item '
            'WHERE id = :item_id '
            'AND vault_id = :vault_id '
            'AND :user_id = (SELECT user_id from vault where id = :vault_id LIMIT 1) '
            'LIMIT 1 '
        )
        params = {
            'user_id': user_id,
            'vault_id': vault_id,
            'item_id': item_id,
        }
        with get_db() as db:
            row = db.execute(query, params).fetchone()
            return VaultItem._from_row(row, encryption_key) if row else None

    @staticmethod
    def create(user_id, vault_id, title, website, username, password, encryption_key: bytes):
        # Encrypt vault item data
        data = dict(
            title=title,
            website=website,
            username=username,
            password=password,
        )
        data = application_helper.encrypt(data, encryption_key)

        statement = (
            'INSERT INTO vault_item(vault_id, data) '
            'SELECT :vault_id, :data '
            'FROM vault '
            'WHERE id = :vault_id '
            'AND user_id = :user_id '
        )
        params = {
            'user_id': user_id,
            'vault_id': vault_id,
            'data': data,
        }
        with get_db() as db:
            db.execute(statement, params)

    @staticmethod
    def update(user_id, vault_id, item_id, title, website, username, password, encryption_key: bytes):
        # Encrypt vault item data
        data = dict(
            title=title,
            website=website,
            username=username,
            password=password,
        )
        data = application_helper.encrypt(data, encryption_key)

        statement = (
            'UPDATE vault_item '
            'SET data = :data, updated_on = CURRENT_TIMESTAMP '
            'WHERE id = :item_id '
            'AND vault_id = :vault_id '
            'AND :user_id = (SELECT user_id from vault where id = :vault_id LIMIT 1) '
        )
        params = {
            'user_id': user_id,
            'vault_id': vault_id,
            'item_id': item_id,
            'data': data,
        }
        with get_db() as db:
            db.execute(statement, params)

    @staticmethod
    def delete(user_id, vault_id, item_id):
        statement = (
            'DELETE FROM vault_item '
            'WHERE id = :item_id '
            'AND vault_id = :vault_id '
            'AND :user_id = (SELECT user_id from vault where id = :vault_id LIMIT 1) '
        )
        params = {
            'user_id': user_id,
            'vault_id': vault_id,
            'item_id': item_id,
        }
        with get_db() as db:
            db.execute(statement, params)
