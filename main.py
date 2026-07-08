cv_text = input("Paste CV Text:\n").lower()

scores = {
    "Leadership": 0,
    "Teamwork": 0,
    "Communication": 0,
    "Creativity": 0,
    "Problem Solving": 0
}

leadership_words = ["leader", "leadership", "managed", "captain", "organized"]
teamwork_words = ["team", "collaboration", "cooperate", "group"]
communication_words = ["communication", "presentation", "speaker"]
creativity_words = ["creative", "innovation", "design", "idea"]
problem_words = ["problem solving", "analysis", "analytical", "research"]

for word in leadership_words:
    if word in cv_text:
        scores["Leadership"] += 1

for word in teamwork_words:
    if word in cv_text:
        scores["Teamwork"] += 1

for word in communication_words:
    if word in cv_text:
        scores["Communication"] += 1

for word in creativity_words:
    if word in cv_text:
        scores["Creativity"] += 1

for word in problem_words:
    if word in cv_text:
        scores["Problem Solving"] += 1

print("\n===== Personality Analysis Report =====")

for trait, score in scores.items():
    print(f"{trait}: {score}")

best_trait = max(scores, key=scores.get)

print("\nDominant Personality Trait:", best_trait)
