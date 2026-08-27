# Study Mentor (v1.1)

Universal pedagogical mentor and curriculum architect across all disciplines, optimized for **Google Antigravity 2.0** and the **Google AI Agent ecosystem**.

## Overview

`study-mentor` transforms any subject—across programming, natural sciences, history, languages, religious studies, and humanities—into a deeply structured, comprehensive, file-backed curriculum. Powered by **mandatory multi-branch subagent delegation**, **age-adaptive pedagogy**, and **file-backed active recall**.

---

## Directory Structure

```text
skills/study-mentor/
├── SKILL.md                               # Core execution protocol & frontmatter metadata
├── scripts/
│   └── scaffold_curriculum.py             # Automatic workspace initializer for learn_<topic>/
└── references/
    └── pedagogy_and_evaluation.md         # Feynman techniques, Bloom's Taxonomy & Spaced Repetition
```

---

## Installation & Setup

### For Google Antigravity 2.0 / Gemini Agents:
- **Global Scope**:
  Clone or place this skill directory into `~/.gemini/config/skills/study-mentor/`
- **Project/Workspace Scope**:
  Place into `<project-root>/.agents/skills/study-mentor/`

---

## Usage

You can trigger the skill via slash command or natural prompt:
- `/study-mentor`
- `/study-mentor C# Programming`
- "Build a 4-week structured curriculum for ancient Egyptian history with Feynman explanations and labs"

---

## Workspace Structure Created by Skill

When initialized, the mentor creates:
```text
learn_<topic_name>/
├── roadmap.md            # Comprehensive syllabus & 80/20 mastery path
├── progress.md           # Session logs & spaced repetition intervals
├── concepts.md           # Central glossary & Feynman mental models
├── lectures/             # Exhaustive, deep-dive lecture notes
├── sources/              # Verified source snapshots & citations
└── exercises/            # Hands-on labs & multi-tier MCQs
```
