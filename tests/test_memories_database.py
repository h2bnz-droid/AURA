from database.memories import (
    create_table,
    save_memory,
    get_memory,
    get_all_memories,
    search_memories,
)


def test_memory_table_exists():
    create_table()

    from database.connection import get_connection

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type = 'table'
          AND name = 'memories'
    """)

    row = cursor.fetchone()
    conn.close()

    assert row is not None


def test_save_and_get_memory():
    create_table()

    save_memory(
        "fact",
        "favorite_color",
        "Biru",
    )

    memory = get_memory("favorite_color")

    assert memory is not None
    assert memory["memory_value"] == "Biru"


def test_get_memory_returns_latest_value():
    create_table()

    save_memory(
        "fact",
        "test_latest_key",
        "Nilai lama",
    )

    save_memory(
        "fact",
        "test_latest_key",
        "Nilai terbaru",
    )

    memory = get_memory("test_latest_key")

    assert memory is not None
    assert memory["memory_value"] == "Nilai terbaru"


def test_get_all_memories():
    create_table()

    save_memory(
        "fact",
        "test_all_key",
        "Memory test",
    )

    memories = get_all_memories()

    assert len(memories) >= 1
    assert any(
        memory["memory_value"] == "Memory test"
        for memory in memories
    )


def test_search_memories():
    create_table()

    save_memory(
        "fact",
        "test_search_key",
        "Warna favorit adalah biru",
    )

    results = search_memories("biru")

    assert any(
        memory["memory_value"] == "Warna favorit adalah biru"
        for memory in results
    )