# Planner

The Planner is the heart of AI Architect OS.

Its responsibility is NOT to generate a timetable.

Its responsibility is to decide what the user should learn today.

The Timetable Builder later converts this decision into an executable study plan.

---

# Purpose

The planner should think like an experienced mentor.

It should consider:

- Available time
- Energy
- Weekday
- Current priorities
- Long-term roadmap

before selecting today's subjects.

---

# Current Planner Inputs

Runtime provides:

- Available study time
- Energy level
- Weekday

Future versions may additionally use:

- Previous sessions
- Completion percentage
- Deadlines
- Exams
- Project milestones
- Internship preparation

---

# Subject Groups

## Core Subjects

Programming

DSA

AI

Mathematics

These receive the highest priority because they directly support the long-term roadmap.

---

## Secondary Subjects

Computer Science

Projects

Research

Systems Engineering

Communication

Industry

Life

These continue progressing without slowing the core roadmap.

---

# Planning Philosophy

The planner should never generate identical study days.

Instead, it rotates subjects naturally.

Example:

Programming + DSA

Programming + AI

DSA + Mathematics

Programming + Research

Programming + Projects

This keeps learning balanced while avoiding burnout.

---

# Weekday Behaviour

Monday – Thursday

Focus primarily on Core Subjects.

Friday – Sunday

Allow broader rotation including Secondary Subjects.

---

# Energy Behaviour

Low

2 focus areas.

Medium

Up to 3 focus areas.

High

Usually 3.

Occasionally 4 when appropriate.

---

# Time Behaviour

The planner should not attempt to fill every available minute.

A small intentional buffer should remain.

This reflects realistic human planning.

---

# Lesson Categories

Lessons belong to one of four categories.

Basic

Medium

Heavy

Project

These categories determine expected study duration.

The planner should derive lesson time from the category rather than assigning arbitrary durations to individual lessons.

Current categories:

Basic
20–35 minutes

Medium
35–60 minutes

Heavy
75–120 minutes

Project
120–180 minutes

These values may evolve through real usage.

---

# Future Planner Evolution

Future versions may include:

Adaptive planning

Completion-based weighting

Deadline awareness

Study history

Learning analytics

Habit awareness

Project awareness

The planner should evolve through real-world usage instead of assumptions.

---

The planner exists to make intelligent learning decisions.

It should feel like a mentor, not a random timetable generator.