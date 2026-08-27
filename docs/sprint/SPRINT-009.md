# Sprint 009 — Personal Cognitive Model

## Status: Completed

Sprint kesembilan berfokus pada pembangunan **Personal Cognitive Model** sebagai lapisan yang mengintegrasikan informasi personal pengguna dari berbagai sistem AURA menjadi representasi yang terstruktur, dapat dilacak, dapat dikoreksi, dan dapat dikembangkan secara bertahap.

Personal Cognitive Model **bukan pengganti** Profile, Memory, Goal, Emotion, Temporal, Reflection, Relationship, atau Learning. Model ini menjadi lapisan integrasi yang membantu AURA membangun pemahaman personal yang lebih konsisten.

---

## Objective

Membangun Personal Cognitive Model yang:

* [x] menyimpan atribut personal pengguna
* [x] memiliki kategori atribut
* [x] menyimpan sumber informasi
* [x] menyimpan confidence
* [x] dapat mengambil informasi
* [x] dapat memperbarui informasi
* [x] dapat menghapus informasi
* [x] terintegrasi dengan Context Builder
* [x] terintegrasi dengan Prompt Builder
* [x] mempertahankan kompatibilitas dengan sistem AURA yang sudah ada

---

## Domain

### PersonalCognitiveModel

* [x] `PersonalCognitiveModel`
* [x] `CognitiveAttribute`
* [x] attribute name
* [x] attribute value
* [x] category
* [x] source
* [x] confidence
* [x] created_at
* [x] updated_at

### Initial Categories

* [x] identity
* [x] preference
* [x] value
* [x] interest
* [x] skill
* [x] habit
* [x] aspiration
* [x] life_stage

---

## Database

### Table

`personal_cognitive_model`

### Fields

* [x] id
* [x] attribute_name
* [x] attribute_value
* [x] category
* [x] source
* [x] confidence
* [x] created_at
* [x] updated_at

### Database Operations

* [x] `create_table`
* [x] `save_attribute`
* [x] `get_attribute`
* [x] `get_all_attributes`
* [x] `update_attribute`
* [x] `delete_attribute`

Database layer tetap menjadi satu-satunya layer yang berinteraksi langsung dengan SQLite.

---

## CognitiveModelService

`CognitiveModelService` menjadi abstraction layer antara Personal Cognitive Model dan database.

* [x] save attribute
* [x] retrieve attribute
* [x] retrieve all attributes
* [x] update attribute
* [x] delete attribute
* [x] confidence handling
* [x] source handling
* [x] validation handling

Service tidak memindahkan business logic database ke engine.

---

## Context Integration

`AuraContext` dikembangkan untuk mendukung Personal Cognitive Model sebagai bagian dari contextual intelligence AURA.

```text
profile
memories
history
emotion
temporal
reflection
relationship
learning
cognitive_model
```

### Context Builder

* [x] tambah `cognitive_model`
* [x] mengambil cognitive model
* [x] empty cognitive model handling
* [x] mempertahankan context yang sudah ada
* [x] tidak menggantikan Profile context
* [x] tidak menggantikan Memory context
* [x] tidak menggantikan Emotion context
* [x] tidak menggantikan Temporal context
* [x] tidak menggantikan Reflection context
* [x] tidak menggantikan Relationship context
* [x] tidak menggantikan Learning context
* [x] tidak menggantikan Conversation History

---

## Prompt Integration

Tambahkan section:

```text
[PERSONAL COGNITIVE MODEL]
```

### Target Prompt Ordering

```text
PROFILE

MEMORY

EMOTION

TEMPORAL

REFLECTION

RELATIONSHIP

LEARNING

PERSONAL COGNITIVE MODEL

RECENT CONVERSATION

CURRENT USER MESSAGE
```

### Prompt Requirements

* [x] cognitive model formatting
* [x] attribute formatting
* [x] source formatting bila diperlukan
* [x] confidence formatting bila diperlukan
* [x] empty cognitive model handling
* [x] ordering verification

---

## Engine Architecture

Sprint 009 **tidak membuat `CognitiveModelEngine` terlebih dahulu**.

Personal Cognitive Model pada sprint ini berfungsi sebagai:

```text
Domain
   ↓
Database
   ↓
Service
   ↓
Context
   ↓
Prompt
```

Engine baru dipertimbangkan pada sprint berikutnya apabila terdapat kebutuhan user-facing seperti:

```text
"Apa yang kamu tahu tentang saya?"

"Ubah preferensi saya."

"Lupakan informasi ini."
```

Tidak membuat engine hanya karena sistem lain memiliki engine.

---

## Cognitive Model Safety

Personal Cognitive Model harus bersifat:

* [x] structured
* [x] explainable
* [x] editable
* [x] confidence-aware
* [x] source-aware

### Rules

* [x] tidak melakukan psychological diagnosis
* [x] tidak menganggap inference sebagai fakta
* [x] inference memiliki confidence
* [x] source informasi dapat dilacak
* [x] pengguna dapat mengoreksi informasi
* [x] pengguna dapat menghapus informasi
* [x] model tidak menentukan nilai hidup pengguna
* [x] model tidak mengambil keputusan hidup secara autonomous

