from database.profile import create_table as create_profile_table
from database.memories import create_table as create_memory_table
from database.conversations import create_table as create_conversation_table
from database.goals import create_table as create_goal_table


def initialize_database():
    print(">>> Initializing database...")

    create_profile_table()
    print("Profile OK")

    create_memory_table()
    print("Memories OK")

    create_conversation_table()
    print("Conversations OK")    

    create_goal_table()
    print("Goals OK")
