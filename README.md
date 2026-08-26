# Study Mentor 🎓

[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/ahanafy41/study-mentor)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **Universal pedagogical mentor and curriculum architect across all disciplines with age-adaptive pedagogy, structured lecture notes, verified exercises, and active recall tracking.**
>
> **مرشد وبوصلة تعليمية شاملة ومصمم مناهج دراسية متقدم عبر كافة العلوم والتخصصات، يعتمد على التدريس المتكيف مع الفئات العمرية والتوثيق والتقييم المستمر.**

---

## 🌟 Overview / نظرة عامة

**Study Mentor** is an autonomous, cross-disciplinary pedagogical learning mentor and curriculum architect designed for AI agents and LLM platforms. Powered by **mandatory multi-branch subagent delegation** and **age-adaptive pedagogy**, it transforms any subject—from programming and computer science to history, natural sciences, mathematics, languages, literature, and religious studies—into a deeply structured, comprehensive, file-backed learning journey.

### 🎯 Key Highlights / أبرز المميزات

- 🌍 **Universal Discipline Coverage**: Operates across technical stacks, humanities, natural sciences, religious studies, languages, and business.
- 👶🧑‍🎓👨‍💼 **Age-Adaptive Pedagogy**: Calibrates explanation style, Feynman analogies, conceptual depth, and pacing to match the target age and experience level.
- ⚡ **Mandatory Multi-Branch Subagent Architecture**: Enforces parallel subagent delegation for research, lecture writing, source verification, and exercise creation.
- 📁 **File-Backed Workspace Persistence**: Organizes every study topic into a structured `learn_<topic_name>/` folder with syllabi, deep lectures, glossaries, and active recall schedules.
- 🔄 **Socratic Active Recall & Spaced Repetition**: Integrates interactive review intervals (24h, 3d, 1w) to guarantee long-term knowledge retention.

---

## 📂 Repository Structure / هيكل المستودع

```text
ahanafy41/study-mentor/
├── LICENSE          # MIT License
├── README.md        # Documentation & connection to SKILL.md
└── SKILL.md         # Core Skill definition file
```

---

## 🧠 Core Skill Architecture / البنية المعمارية للمهارة

For full technical specifications and instructions, refer directly to [SKILL.md](SKILL.md).

### 1. Workspace Directory Layout (`learn_<topic_name>/`)

When Study Mentor initiates a course, it creates a dedicated directory structure:

```text
learn_<topic_name>/
├── roadmap.md            # Comprehensive syllabus, module status, and mastery roadmap
├── progress.md           # Session logs, active recall intervals, and knowledge gaps
├── concepts.md           # Central glossary and index linking concepts to lectures
├── lectures/             # Exhaustive, deep-dive lecture notes (never superficial)
│   ├── 01_topic_fundamentals.md
│   └── ...
├── sources/              # Verified source snapshots, official citations, and transcript analyses
│   ├── official_sources_snapshot.md
│   └── reference_notes.md
└── exercises/            # Hands-on labs, problem sets, MCQs with rationales, and case studies
    ├── lab_01/
    │   └── questions_and_drills.md
    └── notes.md
```

### 2. Multi-Branch Subagent Delegation Matrix

| Subagent Role | Purpose |
| :--- | :--- |
| **Core Theory & First-Principles** | Derives foundational definitions, axioms, mechanisms, and Feynman analogies. |
| **Context, Chronology & In-Depth Mechanics** | Explores history, architecture, causality chains, and comparative tables. |
| **Source Verification Sentinel** | Live web/documentation lookups against official sources and textbooks. |
| **Curriculum Lab & Deliberate Practice** | Formulates multi-tiered MCQs, rubrics, coding drills, and case studies. |
| **Media & Video Ingestion** | Ingests and timestamps video/playlist transcripts into source notes. |

---

## 🚀 Getting Started / دليل البدء السريع

### Installation into Gemini / AI Agent Environments

1. **Clone or Download**:
   ```bash
   git clone https://github.com/ahanafy41/study-mentor.git
   ```

2. **Load the Skill**:
   Import [SKILL.md](SKILL.md) into your agent environment or skills registry.

3. **Triggering the Mentor**:
   Start a learning session with a prompt like:
   - *"Teach me Python asynchronous programming from scratch for an adult software engineer."*
   - *"Build a 4-week Islamic History curriculum about the Abbasid Golden Age for high school students."*
   - *"Create lecture notes and exercises for Linear Algebra Eigenvalues based on MIT 18.06."*

---

## 📜 Version History / سجل الإصدارات

- **v1.0.0** (2026-08-26):
  - Official release of the **Study Mentor** skill.
  - Complete integration of age-adaptive pedagogical frameworks and Feynman analogies.
  - Modular workspace scaffold architecture (`roadmap`, `progress`, `concepts`, `lectures`, `exercises`).

---

## 📄 License / الترخيص

This project is licensed under the [MIT License](LICENSE) - see the [LICENSE](LICENSE) file for details.

Developed by [Ahmed Hanafy](https://github.com/ahanafy41).
