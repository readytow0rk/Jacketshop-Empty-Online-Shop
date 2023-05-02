import os

DATABASES = {
     'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
 }

os.environ["SECRET_KEY"]="django-insecure-j4ippt+3h39u4ontllpc8a(5h&^god(7aicz#@q^sl_(w)2otp"