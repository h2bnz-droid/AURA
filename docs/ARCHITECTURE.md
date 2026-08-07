# AURA Architecture

Version : Sprint 1
Status : Stable
Last Updated : 2026-08-07

## Overview

AURA adalah AI Assistant yang dibangun dengan arsitektur modular.

Setiap kemampuan AURA dipisahkan menjadi Engine yang memiliki tanggung jawab tunggal (Single Responsibility).

Semua Engine berkomunikasi dengan Service, kemudian Service mengakses Database.

```text
User
   │
   ▼
Router
   │
   ▼
Engine Manager
   │
   ├───────────────┐
   │               │
ProfileEngine      │
MemoryEngine       │
GoalEngine         │
ReflectionEngine   │
PlannerEngine (future)
DecisionEngine (future)
KnowledgeEngine (future)
   │
   ▼
Services
   │
   ▼
SQLite Database
```

---

## Architecture Rules

Engine tidak boleh:

- Mengakses SQLite secara langsung.
- Mengakses Engine lain secara langsung.
- Menjalankan SQL.
- Menyimpan state permanen.

Semua operasi data harus melalui Service.

## Project Structure

```text
AURA
│
├── core
│   ├── engines
│   ├── domain
│   ├── router
│   └── manager
│
├── services
│
├── database
│
├── tests
│
├── docs
│
└── main.py
```

---

## Engine Layer

Engine bertanggung jawab memahami intent pengguna dan menghasilkan respons.

Engine tidak boleh berkomunikasi langsung dengan database.

Semua operasi data dilakukan melalui Service.

Setiap Engine mengikuti pola berikut.

```text
analyze()

↓

extract() / collect()

↓

validate()

↓

process()
```

---

## Profile Engine

Tugas:

- Mengelola identitas pengguna
- Mengubah nama
- Mengambil profil

Contoh:

```text
Namaku Budi

↓

ProfileEngine

↓

ProfileService

↓

Database
```

---

## Memory Engine

Tugas:

- Menyimpan catatan
- Mengambil kembali memori

Contoh:

```text
Ingat bahwa aku suka kopi

↓

MemoryEngine

↓

MemoryService

↓

Database
```

---

## Goal Engine

Tugas:

- Membuat goal
- Mengubah progress
- Menyelesaikan goal
- Menghapus goal

---

## Reflection Engine

Reflection menggunakan informasi dari beberapa sumber.

```text
Profile

+

Memory

+

Goal

↓

Reflection
```

Reflection tidak membuat data baru sendiri.

Reflection mengambil konteks dari Engine lain.

---

## Service Layer

Service menjadi perantara antara Engine dan Database.

Engine tidak boleh mengakses SQLite secara langsung.

```text
Engine

↓

Service

↓

Database
```

Contoh:

```text
GoalEngine

↓

GoalService

↓

database/goals.py
```

---

## Database Layer

Semua akses SQLite berada di folder database.

Setiap tabel memiliki file sendiri.

Contoh:

```text
profile.py

memory.py

goals.py

reflection.py
```

---

## Engine Contract

Setiap Engine harus mengimplementasikan kontrak berikut.

```python
class BaseEngine(ABC):

    @abstractmethod
    def analyze(self, message: str):
        ...

    @abstractmethod
    def process(self, message: str):
        ...
```

Method tambahan bersifat opsional, misalnya:

- extract()
- validate()
- collect_context()
- generate()

```text
analyze(message)

process(message)
```

Engine boleh memiliki:

```python
extract()

validate()

collect_context()

generate()
```

Tetapi process() selalu menjadi entry point.

---

## Core Principles

AURA mengikuti prinsip berikut.

1. Separation of Concerns
2. Single Responsibility Principle
3. Engine-First Architecture
4. Service Layer Pattern
5. Modular Design
6. Testable Components

## Design Principles

AURA mengikuti beberapa prinsip.

- Single Responsibility Principle
- Modular Architecture
- Separation of Concerns
- Service Layer Pattern

---

## Design Goals

Arsitektur AURA dirancang dengan tujuan:

- Modular sehingga mudah menambah Engine baru.
- Mudah diuji (unit test).
- Engine tidak bergantung pada database.
- Service menjadi satu-satunya jalur akses data.
- Setiap Engine memiliki satu tanggung jawab utama.

## Request Flow

```text
User
 │
 ▼
Router
 │
 ▼
EngineManager
 │
 ▼
Selected Engine
 │
 ▼
Service
 │
 ▼
Database
 │
 ▼
Response
```

## Roadmap

### Sprint 2

| Engine | Purpose |
| --------- | ---------- |
| PlannerEngine | Membuat rencana tindakan |
| DecisionEngine | Mengambil keputusan |
| KnowledgeEngine | Manajemen pengetahuan |
| ConversationEngine | Percakapan umum |

### Sprint 3

| Engine | Purpose |
| --------- | ---------- |
| EmotionEngine | Analisis emosi |
| LearningEngine | Pembelajaran adaptif |
| SecurityEngine | Keamanan sistem |
