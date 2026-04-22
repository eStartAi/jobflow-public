def tailor_resume(job, base_resume_text):
    title = job.get("title", "")
    desc = job.get("description", "")

    tailored = base_resume_text

    # 🔥 SIMPLE BOOST LOGIC (FAST + EFFECTIVE)
    if "aws" in desc.lower():
        tailored += "\n• Experience working with AWS EC2 and cloud infrastructure"

    if "docker" in desc.lower():
        tailored += "\n• Hands-on Docker container experience"

    if "linux" in desc.lower():
        tailored += "\n• Strong Linux system administration skills"

    return tailored
