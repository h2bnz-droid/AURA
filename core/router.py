from core.chat import ask
from core.commands import detect_command
from core.memory_engine import process_memory
from services.profile_service import owner_name
from services.memory_service import remember
from services.memory_service import recall_all
from skills.manager import run
from core.engines.goal_engine import GoalEngine

goal_engine = GoalEngine()

def process_user_input(user_input: str) -> str:

    response = goal_engine.process(user_input)
    if response:
        return response

    # Cek apakah ini memori yang perlu disimpan
    memory = process_memory(user_input)

    if memory:
        remember(
            memory["category"],
            memory["key"],
            memory["value"]
        )

        return "Baik. Aku sudah mengingatnya."

    # Cek command lain
    command = detect_command(user_input)

    if command == "show_memory":
        return recall_all()

    if command == "who_am_i":
        name = owner_name()

        if name:
            return f"Nama Anda adalah {name}."

        return "Aku belum mengetahui nama Anda."
    
    skill = run(user_input)

    if skill:
        return skill

    # Selain itu kirim ke AI
    return ask(user_input)