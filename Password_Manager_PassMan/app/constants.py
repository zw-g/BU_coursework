# Enables or disables single vault mode.
# When enabled, users will not see the vault selection page.
# They will only see the default (first) vault's items.
SINGLE_VAULT_MODE = True

# The min/max password lengths required when
# signing up for an account with PassMan.
MIN_PASSWORD_LENGTH = 6
MAX_PASSWORD_LENGTH = 25

# The max lengths for various vault item fields
MAX_ITEM_TITLE_LENGTH = 50
MAX_ITEM_WEBSITE_LENGTH = 200
MAX_ITEM_USERNAME_LENGTH = 50
MAX_ITEM_PASSWORD_LENGTH = 50

# Do not check for user authentication for these endpoints.
NON_AUTHENTICATED_ENDPOINTS = [
    "home",
    "session.new",
    "session.create",
    "registration.new",
    "registration.create",
    "static",
]

# The database to use when running tests
TEST_DATABASE = 'test_database.db'
