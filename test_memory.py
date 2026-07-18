from services.memory_service import remember, recall
from database import initialize_database

initialize_database()

remember("personal", "warna_favorit", "biru")

print(recall("warna_favorit"))