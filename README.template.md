# 🚀 JobFlow AI

Automated AI-powered job discovery and filtering system.

## 🔥 Features
- Multi-source job scraping (Greenhouse, Lever)
- AI-powered filtering & scoring
- Smart model routing (OpenRouter)
- Resume + cover letter generation
- Fully automated pipeline

## ⚙️ Tech Stack
- Python 3.12
- OpenRouter (LLMs)
- Flask (API)
- VPS (Ubuntu)

## 📊 Pipeline
Discovery → Normalize → Filter → Score → Output

## 🚀 Usage

```bash
python3 main.py

🧠 AI Models
Fast: lightweight models
Balanced: LLaMA / Mistral
Smart: GPT-level reasoning
🔐 Security
.env protected
Public repo sanitized automatically
📦 Version

VERSION_PLACEHOLDER


---

# ⚡ STEP 2 — CREATE VERSION FILE

```bash
echo "0.1.0" > ~/projects/jobflow/VERSION

🔥 STEP 3 — UPGRADE sync.sh (FINAL PRO VERSION)

Replace your sync.sh with this:

#!/bin/bash

echo "🚀 Starting PRO SYNC..."

PROJECT_DIR=~/projects/jobflow
TMP_DIR="/tmp/jobflow_public"

cd $PROJECT_DIR || exit

# =========================
# STEP 1: VERSION BUMP
# =========================
VERSION=$(cat VERSION)

IFS='.' read -r MAJOR MINOR PATCH <<< "$VERSION"
PATCH=$((PATCH + 1))

NEW_VERSION="$MAJOR.$MINOR.$PATCH"
echo $NEW_VERSION > VERSION

echo "📦 New Version: v$NEW_VERSION"

# =========================
# STEP 2: GENERATE README
# =========================
echo "📝 Generating README..."

sed "s/VERSION_PLACEHOLDER/v$NEW_VERSION/g" README.template.md > README.md

# =========================
# STEP 3: PUSH PRIVATE
# =========================
echo "🔒 Pushing to PRIVATE repo..."

git add .
git commit -m "Auto sync v$NEW_VERSION" || echo "No changes"
git tag "v$NEW_VERSION"
git push origin main --tags

# =========================
# STEP 4: CLEAN PUBLIC COPY
# =========================
echo "🧹 Creating CLEAN public version..."

rm -rf $TMP_DIR
mkdir -p $TMP_DIR

rsync -av --exclude='.git' \
           --exclude='.env' \
           --exclude='venv' \
           --exclude='__pycache__' \
           --exclude='logs' \
           --exclude='outputs' \
           --exclude='.backup_sync' \
           ./ $TMP_DIR

cd $TMP_DIR || exit

# =========================
# STEP 5: PUSH PUBLIC
# =========================
git init
git remote add origin $(git -C $PROJECT_DIR remote get-url public)

git add .
git commit -m "Public release v$NEW_VERSION"
git branch -M main
git push -f origin main

echo "🌍 Public repo updated: v$NEW_VERSION"

# =========================
# DONE
# =========================
echo "✅ PRO SYNC COMPLETE!"
