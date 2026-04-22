def fetch_company_list():
    """
    Returns a list of company slugs to test for ATS systems.
    This is a curated + expandable list.
    """

    return [
        # 🔹 DevOps / Infra friendly
        "zapier",
        "gitlab",
        "hashicorp",
        "datadog",
        "newrelic",
        "cloudflare",
        "fastly",
        "pagerduty",
        "elastic",
        "sentry",
        "digitalocean",

        # 🔹 Mid-tier SaaS
        "hubspot",
        "atlassian",
        "shopify",
        "twilio",
        "okta",
        "mongodb",

        # 🔹 Startups
        "vercel",
        "supabase",
        "railway",
        "planet",
        "scaleai",
        "sourcegraph",

        # 🔹 Limited big tech
        "stripe",
        "dropbox",
        "reddit",
        "figma"
    ]
