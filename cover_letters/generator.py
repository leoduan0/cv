import os
from string import Template
import subprocess
import sys
from textwrap import dedent

names = ["Leo Wu", "Hanbang Wu"]

addresses = [
    "1121 Edinburgh St, New Westminster, BC, Canada",
    "2438-89 Chestnut St, Toronto, ON, Canada",
]

applications = [
    {
        "company": "Agentis",
        "position": "Investment Banking Summer Analyst 2026",
        "whycompany": "At Agentis",
        "address": addresses[0],
        "name": names[0],
    },
    {
        "company": "Vinci",
        "position": "AI Intern 2026",
        "whycompany": "At Vinci",
        "address": addresses[1],
        "name": names[0],
    },
    {
        "company": "Cresta",
        "position": "AI Quality Assurance Intern",
        "whycompany": "At Cresta",
        "address": addresses[1],
        "name": names[0],
    },
    {
        "company": "Bank of Canada",
        "position": "Student Web Development",
        "whycompany": "At Bank of Canada",
        "address": addresses[1],
        "name": names[0],
    },
    {
        "company": "D2L",
        "position": "Internal AI Developer Co-op",
        "whycompany": "At D2L",
        "address": addresses[1],
        "name": names[0],
    },
    {
        "company": "Exiger",
        "position": "AI Data Engineer Intern 2026",
        "whycompany": "At Exiger",
        "address": addresses[1],
        "name": names[0],
    },
    {
        "company": "Exiger",
        "position": "Application Support Intern 2026",
        "whycompany": "At Exiger",
        "address": addresses[1],
        "name": names[0],
    },
    {
        "company": "Exiger",
        "position": "Cybersecurity Intern 2026",
        "whycompany": "At Exiger",
        "address": addresses[1],
        "name": names[0],
    },
    {
        "company": "Exiger",
        "position": "Software Engineer Intern 2026",
        "whycompany": "At Exiger",
        "address": addresses[1],
        "name": names[0],
    },
    {
        "company": "Eli Lilly and Company",
        "position": "AI and Automation Solutions Intern",
        "whycompany": "At Eli Lilly and Company",
        "address": addresses[1],
        "name": names[0],
    },
    {
        "company": "MongoDB",
        "position": "Software Engineer Intern 2026",
        "whycompany": "At MongoDB",
        "address": addresses[1],
        "name": names[0],
    },
    {
        "company": "Novolex",
        "position": "Data Science Intern",
        "whycompany": "At Novolex",
        "address": addresses[1],
        "name": names[0],
    },
    {
        "company": "Celestica",
        "position": "Process and Applications (SCM) Intern 2026",
        "whycompany": "At Celestica",
        "address": addresses[1],
        "name": names[0],
    },
    {
        "company": "Quora",
        "position": "Software Engineering Intern",
        "whycompany": "At Quora",
        "address": addresses[1],
        "name": names[0],
    },
    {
        "company": "Ripple",
        "position": "Software Engineer Intern 2026",
        "whycompany": "At Ripple",
        "address": addresses[1],
        "name": names[0],
    },
    {
        "company": "Ripple",
        "position": "Software Engineer Intern 2026",
        "whycompany": "At Ripple",
        "address": addresses[1],
        "name": names[0],
    },
    {
        "company": "Robinhood",
        "position": "2026 Web Developer Intern",
        "whycompany": "At Robinhood",
        "address": addresses[1],
        "name": names[0],
    },
    {
        "company": "Robinhood",
        "position": "Software Developer Intern 2026",
        "whycompany": "At Robinhood",
        "address": addresses[1],
        "name": names[0],
    },
    {
        "company": "Celestica",
        "position": "SCM Data Scientist Intern 2026",
        "whycompany": "At Celestica",
        "address": addresses[1],
        "name": names[0],
    },
    {
        "company": "Celestica",
        "position": "Supply Chain Management Intern 2026",
        "whycompany": "At Celestica",
        "address": addresses[1],
        "name": names[0],
    },
    {
        "company": "Verdi",
        "position": "Software Engineer Intern 2026",
        "whycompany": "I am particularly drawn to Verdi's focus in making irrigation automation affordable",
        "address": addresses[1],
        "name": names[0],
    },
]

