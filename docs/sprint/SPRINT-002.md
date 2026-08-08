# Sprint 2 — Intelligence Expansion

## Overview

Sprint 2 berfokus pada perluasan kemampuan AURA dari fitur dasar menuju kemampuan perencanaan, pengambilan keputusan, pencarian pengetahuan, dan percakapan umum.

Sprint ini juga memastikan seluruh engine baru dapat diintegrasikan melalui `EngineManager` tanpa mengganggu engine yang sudah ada.

## Objectives

Tujuan Sprint 2:

* Menambahkan kemampuan membuat rencana.
* Menambahkan kemampuan membandingkan pilihan dan mengambil keputusan.
* Menambahkan kemampuan mencari dan menjelaskan pengetahuan.
* Menambahkan kemampuan menangani percakapan umum.
* Mengintegrasikan seluruh engine ke `EngineManager`.
* Menjaga konsistensi kontrak dan perilaku antar-engine.
* Menambahkan unit test dan integration test.
* Memastikan seluruh test suite tetap lulus.

## Completed Components

### Planner

Planner bertanggung jawab menangani perencanaan berdasarkan tujuan pengguna.

Komponen:

* `PlannerIntent`
* `PlannerEngine`
* `PlannerService`
* `database/plans.py`
* Planner unit tests
* Planner integration test

Kemampuan utama:

* Menganalisis perintah pembuatan rencana.
* Mengekstrak tujuan dari pesan pengguna.
* Memvalidasi tujuan.
* Menghasilkan langkah-langkah rencana.
* Menyimpan rencana ke database.

Contoh:

```text
Buat rencana untuk belajar Python

↓

PlannerEngine

↓

PlannerService

↓

plans database

↓

Daftar langkah rencana
```

## Decision

Decision bertanggung jawab membantu pengguna membandingkan pilihan dan mengambil keputusan.

Komponen:

* `DecisionIntent`
* `DecisionEngine`
* Decision unit tests

Kemampuan utama:

* Mendeteksi intent membandingkan pilihan.
* Mendeteksi intent mengambil keputusan.
* Mengekstrak pilihan.
* Memvalidasi pilihan.
* Membandingkan opsi.
* Menghasilkan keputusan.

## Knowledge

Knowledge bertanggung jawab menangani permintaan pencarian dan penjelasan pengetahuan.

Komponen:

* `KnowledgeIntent`
* `KnowledgeEngine`
* Knowledge unit tests

Kemampuan utama:

* Mendeteksi permintaan pencarian informasi.
* Mendeteksi permintaan penjelasan.
* Mengekstrak query.
* Memvalidasi query.
* Menangani query dengan kata penghubung seperti `tentang`.

Contoh:

```text
Cari informasi tentang Python

↓

KnowledgeEngine

↓

Query: Python
```

## Conversation

Conversation bertanggung jawab menangani percakapan umum yang tidak ditangani oleh engine khusus.

Komponen:

* `ConversationIntent`
* `ConversationEngine`
* Conversation unit tests

Intent yang digunakan:

* `GREETING`
* `CHAT`
* `UNKNOWN`

ConversationEngine ditempatkan sebagai salah satu engine terakhir sehingga dapat berfungsi sebagai fallback untuk percakapan umum.

## Engine Manager Integration

Seluruh engine Sprint 2 telah diintegrasikan ke `EngineManager`.

Engine yang dikelola:

```text
ProfileEngine
MemoryEngine
GoalEngine
PlannerEngine
DecisionEngine
KnowledgeEngine
ConversationEngine
```

EngineManager memproses pesan secara berurutan dan mengembalikan respons dari engine pertama yang menangani pesan tersebut.

ConversationEngine berada di bagian akhir daftar engine sehingga percakapan umum dapat menjadi fallback setelah engine khusus tidak menangani pesan.

## Testing

Sprint 2 menambahkan unit test dan integration test untuk komponen baru.

Test yang telah diverifikasi:

* PlannerEngine
* PlannerService
* Planner integration
* DecisionEngine
* KnowledgeEngine
* ConversationEngine
* EngineManager integration

Final regression test:

```text
50 passed
```

Seluruh test suite berhasil dijalankan tanpa regression setelah integrasi EngineManager.

## Architecture

Arsitektur Sprint 2 tetap mengikuti pemisahan tanggung jawab AURA:

```text
User
 │
 ▼
EngineManager
 │
 ├── ProfileEngine
 ├── MemoryEngine
 ├── GoalEngine
 ├── PlannerEngine
 │      │
 │      ▼
 │   PlannerService
 │      │
 │      ▼
 │   plans.py
 │      │
 │      ▼
 │    SQLite
 │
 ├── DecisionEngine
 ├── KnowledgeEngine
 └── ConversationEngine
```

Engine tidak mengakses database secara langsung.

Jika sebuah fitur membutuhkan persistence, akses database dilakukan melalui Service Layer.

## Sprint 2 Checklist

* [x] PlannerIntent
* [x] PlannerEngine
* [x] PlannerService
* [x] Planner database
* [x] Planner unit tests
* [x] Planner integration test
* [x] DecisionIntent
* [x] DecisionEngine
* [x] Decision unit tests
* [x] KnowledgeIntent
* [x] KnowledgeEngine
* [x] Knowledge unit tests
* [x] ConversationIntent
* [x] ConversationEngine
* [x] Conversation unit tests
* [x] EngineManager integration
* [x] Full regression test

## Sprint 2 Result

Sprint 2 berhasil memperluas kemampuan AURA dengan empat kemampuan baru:

```text
Planning
Decision Making
Knowledge
Conversation
```

Seluruh komponen yang telah diimplementasikan berhasil melewati test suite dengan hasil:

```text
50 passed
```

Sprint 2 siap memasuki tahap finalisasi berupa pembaruan changelog, roadmap, Git commit, dan Sprint 2 Git tag.
