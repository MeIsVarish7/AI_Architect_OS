# Architecture

This folder contains permanent architectural decisions of AI Architect OS.

It does NOT explain implementation details.

It explains how the major systems connect and why they exist.

Future AIs should understand this folder before modifying any core component.

---

# High Level Architecture

AI Architect OS is divided into independent systems.

Kernel
↓
Context Engine
↓
Runtime Engine
↓
Curriculum
↓
Planner
↓
Session Controller
↓
Reviews
↓
State Update

Each system has a single responsibility.

---

# Architecture Philosophy

The architecture is intentionally modular.

Every major system should solve one problem only.

Modules communicate with each other instead of containing each other's logic.

---

# Frozen Architecture

Unless the user explicitly changes the design:

Do not redesign architecture.

Improve implementation while preserving architecture.

---

# Current Permanent Decisions

• Runtime provides contextual information (time, energy, weekday).

• Planner decides WHAT to study.

• Timetable Builder decides HOW lessons fit into the available time.

• Session Controller executes today's study session.

• Curriculum owns lesson information.

The planner must never own curriculum data.

---

# Responsibility Separation

Kernel
Stores project philosophy.

Context Engine
Loads permanent knowledge.

Runtime
Collects today's information.

Planner
Creates today's learning strategy.

Timetable Builder
Creates today's timetable.

Session Controller
Runs today's session.

Reviews
Updates long-term progress.

---

This document should only contain architecture that remains useful across multiple sprints.