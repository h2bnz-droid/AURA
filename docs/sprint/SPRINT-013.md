# Sprint 013 — Mindset & Cognitive State

## Status: Completed

Sprint ketiga belas berfokus pada pembangunan **Mindset System** sebagai bagian dari cognitive layer AURA.

Sprint ini memungkinkan AURA untuk:

* menyimpan definisi mindset,
* mengenali mindset berdasarkan input pengguna,
* menentukan `active_mindset`,
* memasukkan mindset ke dalam `AuraContext`,
* mengintegrasikan mindset ke dalam Integrated Cognitive Context,
* menyediakan informasi mindset melalui `MindsetEngine`,
* dan meneruskan informasi mindset ke Prompt Builder sebagai konteks bagi AI.

Sprint 013 merupakan kelanjutan dari:

```text
Sprint 009
Personal Cognitive Model

        ↓

Sprint 010
Long-Term Context Management

        ↓

Sprint 011
Integrated Cognitive Context

        ↓

Sprint 012
Adaptive Personalization

        ↓

Sprint 013
Mindset & Cognitive State
```

---

## 1. Mindset Domain

Mindset direpresentasikan sebagai domain object sederhana menggunakan dataclass.

```python
@dataclass
class Mindset:
    name: str
    description: str
```

Mindset memiliki:

* `name`
* `description`

Desain ini menjaga domain tetap sederhana dan tidak bergantung pada service maupun persistence layer.

---

## 2. Mindset Service

Mindset Service menyediakan sumber data dan operasi dasar untuk mindset.

## Available Mindsets

AURA saat ini memiliki tiga mindset dasar:

### Growth

Melihat kemampuan sebagai sesuatu yang dapat berkembang melalui belajar dan latihan.

### Resilient

Memandang kesulitan sebagai sesuatu yang dapat dihadapi dan dipelajari.

### Reflective

Mendorong evaluasi terhadap pengalaman untuk memahami perkembangan diri.

---

## Service API

### `get_mindsets()`

Mengembalikan seluruh mindset yang tersedia.

### `find_mindset(name)`

Mencari mindset berdasarkan nama.

Pencarian menggunakan normalisasi:

* `strip()`
* `casefold()`

Sehingga pencarian tidak bergantung pada kapitalisasi.

### `detect_mindset(text)`

Menganalisis input pengguna dan menentukan mindset yang paling relevan.

Saat ini mendukung:

```text
growth
resilient
reflective
```

Jika tidak ditemukan indikasi yang sesuai:

```text
None
```

akan dikembalikan.

---

## 3. Mindset Detection

Mindset detection menggunakan keyword-based detection.

## Growths

Contoh indikator:

```text
belajar
berkembang
meningkatkan
latihan
skill
kemampuan
belajar lagi
```

Contoh:

```text
Aku ingin meningkatkan kemampuan Python
```

menghasilkan:

```text
growth
```

---

## Resilients

Contoh indikator:

```text
gagal
sulit
kesulitan
masalah
menyerah
jatuh
bangkit
```

Contoh:

```text
Aku gagal lagi dan rasanya ingin menyerah
```

menghasilkan:

```text
resilient
```

---

## Reflectives

Contoh indikator:

```text
evaluasi
refleksi
merenung
pengalaman
apa yang salah
apa yang bisa dipelajari
```

Contoh:

```text
Aku ingin evaluasi dari pengalaman ini
```

menghasilkan:

```text
reflective
```

---

## 4. AuraContext Integration

`AuraContext` diperluas dengan dua atribut baru:

```python
self.mindsets = []
self.active_mindset = None
```

## `mindsets`

Berisi seluruh mindset yang tersedia bagi AURA.

## `active_mindset`

Berisi mindset yang dianggap paling relevan dengan input pengguna saat context dibangun.

Contoh:

```text
User input:
"Aku gagal lagi belajar Python dan ingin menyerah"

active_mindset:
resilient
```

Dengan demikian mindset menjadi bagian dari state kognitif sementara AURA.

---

## 5. Context Builder Integration

`build_context()` sekarang melakukan:

