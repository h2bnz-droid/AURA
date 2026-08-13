# Sprint 3 — Context Intelligence

## Overview

Sprint 3 focuses on strengthening AURA's contextual intelligence pipeline.

The sprint introduces a dedicated memory retrieval layer and improves the flow from user input to contextual prompt generation.

## Goals

- Build a dedicated memory retrieval system.
- Improve contextual memory relevance.
- Integrate memory retrieval into context construction.
- Strengthen prompt generation.
- Improve router and AI pipeline integration.
- Expand automated test coverage.

## Implemented

### Context Builder

`ContextBuilder` now builds an `AuraContext` containing:

- User input
- User profile
- Relevant memories
- Recent conversation history

Conversation history is limited to the latest 6 entries.

### Memory Retrieval

A dedicated `MemoryRetrieval` component was introduced.

The retrieval pipeline:

1. Normalize user input.
2. Extract searchable words.
3. Search stored memories.
4. Remove duplicate memories.
5. Score memories based on matching words.
6. Rank memories by relevance.
7. Ignore memories with zero relevance.
8. Limit retrieved memories to a maximum of 5.

### Prompt Builder

`PromptBuilder` converts `AuraContext` into the internal AURA prompt.

The prompt contains:

- Profile
- Memory
- Recent conversation
- Current user message

The section order is explicitly tested to preserve a consistent prompt structure.

### Router Integration

The router integrates the contextual AI pipeline with the existing:

- Engines
- Commands
- Skills
- AI fallback

### Chat Pipeline

The chat pipeline now verifies the complete flow:

```text
User Input
    ↓
Router
    ↓
AI Pipeline
    ↓
Context Builder
    ↓
Memory Retrieval
    ↓
AuraContext
    ↓
Prompt Builder
    ↓
AI Provider
    ↓
AURA Response
