# ================================
# ENABLE / DISABLE SOURCES (CRITICAL FIX)
# ================================
USE_GREENHOUSE = True
USE_LEVER = True


# ================================
# Greenhouse Companies
# ================================
GREENHOUSE_COMPANIES = [
    "stripe",
    "airbnb",
    "doordash",
    "discord",
    "notion",
    "figma",
    "datadog",
    "cloudflare",
    "twilio",
    "reddit",
    "shopify",
    "coinbase"
]


# ================================
# Lever Companies
# ================================
LEVER_COMPANIES = [
    "netlify",
    "vercel",
    "render",
    "supabase",
    "railway",
    "gusto",
    "rippling",
    "pilot",
    "sendgrid"
]


# ================================
# MAIN FUNCTION
# ================================
def get_active_companies():
    return {
        "greenhouse": GREENHOUSE_COMPANIES if USE_GREENHOUSE else [],
        "lever": LEVER_COMPANIES if USE_LEVER else []
    }
