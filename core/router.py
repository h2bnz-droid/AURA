from core.chat import ask
from core.commands import detect_command
from core.context_builder import build_context

from core.engines.engine_manager import EngineManager

from services.profile_service import owner_name
from services.memory_service import recall_all

from skills.manager import run


engine_manager = EngineManager()


def process_user_input(user_input: str) -> str:
    # Build context untuk kebutuhan AI layer.
    context = build_context(user_input)

    # Semua engine tetap menggunakan user_input
    # agar kontrak engine existing tidak berubah.
    response = engine_manager.process(user_input)

    if response:
        return response

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

    # Context nantinya digunakan AI layer.
    return ask(user_input)