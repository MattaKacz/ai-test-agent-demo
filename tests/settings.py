SECRET_KEY = 'fake-key-for-testing'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

INSTALLED_APPS = [
    'example.apps.ExampleConfig', # Use the AppConfig
]