import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from statbot.agent import StatBotAgent
from django.conf import settings

# using titanic.csv
csv_path = os.path.join(settings.BASE_DIR, 'media', 'datasets', 'titanic.csv')
agent = StatBotAgent(csv_path)

res = agent.analyze("len(df)")
print(f"Thought:\n{res['thought']}")
print(f"Answer:\n{res['answer']}")
