# ai/client.py

import os
import json
import hashlib
import requests
from datetime import datetime

# =========================
# ENV CONFIG
# =========================
API_KEY = os.getenv("OPENROUTER_API_KEY")
BASE_URL = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")

FAST_MODEL = os.getenv("FAST_MODEL")
BALANCED_MODEL = os.getenv("BALANCED_MODEL")
SMART_MODEL = os.getenv("SMART_MODEL")

FALLBACK_MODEL_1 = os.getenv("FALLBACK_MODEL_1")
FALLBACK_MODEL_2 = os.getenv("FALLBACK_MODEL_2")

ENABLE_CACHE = os.getenv("ENABLE_CACHE", "true").lower() == "true"
CACHE_FILE = os.getenv("CACHE_FILE", "cache.json")
LOG_FILE = os.getenv("LOG_FILE", "logs/ai.log")

TIMEOUT = int(os.getenv("MODEL_TIMEOUT", 12))
MAX_RETRIES = int(os.getenv("MAX_RETRIES", 1))

# =========================
# LOGGING
# =========================
def log(message):
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} | {message}\n")


# =========================
# CACHE
# =========================
def hash_prompt(prompt):
    return hashlib.md5(prompt.encode()).hexdigest()


def load_cache():
    if not os.path.exists(CACHE_FILE):
        return {}
    with open(CACHE_FILE, "r") as f:
        return json.load(f)


def save_cache(cache):
    with open(CACHE_FILE, "w") as f:
        json.dump(cache, f, indent=2)


# =========================
# MODEL CALL
# =========================
def call_model(model, prompt):
    for attempt in range(MAX_RETRIES + 1):
        try:
            response = requests.post(
                f"{BASE_URL}/chat/completions",
                headers={
                    "Authorization": f"Bearer {API_KEY}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": model,
                    "messages": [{"role": "user", "content": prompt}]
                },
                timeout=TIMEOUT
            )

            data = response.json()

            if "choices" in data:
                output = data["choices"][0]["message"]["content"]
                log(f"SUCCESS | {model}")
                return output

            raise Exception(data)

        except Exception as e:
            log(f"ERROR | {model} | Attempt {attempt+1} | {e}")

    return None


# =========================
# MODEL ROUTING
# =========================
def get_model_chain(task_type):
    if task_type == "fast":
        return [FAST_MODEL, BALANCED_MODEL]

    elif task_type == "balanced":
        return [BALANCED_MODEL, SMART_MODEL]

    elif task_type == "smart":
        return [SMART_MODEL]

    return [BALANCED_MODEL]


# =========================
# MAIN GENERATOR
# =========================
def generate(prompt, task_type="balanced"):
    cache_key = hash_prompt(prompt)

    # =========================
    # CACHE CHECK
    # =========================
    if ENABLE_CACHE:
        cache = load_cache()
        if cache_key in cache:
            log("CACHE HIT")
            return cache[cache_key]

    # =========================
    # BUILD MODEL CHAIN
    # =========================
    models = get_model_chain(task_type)
    models += [FALLBACK_MODEL_1, FALLBACK_MODEL_2]

    # =========================
    # SEQUENTIAL EXECUTION
    # =========================
    for model in models:
        if not model:
            continue

        log(f"TRYING | {model}")
        result = call_model(model, prompt)

        if result:
            log(f"USED | {model}")

            # SAVE CACHE
            if ENABLE_CACHE:
                cache = load_cache()
                cache[cache_key] = result
                save_cache(cache)

            return result

    return "❌ All models failed"
