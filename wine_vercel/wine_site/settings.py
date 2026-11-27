# Pengaturan untuk komputer sendiri dan Vercel
import os
from pathlib import Path

from django.core.management.utils import get_random_secret_key

BASE_DIR = Path(__file__).resolve().parent.parent
# Aplikasi tidak memakai login atau sesi, jadi kunci acak sudah cukup
SECRET_KEY = os.environ.get("SECRET_KEY") or get_random_secret_key()
DEBUG = False
ALLOWED_HOSTS = ["localhost", "127.0.0.1", ".vercel.app"]
INSTALLED_APPS = ["klasifikasi"]
MIDDLEWARE = ["django.middleware.csrf.CsrfViewMiddleware"]
ROOT_URLCONF = "wine_site.urls"
WSGI_APPLICATION = "wine_site.wsgi.application"
TEMPLATES = [{
    "BACKEND": "django.template.backends.django.DjangoTemplates",
    "APP_DIRS": True,
}]
# Vercel meneruskan permintaan HTTPS lewat header ini (diperlukan untuk CSRF)
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
LANGUAGE_CODE = "id"
USE_I18N = False
