from database.profile import get_profile, save_profile, update_name


def owner_name():
    profile = get_profile()

    if profile:
        return profile["name"]

    return None


def change_name(name: str):
    update_name(name)


def create_profile(name: str):
    save_profile(name)