```python
context.mindsets = get_mindsets()
context.active_mindset = detect_mindset(user_input)
```

Alur context menjadi:

```text
User Input
    │
    ▼
Context Builder
    │
    ├── Profile
    ├── Memory
    ├── History
    ├── Emotion
    ├── Reflection
    ├── Relationship
    ├── Cognitive Model
    ├── Long-Term Context
    ├── Integrated Cognitive Context
    ├── Personalization
    │
    └── Mindset
          │
          ├── Available Mindsets
          └── Active Mindset
```

---

## 6. Integrated Cognitive Context

Mindset juga diintegrasikan ke dalam `IntegratedCognitiveContext`.

Mindset direpresentasikan sebagai cognitive context item:

```text
category = mindset
value    = growth / resilient / reflective
source   = mindset_service
```

Dengan demikian mindset tidak menjadi subsystem yang berdiri sendiri, tetapi dapat menjadi bagian dari cognitive context yang dikonsumsi oleh sistem lain.

---

## 7. Prompt Builder Integration

Prompt Builder mendapatkan dua section baru.

## `[MINDSET]`

Berisi seluruh mindset yang tersedia.

Contoh:

```text
[MINDSET]

- growth: Melihat kemampuan sebagai sesuatu yang dapat berkembang melalui belajar dan latihan.
- resilient: Memandang kesulitan sebagai sesuatu yang dapat dihadapi dan dipelajari.
- reflective: Mendorong evaluasi terhadap pengalaman untuk memahami perkembangan diri.
```

---

## `[ACTIVE MINDSET]`

Berisi mindset yang sedang aktif berdasarkan input pengguna.

Contoh:

```text
[ACTIVE MINDSET]

- resilient: Memandang kesulitan sebagai sesuatu yang dapat dihadapi dan dipelajari.
```

Dengan demikian AI layer dapat menerima informasi mengenai keadaan mindset pengguna sebagai bagian dari internal context.

---

## 8. Mindset Engine

AURA memiliki `MindsetEngine` yang mengikuti kontrak `BaseEngine`.

Engine mendukung dua kategori utama.

## Show Mindset

Contoh:

```text
lihat mindset
```

atau:

```text
tampilkan mindset
```

AURA menampilkan seluruh mindset yang tersedia.

---

## Find Mindset

Contoh:

```text
jelaskan mindset growth
```

atau:

```text
apa itu mindset resilient
```

AURA mencari mindset berdasarkan nama dan mengembalikan deskripsinya.

---

## Unknown Mindset

Jika mindset tidak ditemukan:

```text
Mindset 'xxx' belum dikenali.
```

---

## 9. Engine Integration

`MindsetEngine` telah diintegrasikan ke dalam `EngineManager`.

Dengan demikian engine dapat berpartisipasi dalam routing normal AURA.

Struktur:

```text
User Input
    │
    ▼
Router
    │
    ▼
EngineManager
    │
    ├── ProfileEngine
    ├── MemoryEngine
    ├── GoalEngine
    ├── LearningEngine
    ├── PlannerEngine
    ├── DecisionEngine
    ├── KnowledgeEngine
    ├── ConversationEngine
    ├── ReflectionEngine
    └── MindsetEngine
```

Engine tetap menggunakan kontrak:

```python
analyze(message)
process(message)
```

sehingga tidak mengubah arsitektur engine yang sudah ada.

---

## 10. AI Pipeline Integration

Mindset sekarang mengalir melalui pipeline:

```text
User Input
    │
    ▼
Context Builder
    │
    ├── detect_mindset()
    │
    ▼
AuraContext
    │
    ├── mindsets
    └── active_mindset
    │
    ▼
Prompt Builder
    │
    ├── [MINDSET]
    └── [ACTIVE MINDSET]
    │
    ▼
AI Provider
    │
    ▼
AURA Response
```

Hal ini membuat mindset menjadi bagian dari **AI context**, bukan sekadar command response.

---

## 11. Testing

Sprint 013 menambahkan dan mempertahankan testing pada beberapa layer.

