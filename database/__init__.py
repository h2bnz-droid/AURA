from database.profile import create_table as create_profile_table
from database.memories import create_table as create_memory_table
from database.conversations import create_table as create_conversation_table
from database.goals import create_table as create_goal_table
from database.learning import create_table as create_learning_table
from database.emotions import create_table as create_emotion_table
from database.temporal import create_table as create_temporal_table
from database.reflections import create_table as create_reflection_table
from database.relationships import create_table as create_relationship_table
from database.personal_cognitive_model import (
    create_table as create_personal_cognitive_model_table,
)


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

    create_learning_table()
    print("Learning OK")

    create_emotion_table()
    print("Emotions OK")

    create_reflection_table()
    print("Reflections OK")

    create_relationship_table()
    print("Relationships OK")

    create_personal_cognitive_model_table()
    print("Personal Cognitive Model OK")