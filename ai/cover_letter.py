def generate_cover_letter(job):
    title = job.get("title", "")
    company = job.get("company", "")

    return f"""
Dear Hiring Manager,

I am excited to apply for the {title} position at {company}.

I bring hands-on experience in Linux systems, automation, and cloud infrastructure, including deploying and managing services on VPS environments. My background in troubleshooting, monitoring, and API-based automation aligns well with this role.

I am eager to contribute and grow within your team.

Sincerely,
GM ALAM
"""
