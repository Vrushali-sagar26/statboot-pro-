import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from statbot.agent import StatBotAgent
from django.conf import settings

csv_path = os.path.join(settings.BASE_DIR, 'data', 'sales_data.csv')
agent = StatBotAgent(csv_path)

res = agent.analyze("len(df)")
print(res['thought'])
print("Final:", res['answer'])
