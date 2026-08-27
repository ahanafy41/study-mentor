#!/usr/bin/env python3
import sys
import os
import re

def sanitize_topic_name(topic):
    topic = topic.strip().lower()
    topic = re.sub(r'[^\w\-_]+', '_', topic)
    return topic.strip('_')

def create_workspace(topic_raw):
    topic = sanitize_topic_name(topic_raw)
    base_dir = f"learn_{topic}"
    os.makedirs(os.path.join(base_dir, "lectures"), exist_ok=True)
    os.makedirs(os.path.join(base_dir, "sources"), exist_ok=True)
    os.makedirs(os.path.join(base_dir, "exercises", "lab_01"), exist_ok=True)

    roadmap_path = os.path.join(base_dir, "roadmap.md")
    if not os.path.exists(roadmap_path):
        with open(roadmap_path, "w", encoding="utf-8") as f:
            f.write(f"# Curriculum Roadmap: {topic_raw}\n\n## 1. Overview\n\n## 2. Core Modules\n- [ ] Module 1: Foundations\n- [ ] Module 2: Core Mechanics\n- [ ] Module 3: Advanced Applications\n\n## 3. 80/20 Mastery Path\n")

    progress_path = os.path.join(base_dir, "progress.md")
    if not os.path.exists(progress_path):
        with open(progress_path, "w", encoding="utf-8") as f:
            f.write(f"# Learning Progress: {topic_raw}\n\n## Session History\n| Date | Topic / Module | Mastery (1-5) | Next Spaced Repetition |\n|---|---|---|---|\n\n## Active Knowledge Gaps & Notes\n")

    concepts_path = os.path.join(base_dir, "concepts.md")
    if not os.path.exists(concepts_path):
        with open(concepts_path, "w", encoding="utf-8") as f:
            f.write(f"# Conceptual Index & Glossary: {topic_raw}\n\n| Concept | Core Intuition / Feynman Model | Reference Lecture |\n|---|---|---|\n")

    print(f"Successfully initialized workspace at: {base_dir}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 scaffold_curriculum.py <topic_name>")
        sys.exit(1)
    create_workspace(" ".join(sys.argv[1:]))
