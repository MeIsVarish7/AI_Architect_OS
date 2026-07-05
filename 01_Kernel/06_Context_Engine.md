# Context Engine

## Purpose

The Context Engine is responsible for reconstructing my current learning state before every learning session.

Its purpose is to provide any AI with sufficient context so that it can immediately continue my learning journey without unnecessary questioning.

The Context Engine generates a Dynamic Session Prompt based on the current state of AI Architect OS.

---

## Primary Mission

Understand my current state and generate the most relevant context for the next learning session.

The Context Engine should minimize unnecessary questions by using the information already available inside AI Architect OS.

---

## Responsibilities

The Context Engine must:

- Read the current state of AI Architect OS.
- Determine where I last stopped.
- Identify unfinished work.
- Determine the next logical topic.
- Understand active projects.
- Understand current research stage.
- Understand available study time.
- Generate a Dynamic Session Prompt.

---

## Inputs

The Context Engine may read information from:

- North Star
- Kernel
- Curriculum
- Daily Context
- Weekly Planner
- Monthly Planner
- Projects Dashboard
- Research Dashboard
- GitHub Dashboard
- BlackBook
- Reviews Dashboard
- Resources Dashboard
- End of Day Review

Each file provides part of the overall context.

---

## Context Priority

When information conflicts, prioritize:

1. End of Day Review
2. Daily Context
3. Weekly Planner
4. Monthly Planner
5. Active Projects
6. Research Status
7. Curriculum
8. Kernel

More recent information has higher priority than older planning.

---

## State Reconstruction

Before generating a session, determine:

- Current Sprint
- Current Curriculum Domain
- Current Level
- Current Topic
- Last Completed Topic
- Current Project
- Current Research Stage
- Current Priorities
- Available Time
- Current Constraints

The Context Engine should infer as much as possible without asking the user.

---

## Dynamic Session Prompt

The output of the Context Engine is a Dynamic Session Prompt.

The prompt should contain only information required for the next learning session.

It should avoid unnecessary repetition.

It should always begin from the user's latest confirmed learning state.

---

## Question Strategy

The Context Engine should only ask questions when required.

Questions should only be asked if the necessary information cannot be reconstructed from AI Architect OS.

Typical examples include:

- Available study time today.
- Unexpected interruptions.
- Newly introduced projects.
- Changes to long-term goals.

Avoid asking for information that already exists inside the Operating System.

---

## Adaptability

Every generated session should adapt to:

- Available time.
- Current competency.
- Active priorities.
- Current projects.
- Long-term objectives.

No two session prompts are expected to be identical.

---

## Constraints

The Context Engine should never:

- Restart completed topics.
- Ignore unfinished work.
- Skip curriculum dependencies.
- Recommend duplicate work.
- Lose learning continuity.
- Generate unnecessary context.

---

## Success Criteria

A successful Context Engine should allow any capable AI to:

- Understand my current learning state.
- Continue from my last completed topic.
- Generate an adaptive learning session.
- Minimize unnecessary questions.
- Preserve long-term continuity.