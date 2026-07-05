# OS Controller

## Purpose

The OS Controller is the orchestration layer of AI Architect OS.

It coordinates every component of the Operating System during a learning session.

The OS Controller does not teach.

It does not generate prompts.

It does not store knowledge.

Its only responsibility is to execute the Operating System in the correct order.

---

## Primary Mission

Manage the complete lifecycle of every AI learning session from startup to shutdown.

---

## Responsibilities

The OS Controller must:

- Start a new learning session.
- Invoke the Runtime Engine.
- Invoke the Context Engine.
- Invoke the Dynamic Prompt Generator.
- Launch the AI learning session.
- Receive the Session Update.
- Update AI Architect OS.
- Prepare the next session.

---

## Session Lifecycle

Every learning session follows this sequence:

1. User starts AI Architect OS.
2. Load Runtime Engine.
3. Invoke Context Engine.
4. Reconstruct Current State.
5. Invoke Dynamic Prompt Generator.
6. Generate Dynamic Session Prompt.
7. Launch AI Session.
8. Receive Session Update.
9. Update Operating System.
10. End Session.

---

## Startup

At session startup the OS Controller should:

- Read the Runtime Engine.
- Ensure the Operating System is available.
- Begin state reconstruction.
- Minimize unnecessary user interaction.

---

## Runtime Coordination

The OS Controller delegates responsibilities.

Runtime Engine

↓

Context Engine

↓

Dynamic Prompt Generator

↓

AI Learning Session

↓

Session Update

The OS Controller should never perform these responsibilities itself.

---

## User Interaction

The OS Controller should ask the user only for information that cannot be reconstructed automatically.

Typical examples include:

- Available study time.
- New personal constraints.
- New long-term goals.

Everything else should be reconstructed from AI Architect OS.

---

## Session Shutdown

At the end of every session the OS Controller should:

- Receive the Session Update.
- Confirm it with the user.
- Update AI Architect OS.
- Preserve learning continuity.
- Prepare the next session.

---

## Design Principles

The OS Controller should:

- Orchestrate.
- Delegate.
- Coordinate.

It should never:

- Teach.
- Mentor.
- Generate prompts.
- Verify competency.
- Make curriculum decisions.

Those responsibilities belong to other Kernel components.

---

## Constraints

The OS Controller should never:

- Duplicate responsibilities.
- Break learning continuity.
- Skip required execution stages.
- Depend on a specific AI model.

---

## Success Criteria

A successful OS Controller should coordinate every learning session while allowing each Kernel component to perform its own specialized responsibility.