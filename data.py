schemes = [
    {
        "name": "NSP Scholarship",
        "condition": lambda u: u["occupation"] == "student" and u["income"] < 250000,
        "benefits": "Financial support",
        "documents": ["Aadhaar", "Income Certificate"],
        "steps": ["Register", "Apply"],
        "link": "https://scholarships.gov.in/"
    }
]
