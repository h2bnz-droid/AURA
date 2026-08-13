# AURA Roadmap

## Vision

AURA dikembangkan sebagai AI Companion dengan arsitektur modular yang dapat berkembang dari sistem assistant dasar menuju sistem cognitive assistant yang lebih mampu memahami konteks, tujuan, keputusan, pengetahuan, dan perkembangan pengguna.

---

## Milestone 1 — Foundation

**Status:** Completed

Milestone pertama berfokus pada pembangunan fondasi arsitektur AURA.

### Architecture

* [x] Modular project structure
* [x] BaseEngine
* [x] Engine architecture
* [x] Engine Manager
* [x] Router architecture
* [x] Domain layer
* [x] Service layer
* [x] Database layer

### Core Systems

* [x] AuraKernel
* [x] AI Provider
* [x] Prompt Builder
* [x] Context Builder
* [x] Conversation History

### Foundation Engines

* [x] ProfileEngine
* [x] MemoryEngine
* [x] GoalEngine
* [x] ReflectionEngine

### Persistence

* [x] Profile database
* [x] Memory database
* [x] Goal database
* [x] Reflection database

### Quality

* [x] Type hints
* [x] Unit tests
* [x] Engine consistency
* [x] Architecture documentation

---

## Milestone 2 — Intelligence Expansion

**Status:** Completed

Milestone kedua memperluas kemampuan AURA dengan sistem perencanaan, pengambilan keputusan, pengetahuan, dan percakapan.

### Planner

* [x] PlannerIntent
* [x] PlannerEngine
* [x] PlannerService
* [x] Planner database
* [x] Plan persistence
* [x] Planner unit tests
* [x] Planner integration test

### Decision

* [x] DecisionIntent
* [x] DecisionEngine
* [x] Decision unit tests

### Knowledge

* [x] KnowledgeIntent
* [x] KnowledgeEngine
* [x] Knowledge unit tests
* [x] Search query extraction
* [x] Explanation query extraction

### Conversation

* [x] ConversationIntent
* [x] ConversationEngine
* [x] Greeting handling
* [x] General conversation fallback
* [x] Conversation unit tests

### Integration

* [x] Sprint 2 engines integrated into EngineManager
* [x] Engine Manager integration tests
* [x] Full regression testing

### Result

Sprint 2 selesai dengan:

```text
50 passed
```

---

---

## Milestone 3 — Cognitive Systems

**Status:** Planned

Milestone ketiga berfokus pada pengembangan kemampuan kognitif AURA yang lebih dalam.

### Sprint 3 — Context Intelligence

**Status:** Completed

Sprint ketiga berfokus pada pembangunan contextual intelligence layer yang menghubungkan input pengguna, memory retrieval, context construction, prompt generation, dan AI pipeline.

### Context

* [x] AuraContext
* [x] Context Builder
* [x] Profile context
* [x] Recent conversation context
* [x] Current user message context

### Memory Retrieval

* [x] Dedicated MemoryRetrieval
* [x] Memory normalization
* [x] Keyword-based retrieval
* [x] Memory deduplication
* [x] Memory relevance scoring
* [x] Memory ranking
* [x] Maximum memory result limit

### Prompt Pipeline

* [x] Context-to-prompt integration
* [x] Profile prompt section
* [x] Memory prompt section
* [x] Recent conversation prompt section
* [x] Current user message section
* [x] Empty context handling

## Integration*

* [x] Chat pipeline integration
* [x] Router integration
* [x] Context/prompt integration
* [x] Full pipeline integration

## Quality*

* [x] Context Builder tests
* [x] Memory Retrieval tests
* [x] Prompt Builder tests
* [x] Chat tests
* [x] Router tests
* [x] Integration tests
* [x] Full regression testing

````markdown
### Result

Sprint 3 selesai dengan:

```text
82 passed
```

## Milestone 4 — Personal Cognitive Assistant

## Status: planned

Milestone keempat berfokus pada integrasi kemampuan AURA menjadi sistem personal cognitive assistant yang lebih utuh.

### Planned Capabilities

* [ ] Long-term context management
* [ ] Cross-engine context sharing
* [ ] Adaptive planning
* [ ] Decision support
* [ ] Personal knowledge management
* [ ] Learning from user interactions
* [ ] Improved personalization

---

## Milestone 5 — AURA Maturity

## Status: release

Milestone akhir berfokus pada stabilitas, keamanan, observability, dan kesiapan AURA sebagai platform cognitive assistant.

### Planned Areas

* [ ] Security hardening
* [ ] Reliability improvements
* [ ] Performance optimization
* [ ] Observability
* [ ] Advanced testing
* [ ] Documentation completion
* [ ] Stable release process

---

## Current Progress

```text
Milestone 1 — Foundation
████████████████████ 100%

Milestone 2 — Intelligence Expansion
████████████████████ 100%

Milestone 3 — Cognitive Systems
░░░░░░░░░░░░░░░░░░░░   0%

Milestone 4 — Personal Cognitive Assistant
░░░░░░░░░░░░░░░░░░░░   0%

Milestone 5 — AURA Maturity
░░░░░░░░░░░░░░░░░░░░   0%
```

## Release History

| Release | Milestone              | Status    |
| ------- | ---------------------- | --------- |
| v0.1.0  | Foundation             | Completed |
| v0.2.0  | Intelligence Expansion | Completed |
| v0.3.0  | Context Intelligence   | Completed |

## Development Principle

Setiap milestone harus mempertahankan prinsip arsitektur AURA:

* Modular architecture
* Single Responsibility
* Separation of Concerns
* Consistent Engine contract
* Service Layer separation
* Database abstraction
* Test-driven verification

Perubahan besar pada arsitektur harus didukung oleh test dan dokumentasi sebelum milestone dianggap selesai.
