#!/bin/bash

echo "🚀 Starting PRO SYNC..."

PROJECT_DIR=~/projects/jobflow
TMP_DIR="/tmp/jobflow_public"

cd $PROJECT_DIR || exit

# =========================
# STEP 1: VERSION BUMP (SAFE)
# =========================
if [ ! -f VERSION ]; then
    echo "0.1.0" > VERSION
fi

VERSION=$(cat VERSION)

IFS='.' read -r MAJOR MINOR PATCH <<< "$VERSION"

# fallback safety
MAJOR=${MAJOR:-0}
MINOR=${MINOR:-1}
PATCH=${PATCH:-0}

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