Contoh explicit information:

```text
attribute:

    skill = Python

source:

    user_statement

confidence:

    1.0
```

Contoh inference:

```text
attribute:

    preference = learning_by_practice

source:

    inference

confidence:

    0.72
```

Inference tidak boleh diperlakukan sama dengan fakta yang diberikan langsung oleh pengguna.

---

## Testing

### Domain Tests

* [x] PersonalCognitiveModel creation
* [x] CognitiveAttribute creation
* [x] attribute validation
* [x] category validation
* [x] confidence validation
* [x] source validation

### Database Tests

* [x] create table
* [x] save attribute
* [x] retrieve attribute
* [x] retrieve all attributes
* [x] update attribute
* [x] delete attribute
* [x] multiple attributes
* [x] empty database handling

### Service Tests

* [x] save attribute
* [x] retrieve attribute
* [x] retrieve all attributes
* [x] update attribute
* [x] delete attribute
* [x] source handling
* [x] confidence handling
* [x] database abstraction

### Context Tests

* [x] cognitive model masuk Context Builder
* [x] Context Builder meneruskan user input
* [x] cognitive model dapat kosong
* [x] context lama tetap kompatibel
* [x] existing context tidak hilang

### Prompt Tests

* [x] cognitive model masuk prompt
* [x] attribute formatting
* [x] empty model handling
* [x] prompt ordering
* [x] current user message tetap berada di akhir

### Integration Tests

* [x] PersonalCognitiveModel + Database
* [x] PersonalCognitiveModel + Service
* [x] CognitiveModelService + Context Builder
* [x] Context Builder + Prompt Builder
* [x] Personal Cognitive Model + Chat Pipeline

---

## Regression

Semua sistem dari Sprint 1–8 tetap kompatibel.

Full regression Sprint 009:

```text
190 passed
0 failed
0 errors
```

Sprint 009 telah melewati full regression sebelum dianggap selesai.

---

## Quality

* [x] Type hints
* [x] Single Responsibility
* [x] Separation of Concerns
* [x] Engine contract consistency
* [x] Service layer separation
* [x] Database abstraction
* [x] No direct database access from engine
* [x] No duplicated business logic
* [x] Test coverage
* [x] Documentation

---

## Acceptance Criteria

Sprint 009 dianggap selesai karena:

1. [x] Personal Cognitive Model memiliki domain yang jelas.
2. [x] Cognitive Attribute dapat dibuat.
3. [x] Attribute dapat disimpan.
4. [x] Attribute dapat diambil.
5. [x] Attribute dapat diperbarui.
6. [x] Attribute dapat dihapus.
7. [x] Category dapat disimpan.
8. [x] Source dapat dicatat.
9. [x] Confidence dapat dicatat.
10. [x] Database persistence berjalan.
11. [x] CognitiveModelService digunakan sebagai abstraction layer.
12. [x] Context Builder dapat mengambil Personal Cognitive Model.
13. [x] Prompt Builder dapat menggunakan Personal Cognitive Model.
14. [x] Empty state ditangani.
15. [x] Existing context tetap kompatibel.
16. [x] Tidak ada direct database access dari engine.
17. [x] Tidak ada psychological diagnosis otomatis.
18. [x] Inference dibedakan dari explicit user information.
19. [x] Unit tests tersedia.
20. [x] Integration tests tersedia.
21. [x] Full regression berhasil.
22. [x] Dokumentasi Sprint 009 selesai.

---

## Relation to AURA Master Blueprint

Sprint 009 menjadi fondasi menuju:

```text
Personal Cognitive Model
        ↓
Long-Term Context
        ↓
Life Timeline
        ↓
Adaptive Personalization
        ↓
Lifelong Cognitive Model
        ↓
Lifelong Personal Cognitive Companion
```

Sprint ini menjadi jembatan dari kumpulan sistem personal AURA menuju representasi pengguna yang lebih terstruktur.

---

## Result

Sprint 009 — Completed

Hasil akhir:

```text
190 passed
0 failed
0 errors
```

Komponen utama yang berhasil dibangun:

```text
Personal Cognitive Model
        ↓
SQLite Persistence
        ↓
CognitiveModelService
        ↓
AuraContext
        ↓
PromptBuilder
        ↓
AURA Cognitive Pipeline
```

Personal Cognitive Model sekarang menjadi salah satu sumber contextual intelligence AURA tanpa menggantikan subsystem personal yang sudah ada.

---

## Development Principle

Personal Cognitive Model harus membantu AURA **memahami pengguna dengan lebih baik tanpa mengambil alih identitas, nilai, keputusan, atau kehidupan pengguna**.

AURA harus semakin personal, tetapi tetap:

* human-centered
* privacy-aware
* explainable
* correctable
* confidence-aware
* modular
* testable

> AURA membantu manusia menjadi versi terbaik dirinya sendiri, bukan menentukan seperti apa versi terbaik tersebut.
