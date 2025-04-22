import os
import django
from django.conf import settings
from django.db import connection

# 👇 CAMBIA ESTO por el path correcto a tu settings si está en otro subdirectorio
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ttarena_backend.settings")

django.setup()

print("==== Django DB Settings ====")
print(settings.DATABASES["default"])

print("\n==== Connection Info ====")
print(connection.settings_dict)