LETTER_TEMPLATE = Template(
    """
\\documentclass[11pt,a4paper]{letter}

\\usepackage[scale=0.8]{geometry}
\\usepackage{hyperref}

\\newcommand{\\Company}{$company}
\\newcommand{\\Position}{$position}
\\newcommand{\\WhyCompany}{$whycompany}

\\signature{$name}
\\address{$address}

\\begin{document}
\\begin{letter}{}
  \\opening{Dear \\Company\\ Recruitment Team:}

  I am writing to apply for the \\Position\\ position at \\Company. As a first-year student intending to major in Statistics and Computer Science at the University of Toronto, I have extensive experience in full-stack web development, applied machine learning, and collaborative tools for software development. \\WhyCompany, and I am ready to contribute to your engineering team by applying my technical skills to real-world, high-impact projects.

  As a member of the UofT Autonomous Scale Racing (UTASR) team, I combined research and application by implementing the state-of-the-art Deeplabv3 segmentation model using PyTorch to enhance autonomous vehicle perception. This experience deepened my appreciation for building systems that strike a balance between accuracy and performance, as well as the importance of using version control systems effectively to support cohesive teamwork.

  At UofT BIONIC, I currently lead the software development of an Android app for a client with special accessibility needs. Moving out of my usual comfort zone of React Native to Kotlin-based, native Android development pushed me to be extra attentive to all parts of the project - a challenge that strengthened both my technical skills and communication skills as a lead.

  Beyond university work, I enjoy sharpening my skills through personal projects. I built \\href{https://lerna.app}{Lerna} and \\href{https://commonblog.vercel.app}{CommonBlog}, which gave me hands-on experience in full-stack web development from initial commit to deployment. From using new technologies such as PostgreSQL to designing fault-tolerant APIs, I've learned to treat software development as an invaluable opportunity to challenge myself while delivering reliable products for users.

  I am incredibly excited to bring my curiosity, technical foundations, and collaborative mindset to \\Company. Thank you for considering my application.

  \\closing{Sincerely,}
\\end{letter}
\\end{document}
"""
)


def sanitize_filename(company: str, position: str) -> str:
    return f"{company}-{position}".replace(" ", "_").lower()


def generate_tex_file(application, output_dir="."):
    os.makedirs(output_dir, exist_ok=True)
    tex_content = dedent(
        LETTER_TEMPLATE.substitute(
            company=application["company"],
            position=application["position"],
            whycompany=application["whycompany"],
            address=application["address"],
            name=application["name"],
        )
    )

    filename_base = sanitize_filename(application["company"], application["position"])
    tex_path = os.path.join(output_dir, f"{filename_base}.tex")

    with open(tex_path, "w", encoding="utf-8") as f:
        f.write(tex_content)

    print(f"Generated at {tex_path}")
    return tex_path


def format_tex(tex_path):
    try:
        subprocess.run(
            ["tex-fmt", "--nowrap", tex_path],
            cwd=os.path.dirname(tex_path),
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True,
        )
        print(f"Formatted {tex_path}")
    except subprocess.CalledProcessError:
        print(f"Failed to format {tex_path}")


def compile_tex(tex_path):
    try:
        subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", tex_path],
            cwd=os.path.dirname(tex_path),
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True,
        )
        print(f"Compiled {os.path.basename(tex_path)}")
    except subprocess.CalledProcessError:
        print(f"Failed to compile {tex_path}")


if __name__ == "__main__":
    indices = [int(x) for x in sys.argv[1:]]
    if len(indices) == 0:
        indices = [i for i in range(len(applications))]
    for app in [a for i, a in enumerate(applications) if i in indices]:
        if not app:
            continue
        tex_path = generate_tex_file(app)
        format_tex(tex_path)
        compile_tex(tex_path)
