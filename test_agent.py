import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from statbot.agent import StatBotAgent
from django.conf import settings

csv_path = os.path.join(settings.BASE_DIR, 'data', 'sales_data.csv')

agent = StatBotAgent(csv_path)

print("--- Testing Standard Query ---")
res1 = agent.analyze("How many rows are in the dataset?")
print("Answer:", res1['answer'])
print("Thought Length:", len(res1['thought']))

print("\n--- Testing Chart Generation ---")
res2 = agent.analyze("Plot the average sales per month (if applicable, or just any numerical data).")
print("Answer:", res2['answer'])
print("Chart URL:", res2['chart_url'])

print("Works!")
