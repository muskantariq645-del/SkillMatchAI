from flask import Flask, render_template, request

app = Flask(__name__)

CAREERS = [
    {
        "title": "Python Developer",
        "keywords": ["python", "programming", "coding", "software"],
        "description": "Develop applications and solve problems using Python.",
        "learn": "Python, problem solving, Git"
    },
    {
        "title": "Web Developer",
        "keywords": ["html", "css", "javascript", "web", "website"],
        "description": "Create and maintain interactive websites.",
        "learn": "HTML, CSS, JavaScript, web fundamentals"
    },
    {
        "title": "Data Analyst",
        "keywords": ["sql", "excel", "data", "statistics", "analysis"],
        "description": "Explore data to identify patterns and support decisions.",
        "learn": "SQL, Excel, Python, data visualization"
    },
    {
        "title": "AI / Machine Learning Beginner",
        "keywords": ["ai", "artificial intelligence", "machine learning",
                     "python", "models"],
        "description": "Explore intelligent systems and machine learning projects.",
        "learn": "Python, statistics, machine learning fundamentals"
    },
    {
        "title": "UI/UX Designer",
        "keywords": ["design", "creativity", "ui", "ux", "user experience"],
        "description": "Design digital products that are clear and easy to use.",
        "learn": "Design principles, prototyping, user research"
    },
    {
        "title": "Cybersecurity Analyst",
        "keywords": ["security", "network", "cybersecurity", "linux"],
        "description": "Help protect computer systems and digital information.",
        "learn": "Networking, Linux, security fundamentals"
    }
]


def recommend_careers(skills, interests):
    profile = (skills + " " + interests).lower()
    matches = []

    for career in CAREERS:
        matched = [
            word for word in career["keywords"]
            if word in profile
        ]

        if matched:
            score = min(95, 50 + len(matched) * 15)
            matches.append({
                "title": career["title"],
                "description": career["description"],
                "learn": career["learn"],
                "score": score
            })

    if not matches:
        matches = [{
            "title": "Explore Software Development",
            "description": (
                "Start by exploring programming, web development, "
                "and data analysis to discover what interests you."
            ),
            "learn": "Python basics, HTML, CSS, problem solving",
            "score": 50
        }]

    matches.sort(key=lambda item: item["score"], reverse=True)
    return matches[:3]


@app.route("/", methods=["GET", "POST"])
def home():
    name = ""
    skills = ""
    interests = ""
    results = []

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        skills = request.form.get("skills", "").strip()
        interests = request.form.get("interests", "").strip()

        if name and skills and interests:
            results = recommend_careers(skills, interests)

    return render_template(
        "index.html",
        name=name,
        skills=skills,
        interests=interests,
        results=results
    )


if __name__ == "__main__":
    app.run(debug=True)