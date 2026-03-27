import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from statbot.agent import StatBotAgent
from django.conf import settings
import pandas as pd

df = pd.DataFrame({'col': range(891)})
df.to_csv('dummy.csv', index=False)

agent = StatBotAgent('dummy.csv')
res1 = agent.analyze("len(df)")
print(res1['thought'])
print("final answer:")
print(res1['answer'])
