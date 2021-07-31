from dataclasses import dataclass
from datetime import datetime
from ..helpers import application_helper
from ..db import get_db


@dataclass
class Vault:
    id: int
    title: str
    description: str
    created_on: datetime
    updated_on: datetime

    @staticmethod
    def _from_row(row, encryption_key: bytes):
        data = application_helper.decrypt(row['data'], encryption_key)
        return Vault(
            row['id'],
            data['title'],
            data['description'],
            row['created_on'],
            row['updated_on'],
        )

    @staticmethod
    def find_by_user(user_id, encryption_key: bytes):
        query = (
            'SELECT id, data, created_on, updated_on '
            'FROM vault '
            'WHERE user_id = :user_id '
            'ORDER BY created_on ASC '
        )
        params = {
            'user_id': user_id,
        }
        with get_db() as db:
            rows = db.execute(query, params).fetchall()
            return [Vault._from_row(row, encryption_key) for row in rows]

    @staticmethod
    def find_by_id(user_id, vault_id, encryption_key: bytes):
        query = (
            'SELECT id, data, created_on, updated_on '
            'FROM vault '
            'WHERE user_id = :user_id '
            'AND id = :vault_id '
            'LIMIT 1 '
        )
        params = {
            'user_id': user_id,
            'vault_id': vault_id,
        }
        with get_db() as db:
            row = db.execute(query, params).fetchone()
            return Vault._from_row(row, encryption_key) if row else None

    @staticmethod
    def create(user_id, title, description, encryption_key: bytes):
        # Encrypt vault data
        data = dict(title=title, description=description)
        data = application_helper.encrypt(data, encryption_key)

        statement = (
            'INSERT INTO vault(user_id, data) '
            'VALUES (:user_id, :data) '
        )
        params = {
            'user_id': user_id,
            'data': data,
        }
        with get_db() as db:
            db.execute(statement, params)
