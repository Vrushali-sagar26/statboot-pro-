import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from langchain_google_genai import ChatGoogleGenerativeAI
from django.conf import settings
import traceback

GEMINI_API_KEY = getattr(settings, "GEMINI_API_KEY", os.environ.get("GEMINI_API_KEY", ""))

models_to_test = ["gemini-pro", "gemini-1.5-pro", "gemini-1.5-flash-latest", "gemini-1.0-pro"]
for m in models_to_test:
    try:
        model = ChatGoogleGenerativeAI(model=m, google_api_key=GEMINI_API_KEY, temperature=0, max_retries=1)
        res = model.invoke("Hello, say 'Test'")
        print(f"Success with {m}: {res.content}")
        break
    except Exception as e:
        print(f"Failed with {m}: {e}")
