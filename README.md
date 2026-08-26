# Study Mentor 🎓

[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/ahanafy41/study-mentor/releases/tag/v1.0.0)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub Actions CI](https://github.com/ahanafy41/study-mentor/actions/workflows/validate-skill.yml/badge.svg)](https://github.com/ahanafy41/study-mentor/actions/workflows/validate-skill.yml)
[![Release Workflow](https://github.com/ahanafy41/study-mentor/actions/workflows/release.yml/badge.svg)](https://github.com/ahanafy41/study-mentor/actions/workflows/release.yml)

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
- 🚀 **GitHub Actions Automated Pipeline**: Built-in CI/CD for skill validation, release packaging, and tag-triggered GitHub Releases.

---

## 📂 Repository Structure / هيكل المستودع

```text
ahanafy41/study-mentor/
├── .github/
│   └── workflows/
│       ├── release.yml           # Automated release workflow (v1.0.0+)
│       └── validate-skill.yml    # CI workflow for SKILL validation & linting
├── templates/                    # Workspace scaffolding templates
│   ├── roadmap_template.md       # Syllabus & module tracker template
│   ├── progress_template.md      # Session log & active recall tracker template
│   ├── concepts_template.md      # Master glossary & concepts index template
│   ├── lecture_template.md       # Exhaustive lecture note blueprint
│   └── exercise_template.md      # Tiered exercises & lab drill template
├── AGENT_GUIDE.md                # In-depth execution guide for AI agents
├── LICENSE                       # MIT License
├── README.md                     # Main project documentation & connection to SKILL.md
└── SKILL.md                      # Core Skill definition file
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
   Import `SKILL.md` into your agent environment or skills registry.

3. **Triggering the Mentor**:
   Start a learning session with a prompt like:
   - *"Teach me Python asynchronous programming from scratch for an adult software engineer."*
   - *"Build a 4-week Islamic History curriculum about the Abbasid Golden Age for high school students."*
   - *"Create lecture notes and exercises for Linear Algebra Eigenvalues based on MIT 18.06."*

---

## 🤖 GitHub Actions CI/CD Pipeline

This repository includes two GitHub Actions workflows:

1. **[validate-skill.yml](.github/workflows/validate-skill.yml)**: Validates YAML frontmatter, Markdown formatting, and template file integrity on every push and pull request.
2. **[release.yml](.github/workflows/release.yml)**: Automatically packages the release archive (`study-mentor-v1.0.0.zip`), extracts changelogs, and creates a tagged GitHub Release when a tag like `v1.0.0` is pushed.

---

## 📜 Version History / سجل الإصدارات

- **v1.0.0** (2026-08-26):
  - Initial public release of the **Study Mentor** skill package.
  - Complete integration of age-adaptive pedagogical frameworks and Feynman analogies.
  - Modular workspace scaffold templates (`roadmap`, `progress`, `concepts`, `lectures`, `exercises`).
  - Automated GitHub Actions release and verification workflows.

---

## 📄 License / الترخيص

This project is licensed under the [MIT License](LICENSE) - see the [LICENSE](LICENSE) file for details.

Developed with ❤️ by [Ahmed Hanafy](https://github.com/ahanafy41).
