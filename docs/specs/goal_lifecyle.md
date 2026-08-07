Sprint 5 — Goal Lifecycle Engine
Tujuan

AURA tidak hanya menyimpan goal, tetapi mampu menemani pengguna sampai goal tersebut selesai.

Alurnya:

User
 │
 ▼
"Aku ingin belajar Python"
 │
 ▼
Goal dibuat
 │
 ▼
"Aku sudah belajar 2 jam"
 │
 ▼
Progress bertambah
 │
 ▼
"Goal saya apa?"
 │
 ▼
Tampilkan progress
 │
 ▼
"Goal ini selesai."
 │
 ▼
Goal selesai
 │
 ▼
Refleksi & apresiasi
Sprint 5A
Domain

Buat enum baru atau lengkapi GoalIntent.

Misalnya:

class GoalIntent(Enum):
    UNKNOWN = auto()

    CREATE = auto()
    SHOW = auto()

    UPDATE = auto()
    COMPLETE = auto()
    ABANDON = auto()

    LIST = auto()

Kalau SHOW sudah mewakili LIST, tidak perlu ditambah. Kita tetap sederhana.

Sprint 5B
Database

Di database/goals.py tambahkan fungsi:

find_goal_by_title(title)

dan

get_goal(goal_id)

Karena nanti update progress membutuhkan goal tertentu.

Sprint 5C
Service

Tambahkan fungsi bisnis:

increase_progress(
    goal_id,
    amount
)

Logikanya:

progress lama

↓

+ amount

↓

maksimal 100

↓

simpan

Kalau mencapai 100%, otomatis panggil:

complete_goal()
Sprint 5D
Engine

Ini bagian yang paling menarik.

Sekarang GoalEngine hanya mengenali:

Aku ingin...

Nanti ia juga mengenali:

Hari ini aku belajar Python.

atau

Aku sudah latihan.

atau

Progressku bertambah.

Kemudian mencari goal yang paling relevan.

Misalnya:

Goal:

Belajar Python

User:

Hari ini aku belajar Python selama 2 jam.

↓

Engine menemukan:

Belajar Python

↓

Progress naik 10%.

Sprint 5E
Reflection

Ini yang membuat AURA berbeda.

Kalau progress naik:

AURA tidak hanya berkata:

Progress diperbarui.

Tetapi misalnya:

Bagus. Goal "Belajar Python" sekarang sudah mencapai 30%.

Konsistensi kecil seperti ini akan lebih berpengaruh daripada belajar berlebihan dalam satu hari.

Kalimat ini tidak perlu dibuat rumit. Yang penting terasa mendukung, bukan sekadar mengonfirmasi.

Struktur Sprint
Sprint 5

├── 5A Domain
├── 5B Database
├── 5C Service
├── 5D Engine
├── 5E Reflection
├── 5F Testing
└── Commit v0.3.0
Satu keputusan arsitektur

Mulai Sprint 5, kita mulai membedakan dua jenis respons AURA:

Respons operasional: membuat goal, mengubah progres, menampilkan daftar goal.
Respons pendamping: memberi refleksi, apresiasi, atau saran singkat setelah aksi selesai.

Dengan pemisahan ini, nanti akan lebih mudah jika kita ingin mengembangkan modul refleksi atau coaching tanpa mengubah logika Goal Engine.