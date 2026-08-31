from core.domain.mindset import Mindset


DEFAULT_MINDSETS = [
    Mindset(
        name="growth",
        description="Melihat kemampuan sebagai sesuatu yang dapat berkembang melalui belajar dan latihan.",
    ),
    Mindset(
        name="resilient",
        description="Memandang kesulitan sebagai sesuatu yang dapat dihadapi dan dipelajari.",
    ),
    Mindset(
        name="reflective",
        description="Mendorong evaluasi terhadap pengalaman untuk memahami perkembangan diri.",
    ),
]


def get_mindsets() -> list[Mindset]:
    return list(DEFAULT_MINDSETS)


def find_mindset(name: str) -> Mindset | None:
    query = name.strip().casefold()

    if not query:
        return None

    for mindset in DEFAULT_MINDSETS:
        if mindset.name.casefold() == query:
            return mindset

    return None

def detect_mindset(text: str) -> Mindset | None:
    query = text.strip().casefold()

    if not query:
        return None

    growth_keywords = (
        "belajar",
        "berkembang",
        "meningkatkan",
        "latihan",
        "skill",
        "kemampuan",
        "belajar lagi",
    )

    resilient_keywords = (
        "gagal",
        "sulit",
        "kesulitan",
        "masalah",
        "menyerah",
        "jatuh",
        "bangkit",
    )

    reflective_keywords = (
        "evaluasi",
        "refleksi",
        "merenung",
        "pengalaman",
        "apa yang salah",
        "apa yang bisa dipelajari",
    )

    if any(keyword in query for keyword in resilient_keywords):
        return find_mindset("resilient")

    if any(keyword in query for keyword in reflective_keywords):
        return find_mindset("reflective")

    if any(keyword in query for keyword in growth_keywords):
        return find_mindset("growth")

    return None