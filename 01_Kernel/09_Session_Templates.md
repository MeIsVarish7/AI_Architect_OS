# Session Templates

## Purpose

Session Templates define the information required to generate different types of Dynamic Session Prompts.

They do not contain the final prompt.

Instead, they define the variables and structure required by the Dynamic Prompt Generator.

The final prompt should always adapt to the current learning state.

---

## Primary Mission

Provide standardized session structures that allow the Dynamic Prompt Generator to create context-aware learning sessions for any compatible AI.

---

## Session Philosophy

Every session should:

- Continue from the current learning state.
- Follow curriculum dependencies.
- Respect available study time.
- Avoid unnecessary repetition.
- Adapt to demonstrated competency.
- Preserve long-term learning continuity.

The Operating System provides context.

The Dynamic Prompt Generator builds the prompt.

The AI provides intelligence.

---

## Learning Session

Purpose:

Teach the next logical curriculum topic.

Required Variables:

- Current Curriculum Domain
- Current Level
- Current Topic
- Previous Session Summary
- Available Study Time
- Current Objective
- Teaching Strategy
- Competency Confidence
- Verification Strategy
- Expected Session Outcome

---

## Revision Session

Purpose:

Strengthen previously learned topics.

Required Variables:

- Revision Topics
- Weak Concepts
- Previous Mistakes
- Available Study Time
- Revision Objective
- Practice Strategy

---

## Project Session

Purpose:

Continue active engineering projects.

Required Variables:

- Current Project
- Current Milestone
- Current Blockers
- Current Objective
- Available Study Time

---

## Research Session

Purpose:

Continue active research.

Required Variables:

- Current Research Stage
- Current Paper
- Current Experiment
- Current Objective
- Available Study Time

Research sessions should only be generated when permitted by the Research Roadmap.

---

## Interview Session

Purpose:

Prepare for technical interviews.

Required Variables:

- Interview Domain
- Current Weak Areas
- Available Study Time
- Interview Objective
- Difficulty Level

---

## Debug Session

Purpose:

Solve implementation problems while improving engineering understanding.

Required Variables:

- Current Problem
- Error Description
- Expected Behaviour
- Current Understanding
- Debug Objective

The objective is learning rather than simply fixing code.

---

## Session Completion

Every session should finish by generating a Session Update.

The Session Update becomes the primary input for the next Dynamic Session Prompt.

---

## Constraints

Session Templates should never:

- Restart completed topics.
- Ignore previous progress.
- Skip curriculum dependencies.
- Generate unnecessary work.
- Lose learning continuity.
- Depend on a specific AI model.

---

## Relationship with Dynamic Prompt Generator

Session Templates do not generate prompts.

They define the variables, structure, and requirements used by the Dynamic Prompt Generator.

The Dynamic Prompt Generator combines these templates with the current Operating System state to produce a Dynamic Session Prompt.

---

## Success Criteria

A successful Session Template should enable the Dynamic Prompt Generator to create a learning session that allows any compatible AI to:

- Understand the current learning state.
- Continue from the previous session.
- Teach adaptively.
- Mentor effectively.
- Preserve learning continuity.
- Generate a useful Session Update.