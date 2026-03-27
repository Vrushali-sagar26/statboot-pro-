import os
import django
import json
from django.test import RequestFactory
from django.http import JsonResponse

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from statbot.views import ProcessQueryView
from statbot.models import Dataset, QueryHistory

def test_caching():
    print("--- Running Caching Verification ---")
    
    # Get or create a dataset
    dataset = Dataset.objects.first()
    if not dataset:
        print("No dataset found. Please run migrations and add a dataset first.")
        return

    factory = RequestFactory()
    view = ProcessQueryView.as_view()
    
    query_text = "What is the total number of records?"
    
    # 1. Clear existing history for this query to ensure a clean start
    QueryHistory.objects.filter(dataset=dataset, query=query_text).delete()
    
    # 2. First call (should NOT be cached)
    print(f"Executing first call for query: '{query_text}'...")
    request = factory.post('/process_query/', {'query': query_text, 'dataset_id': dataset.id})
    response = view(request)
    data = json.loads(response.content)
    
    print(f"First call 'cached' status: {data.get('cached')}")
    
    # 3. Second call (should BE cached)
    print("Executing second call for the same query...")
    request = factory.post('/process_query/', {'query': query_text, 'dataset_id': dataset.id})
    response = view(request)
    data = json.loads(response.content)
    
    print(f"Second call 'cached' status: {data.get('cached')}")
    
    if data.get('cached') is True:
        print("SUCCESS: Caching is working correctly!")
    else:
        print("FAILURE: Second call was not cached.")

if __name__ == "__main__":
    test_caching()
