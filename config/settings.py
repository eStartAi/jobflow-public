CONFIG = {

    # ================================
    # 🎯 TARGET ROLES (STRICT)
    # ================================
    "target_roles": [
        "devops engineer",
        "site reliability engineer",
        "sre",
        "cloud engineer",
        "infrastructure engineer",
        "platform engineer",
        "production engineer",
        "cloud support engineer",
        "technical support engineer",
        "systems engineer"
    ],

    # ================================
    # ✅ MUST HAVE (CORE SIGNAL)
    # ================================
    "must_have_keywords": [
        "linux",
        "aws",
        "ec2",
        "ssh",
        "infrastructure",
        "cloud",
        "system",
        "troubleshooting"
    ],

    # ================================
    # 🚀 BONUS (BOOST SCORE)
    # ================================
    "bonus_keywords": [
        "docker",
        "kubernetes",
        "ci/cd",
        "terraform",
        "ansible",
        "monitoring",
        "grafana",
        "prometheus",
        "splunk",
        "dynatrace",
        "automation",
        "api"
    ],

    # ================================
    # ❌ EXCLUDE (CRITICAL CLEANUP)
    # ================================
    "exclude_keywords": [
        "senior",
        "staff",
        "principal",
        "manager",
        "director",
        "architect",
        "machine learning",
        "ml",
        "data scientist",
        "data engineer",
        "frontend",
        "backend",
        "fullstack",
        "ios",
        "android",
        "designer",
        "marketing",
        "sales",
        "account",
        "finance"
    ],

    # ================================
    # 🧠 EXPERIENCE TARGET
    # ================================
    "experience_level": [
        "entry",
        "junior",
        "associate",
        "0-2",
        "1-3"
    ],

    # ================================
    # 🌍 LOCATION FILTER
    # ================================
    "locations": [
        "remote",
        "united states",
        "pennsylvania",
        "new jersey",
        "new york"
    ],

    # ================================
    # 🧠 SMART FILTERS
    # ================================
    "smart_filters": {
        "reject_if_requires_clearance": True,
        "prefer_no_degree_required": True,
        "prefer_skills_based_roles": True
    },

    # ================================
    # 📊 SCORING WEIGHTS
    # ================================
    "scoring_weights": {
        "title_match": 30,
        "must_have_match": 25,
        "bonus_match": 10,
        "experience_match": 10,
        "location_match": 5
    },

    # ================================
    # 🎯 APPLY THRESHOLD
    # ================================
    "apply_threshold": 30
}
