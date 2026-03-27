import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from statbot.models import QueryHistory
for qh in QueryHistory.objects.all().order_by('-created_at')[:5]:
    print("Query:", qh.query)
    print("Answer:", qh.answer)
    print("Thought contains 'error':", 'error' in str(qh.thought))
    print("Observation ending in error:", str(qh.thought).endswith('error'))
    print("Thought dump:")
    print(qh.thought)
    print('---')