## Mindset Domain

* Mindset object
* Mindset attributes

## Mindset Service

* `get_mindsets()`
* `find_mindset()`
* `detect_mindset()`

## Mindset Detection

Test untuk:

```text
growth
resilient
reflective
unknown
```

## Context

Test untuk:

```text
mindsets
active_mindset
```

## Integrated Cognitive Context

Test untuk memastikan mindset dapat masuk ke cognitive context.

## Prompt Builder

Test untuk:

```text
[MINDSET]
[ACTIVE MINDSET]
```

## Mindset Engine

Test untuk:

```text
show
find
unknown
active mindset
```

## Engine Integration

Test memastikan `MindsetEngine` terdaftar pada `EngineManager`.

---

## 12. Regression Test

Regression terakhir:

```text
312 passed
```

Status:

```text
PASS
```

Tidak terdapat regression failure yang menghalangi penyelesaian Sprint 013.

---

## 13. Architecture Impact

Sprint 013 menambahkan cognitive state baru tanpa mengubah fundamental architecture AURA.

Dependency direction tetap:

```text
Domain
  ↑
Service
  ↑
Context
  ↑
Engine / Prompt
  ↑
AI Layer
```

Mindset tetap dipisahkan menjadi:

```text
core/domain/mindset.py
        │
        ▼
services/mindset_service.py
        │
        ├───────────────┐
        ▼               ▼
Context Builder      Mindset Engine
        │               │
        ▼               │
AuraContext            │
        │               │
        └───────┬───────┘
                ▼
          Prompt Builder
                │
                ▼
            AI Provider
```

Tidak ada persistence database yang diperlukan untuk Sprint 013 karena mindset yang dibangun pada sprint ini masih bersifat predefined cognitive model.

---

## 14. Design Principles

Sprint 013 mempertahankan prinsip utama AURA:

* Modular Architecture
* Single Responsibility
* Separation of Concerns
* Consistent Engine Contract
* Service Layer Separation
* Domain Isolation
* Context-driven AI pipeline
* Test-driven verification

Mindset detection berada di service layer, bukan di Prompt Builder atau AI Provider.

Dengan demikian masing-masing layer memiliki tanggung jawab yang jelas.

---

## 15. Definition of Done

```text
[x] Mindset domain
[x] Mindset service
[x] Mindset retrieval
[x] Mindset lookup
[x] Mindset detection
[x] Growth detection
[x] Resilient detection
[x] Reflective detection
[x] Unknown detection
[x] AuraContext integration
[x] Active mindset
[x] Context Builder integration
[x] Integrated Cognitive Context integration
[x] Prompt Builder integration
[x] MindsetEngine
[x] EngineManager integration
[x] AI context integration
[x] Unit tests
[x] Integration tests
[x] Regression testing
[x] Documentation
```

---

## 16. Final Result

Sprint 013 berhasil menambahkan **Mindset & Cognitive State** ke dalam cognitive architecture AURA.

AURA sekarang tidak hanya mengetahui:

```text
siapa pengguna
apa yang diingat
apa yang sedang dipelajari
apa tujuan pengguna
bagaimana emosi pengguna
apa refleksi pengguna
bagaimana pola kognitif pengguna
bagaimana preferensi pengguna
```

tetapi juga dapat mempertimbangkan:

```text
mindset pengguna saat ini
```

Contoh:

```text
User:
"Aku gagal lagi belajar Python dan ingin menyerah."

        ↓

Mindset Detection

        ↓

active_mindset = resilient

        ↓

AuraContext

        ↓

Prompt Builder

        ↓

[ACTIVE MINDSET]
resilient

        ↓

AI Provider

        ↓

Response AURA
```

Dengan selesainya Sprint 013, **Mindset System resmi menjadi bagian dari cognitive context AURA**.

---

## Sprint 013 Final Status

```text
Sprint 013 — Mindset & Cognitive State

Status:
COMPLETED

Regression:
312 passed

Architecture:
Stable

Integration:
Completed

Documentation:
Completed
```

Sprint 013 dinyatakan **SELESAI**.
