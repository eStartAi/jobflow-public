def generate_answers(job):
    title = job.get("title", "")
    company = job.get("company", "")

    answers = f"""
Why are you interested in this role?
→ I am interested in the {title} role at {company} because it aligns with my experience in Linux systems, automation, and cloud infrastructure.

What makes you a good fit?
→ I have hands-on experience working with VPS systems, deploying applications, troubleshooting infrastructure, and automating workflows using Python and APIs.

Describe a challenge:
→ I built and deployed automated systems on VPS environments, handling errors, debugging issues, and ensuring uptime using monitoring tools.
"""

    return answers
