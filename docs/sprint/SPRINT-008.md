# Sprint 008 — Relationship Awareness

## Status: Planned

Sprint kedelapan berfokus pada pembangunan dasar Relationship Awareness AURA.

Sprint ini membuat AURA mampu mengenali relationship sederhana dari input pengguna, menyimpan relationship, mengambil relationship yang tersimpan, memperbarui relationship, dan menyediakan relationship context untuk pipeline AURA.

Sistem awal bersifat structured dan rule-based. Sprint ini tidak bertujuan membangun social graph atau autonomous relationship analysis.

---

## Objective

Membangun Relationship System yang:

- [ ] menerima relationship dari pengguna
- [ ] menentukan intent relationship
- [ ] menyimpan relationship
- [ ] mengambil relationship
- [ ] memperbarui relationship
- [ ] menyediakan relationship context
- [ ] mengintegrasikan RelationshipEngine
- [ ] mempertahankan kontrak Engine, Service, dan Database

---

## Domain

### RelationshipIntent

- [ ] RelationshipIntent
- [ ] CREATE intent
- [ ] SHOW intent
- [ ] UPDATE intent
- [ ] UNKNOWN intent

---

## Relationship Data

Relationship awal memiliki:

- [ ] person_name
- [ ] relationship_type
- [ ] status
- [ ] note
- [ ] created_at
- [ ] updated_at

Relationship type awal:

- [ ] friend
- [ ] family
- [ ] mother
- [ ] father
- [ ] sibling
- [ ] partner
- [ ] colleague
- [ ] other

---

## Relationship Database

### Table: relationships

Database layer:

- [ ] create_table
- [ ] save_relationship
- [ ] get_relationship
- [ ] get_all_relationships
- [ ] update_relationship

RelationshipEngine tidak boleh mengakses database secara langsung.

---

## RelationshipService

- [ ] RelationshipService
- [ ] save relationship
- [ ] get relationship
- [ ] get all relationships
- [ ] update relationship
- [ ] relationship normalization

RelationshipService menjadi abstraction layer antara RelationshipEngine dan database.

---

## RelationshipEngine

- [ ] RelationshipEngine
- [ ] BaseEngine compliance
- [ ] message analysis
- [ ] relationship creation
- [ ] relationship retrieval
- [ ] relationship update
- [ ] unknown handling

RelationshipEngine bertanggung jawab terhadap reasoning tingkat engine.

---

## Context Integration

Relationship data masuk ke `AuraContext`.

- [ ] Relationship context model
- [ ] Relationship retrieval
- [ ] Context Builder integration
- [ ] Empty relationship handling

Relationship context tidak boleh menggantikan:

- Profile
- Memory
- Emotion
- Temporal
- Reflection
- Conversation History

---

## Prompt Integration

- [ ] Relationship prompt section
- [ ] Relationship context formatting
- [ ] Empty relationship handling
- [ ] Prompt ordering verification

Target context:

PROFILE
MEMORY
EMOTION
TEMPORAL
REFLECTION
RELATIONSHIP
RECENT CONVERSATION
CURRENT USER MESSAGE

---

## Engine Integration

- [ ] RelationshipEngine integrated into EngineManager
- [ ] Engine priority verification
- [ ] Conversation fallback compatibility
- [ ] Regression against existing engines

RelationshipEngine tidak boleh mengambil alih input yang lebih spesifik dari:

- ProfileEngine
- MemoryEngine
- GoalEngine
- PlannerEngine
- DecisionEngine
- KnowledgeEngine
- LearningEngine
- EmotionEngine
- TemporalEngine
- ReflectionEngine

ConversationEngine tetap menjadi fallback.

---

## Testing

### Unit Tests

- [ ] RelationshipIntent tests
- [ ] Relationship database tests
- [ ] RelationshipService tests
- [ ] RelationshipEngine tests

### Integration Tests

- [ ] RelationshipEngine + RelationshipService
- [ ] Relationship + EngineManager
- [ ] Relationship + Context Builder
- [ ] Relationship + Prompt Builder
- [ ] Relationship + Chat pipeline

### Regression

- [ ] Full regression testing
- [ ] Existing tests remain passing

---

## Quality

- [ ] Type hints
- [ ] Engine contract consistency
- [ ] Service layer separation
- [ ] Database abstraction
- [ ] No direct database access from Engine
- [ ] No duplicated business logic
- [ ] Test coverage
- [ ] Documentation

---

## Acceptance Criteria

Sprint 8 dianggap selesai apabila:

1. RelationshipIntent dapat membedakan intent relationship.
2. RelationshipEngine dapat memproses relationship input.
3. RelationshipEngine menggunakan RelationshipService.
4. RelationshipService menggunakan database abstraction.
5. Relationship dapat disimpan.
6. Relationship dapat diambil.
7. Relationship dapat diperbarui.
8. Relationship context masuk ke Context Builder.
9. Relationship context masuk ke Prompt Builder.
10. RelationshipEngine terintegrasi dengan EngineManager.
11. ConversationEngine tetap menjadi fallback.
12. Full regression tidak mengalami failure.
13. Dokumentasi Sprint 8 selesai.

---

## Result

Sprint 8 belum dimulai.

Target regression:

159+ passed
0 failed
0 errors
