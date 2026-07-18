from core.kernel import AuraKernel
from core.router import process
from database import initialize_database
from database.profile import (
    get_profile,
    save_profile
)

initialize_database()

kernel = AuraKernel()

profile = get_profile()

if profile is None:

    print("\nHalo 😊")
    print("Aku AURA.")
    print("Sebelum kita mulai...")

    name = input("Siapa nama Anda? : ")

    save_profile(name)

    owner_name = name

else:

    owner_name = profile["name"]

    print(f"\nSelamat datang kembali, {owner_name} 😊")

print("=" * 50)
print("        AURA v0.0.2 - Genesis")
print("=" * 50)

while True:

    user = input("\nAnda : ")

    if user.lower() in ["exit", "quit", "keluar"]:
        print("\nAURA : Sampai jumpa 😊")
        break

    print("\nAURA :", kernel.process(user))