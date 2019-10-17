from mtnmomo.collection import Collection
import os


COLLECTION_USER_ID = os.environ.get('COLLECTION_USER_ID')
COLLECTION_API_SECRET = os.environ.get('COLLECTION_API_SECRET')
COLLECTION_PRIMARY_KEY = os.environ.get('COLLECTION_PRIMARY_KEY')


collection_client = Collection(
    {
        "COLLECTION_USER_ID": COLLECTION_USER_ID,
        "COLLECTION_API_SECRET": COLLECTION_API_SECRET,
        "COLLECTION_PRIMARY_KEY": COLLECTION_PRIMARY_KEY
    })
