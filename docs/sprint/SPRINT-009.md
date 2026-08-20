# Sprint 009 — Personal Cognitive Model

## Status: Planned

Sprint kesembilan berfokus pada pembangunan **Personal Cognitive Model** sebagai lapisan yang mengintegrasikan informasi personal pengguna dari berbagai sistem AURA menjadi representasi yang terstruktur, dapat dilacak, dapat dikoreksi, dan dapat dikembangkan secara bertahap.

Personal Cognitive Model **bukan pengganti** Profile, Memory, Goal, Emotion, Temporal, Reflection, Relationship, atau Learning. Model ini menjadi lapisan integrasi yang membantu AURA membangun pemahaman personal yang lebih konsisten.

---

## Objective

Membangun Personal Cognitive Model yang:

* menyimpan atribut personal pengguna
* memiliki kategori atribut
* menyimpan sumber informasi
* menyimpan confidence
* dapat mengambil informasi
* dapat memperbarui informasi
* dapat menghapus informasi
* terintegrasi dengan Context Builder
* terintegrasi dengan Prompt Builder
* mempertahankan kompatibilitas dengan sistem AURA yang sudah ada

---

## Domain

### PersonalCognitiveModel

* [ ] `PersonalCognitiveModel`
* [ ] `CognitiveAttribute`
* [ ] attribute name
* [ ] attribute value
* [ ] category
* [ ] source
* [ ] confidence
* [ ] created_at
* [ ] updated_at

### Initial Categories

* [ ] identity
* [ ] preference
* [ ] value
* [ ] interest
* [ ] skill
* [ ] habit
* [ ] aspiration
* [ ] life_stage

---

## Database

### Table

`personal_cognitive_model`

### Fields

* [ ] id
* [ ] attribute_name
* [ ] attribute_value
* [ ] category
* [ ] source
* [ ] confidence
* [ ] created_at
* [ ] updated_at

### Database Operations

* [ ] `create_table`
* [ ] `save_attribute`
* [ ] `get_attribute`
* [ ] `get_all_attributes`
* [ ] `update_attribute`
* [ ] `delete_attribute`

Database layer harus tetap menjadi satu-satunya layer yang berinteraksi langsung dengan SQLite.

---

## CognitiveModelService

`CognitiveModelService` menjadi abstraction layer antara Personal Cognitive Model dan database.

* [ ] save attribute
* [ ] retrieve attribute
* [ ] retrieve all attributes
* [ ] update attribute
* [ ] delete attribute
* [ ] confidence handling
* [ ] source handling
* [ ] validation handling

Service tidak boleh memindahkan business logic database ke engine.

---

## Context Integration

`AuraContext` dikembangkan menjadi:

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

* [ ] tambah `cognitive_model`
* [ ] mengambil cognitive model
* [ ] empty cognitive model handling
* [ ] mempertahankan context yang sudah ada
* [ ] tidak menggantikan Profile context
* [ ] tidak menggantikan Memory context
* [ ] tidak menggantikan Emotion context
* [ ] tidak menggantikan Temporal context
* [ ] tidak menggantikan Reflection context
* [ ] tidak menggantikan Relationship context
* [ ] tidak menggantikan Learning context
* [ ] tidak menggantikan Conversation History

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

* [ ] cognitive model formatting
* [ ] attribute formatting
* [ ] source formatting bila diperlukan
* [ ] confidence formatting bila diperlukan
* [ ] empty cognitive model handling
* [ ] ordering verification

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

Tidak boleh membuat engine hanya karena sistem lain memiliki engine.

---

## Cognitive Model Safety

Personal Cognitive Model harus bersifat:

* [ ] structured
* [ ] explainable
* [ ] editable
* [ ] confidence-aware
* [ ] source-aware

### Rules

* [ ] tidak melakukan psychological diagnosis
* [ ] tidak menganggap inference sebagai fakta
* [ ] inference harus memiliki confidence
* [ ] source informasi dapat dilacak
* [ ] pengguna dapat mengoreksi informasi
* [ ] pengguna dapat menghapus informasi
* [ ] model tidak menentukan nilai hidup pengguna
* [ ] model tidak mengambil keputusan hidup secara autonomous

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

* [ ] PersonalCognitiveModel creation
* [ ] CognitiveAttribute creation
* [ ] attribute validation
* [ ] category validation
* [ ] confidence validation
* [ ] source validation

### Database Tests

* [ ] create table
* [ ] save attribute
* [ ] retrieve attribute
* [ ] retrieve all attributes
* [ ] update attribute
* [ ] delete attribute
* [ ] multiple attributes
* [ ] empty database handling

### Service Tests

* [ ] save attribute
* [ ] retrieve attribute
* [ ] retrieve all attributes
* [ ] update attribute
* [ ] delete attribute
* [ ] source handling
* [ ] confidence handling
* [ ] database abstraction

### Context Tests

* [ ] cognitive model masuk Context Builder
* [ ] Context Builder meneruskan user input
* [ ] cognitive model dapat kosong
* [ ] context lama tetap kompatibel
* [ ] existing context tidak hilang

### Prompt Tests

* [ ] cognitive model masuk prompt
* [ ] attribute formatting
* [ ] empty model handling
* [ ] prompt ordering
* [ ] current user message tetap berada di akhir

### Integration Tests

* [ ] PersonalCognitiveModel + Database
* [ ] PersonalCognitiveModel + Service
* [ ] CognitiveModelService + Context Builder
* [ ] Context Builder + Prompt Builder
* [ ] Personal Cognitive Model + Chat Pipeline

---

## Regression

Semua sistem dari Sprint 1–8 harus tetap kompatibel.

Target:

```text
0 failed
0 errors
```

Full regression wajib dilakukan setelah seluruh implementasi Sprint 009 selesai.

---

## Quality

* [ ] Type hints
* [ ] Single Responsibility
* [ ] Separation of Concerns
* [ ] Engine contract consistency
* [ ] Service layer separation
* [ ] Database abstraction
* [ ] No direct database access from engine
* [ ] No duplicated business logic
* [ ] Test coverage
* [ ] Documentation

---

## Acceptance Criteria

Sprint 009 dianggap selesai apabila:

1. Personal Cognitive Model memiliki domain yang jelas.
2. Cognitive Attribute dapat dibuat.
3. Attribute dapat disimpan.
4. Attribute dapat diambil.
5. Attribute dapat diperbarui.
6. Attribute dapat dihapus.
7. Category dapat disimpan.
8. Source dapat dicatat.
9. Confidence dapat dicatat.
10. Database persistence berjalan.
11. CognitiveModelService digunakan sebagai abstraction layer.
12. Context Builder dapat mengambil Personal Cognitive Model.
13. Prompt Builder dapat menggunakan Personal Cognitive Model.
14. Empty state ditangani.
15. Existing context tetap kompatibel.
16. Tidak ada direct database access dari engine.
17. Tidak ada psychological diagnosis otomatis.
18. Inference dibedakan dari explicit user information.
19. Unit tests tersedia.
20. Integration tests tersedia.
21. Full regression berhasil.
22. Dokumentasi Sprint 009 selesai.

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

Sprint ini merupakan jembatan dari kumpulan sistem personal AURA menuju representasi pengguna yang lebih terstruktur.

---

## Result

Sprint 009 belum dimulai.

Target akhir:

```text
XXX passed
0 failed
0 errors
```

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
