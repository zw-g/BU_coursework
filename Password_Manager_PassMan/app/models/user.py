import os
import sqlite3
from dataclasses import dataclass
from datetime import datetime
from passlib.hash import bcrypt
from ..db import get_db


@dataclass
class User:
    id: int
    username: str
    salt: bytes
    created_on: datetime
    updated_on: datetime

    @staticmethod
    def _from_row(row):
        return User(
            row['id'],
            row['username'],
            row['salt'],
            row['created_on'],
            row['updated_on'],
        )

    @staticmethod
    def find_by_username_password(username, password):
        query = (
            'SELECT id, username, password_hash, salt, created_on, updated_on '
            'FROM user '
            'WHERE username = :username '
            'LIMIT 1 '
        )
        params = {
            'username': username,
        }
        with get_db() as db:
            row = db.execute(query, params).fetchone()
            if not row:
                return None
            if not bcrypt.verify(password, row['password_hash']):
                return None
            return User._from_row(row)

    @staticmethod
    def find_by_id(user_id):
        query = (
            'SELECT id, username, salt, created_on, updated_on '
            'FROM user '
            'WHERE id = :user_id '
            'LIMIT 1 '
        )
        params = {
            'user_id': user_id,
        }
        with get_db() as db:
            row = db.execute(query, params).fetchone()
            return User._from_row(row) if row else None

    @staticmethod
    def create(username, password):
        # Hash the user's password
        password_hash = bcrypt.hash(password)

        # Ref: https://cryptography.io/en/latest/fernet/#using-passwords-with-fernet
        salt = os.urandom(16)

        statement = (
            'INSERT INTO user(username, password_hash, salt) '
            'VALUES (:username, :password_hash, :salt) '
        )
        params = {
            'username': username,
            'password_hash': password_hash,
            'salt': salt,
        }
        try:
            with get_db() as db:
                db.execute(statement, params)
        except sqlite3.IntegrityError as ex:
            raise RuntimeError(f'Username {username} is already taken')
