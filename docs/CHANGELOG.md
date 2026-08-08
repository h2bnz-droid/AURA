# Changelog

## v0.2.0 — Intelligence Expansion

Release Date: 2026-08-08

### Added

#### Engines

* PlannerEngine
* DecisionEngine
* KnowledgeEngine
* ConversationEngine

#### Domain Intent System

* PlannerIntent
* DecisionIntent
* KnowledgeIntent
* ConversationIntent

#### Planner System

* Planner Service
* Planner Database
* Plan persistence
* Plan generation

#### Engine Integration

* Sprint 2 engines integrated into Engine Manager
* ConversationEngine fallback behavior

### Improved

* Expanded Engine Manager capabilities
* Consistent Engine architecture across Sprint 2 engines
* Consistent intent-based processing
* Planner persistence through Service and Database layers
* Query extraction and validation in KnowledgeEngine
* Engine integration testing
* Regression test coverage

### Testing

* PlannerEngine unit tests
* PlannerService unit tests
* Planner integration test
* DecisionEngine unit tests
* KnowledgeEngine unit tests
* ConversationEngine unit tests
* EngineManager integration tests
* Full regression test suite

Final test result:

```text
50 passed
```

### Documentation

* Sprint 2 documentation
* Sprint 2 architecture and integration notes

### Notes

This release expands AURA beyond its foundational architecture into additional cognitive capabilities.

Sprint 2 introduces planning, decision making, knowledge interaction, and general conversation while maintaining the modular Engine, Service, and Database architecture established in Sprint 1.
