from .settings import BASE_DIR


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "s)gh((cn*-8g&4ug&j%l+%g&&0zfdeyr!**!rz#k#hb&mh0kt*"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}