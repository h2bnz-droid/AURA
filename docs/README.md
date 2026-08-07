# AURA

> **A Personal AI Operating System**

AURA (Adaptive Unified Reasoning Assistant) adalah AI yang dirancang untuk berkembang bersama satu pengguna.

Berbeda dengan chatbot tradisional yang berfokus pada percakapan, AURA dibangun untuk memahami, mengingat, membantu merencanakan, dan mendukung pertumbuhan pengguna dari waktu ke waktu.

---

## What makes AURA different?

Most AI assistants are designed to answer questions.

AURA is designed to understand one person.

Instead of only generating responses, AURA continuously builds knowledge about its user through memory, goals, and reflection, allowing it to provide long-term assistance rather than isolated conversations.

## Vision

Membangun AI Companion yang mampu:

- Mengingat informasi penting.
- Memahami tujuan pengguna.
- Membantu melakukan refleksi.
- Merencanakan langkah berikutnya.
- Menjadi partner jangka panjang.

---

## Current Features

### Core

- Modular Architecture
- Router
- Engine Manager
- BaseEngine
- Domain Layer

### Engines

- Profile Engine
- Memory Engine
- Goal Engine
- Reflection Engine

### Services

- Profile Service
- Memory Service
- Goal Service
- Reflection Service

### Database

- SQLite Storage
- Persistent Memory
- Goal Storage
- Reflection Storage

---

## Project Structure

```text
AURA
├── core
│   ├── domain
│   ├── engines
│   ├── manager
│   └── router
│
├── services
├── database
├── tests
├── docs
└── main.py
```

---

## Architecture

```text
User
   │
   ▼
Router
   │
   ▼
Engine Manager
   │
   ├── Profile Engine
   ├── Memory Engine
   ├── Goal Engine
   └── Reflection Engine
           │
           ▼
        Services
           │
           ▼
        SQLite
```

---

## Design Principles

- Modular Architecture
- Single Responsibility Principle
- Separation of Concerns
- Service Layer Pattern
- Testable Components

---

## Roadmap

### Sprint 1 ✅

- Foundation Architecture
- Core Engines
- Service Layer
- Database Layer
- Documentation

### Sprint 2

- Planner Engine
- Decision Engine
- Knowledge Engine
- Conversation Engine

### Sprint 3

- Emotion Engine
- Learning Engine
- Security Engine

---

## Technology

- Python
- SQLite
- Ollama
- Git
- VS Code

---

## Documentation

- `docs/architecture.md`
- `docs/philosophy.md`
- `CHANGELOG.md`

---

## License

This project is currently under active development.
License information will be added before the first stable release.

---

## Author

Developed by the AURA Project.
