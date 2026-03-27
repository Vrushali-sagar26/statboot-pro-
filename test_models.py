import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

import google.generativeai as genai
from django.conf import settings

GEMINI_API_KEY = getattr(settings, "GEMINI_API_KEY", os.environ.get("GEMINI_API_KEY", ""))
genai.configure(api_key=GEMINI_API_KEY)

print("Models:")
for m in genai.list_models():
    print(m.name)
