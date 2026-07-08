cv_text = input("Enter CV text: ").lower()

traits = []

if "leader" in cv_text or "leadership" in cv_text:
    traits.append("Leadership")

if "team" in cv_text or "collaboration" in cv_text:
    traits.append("Teamwork")

if "communication" in cv_text:
    traits.append("Communication Skills")

if "creative" in cv_text:
    traits.append("Creativity")

if "problem solving" in cv_text:
    traits.append("Problem Solving")

print("\nPredicted Personality Traits:")
if traits:
    for trait in traits:
        print("-", trait)
else:
    print("No specific traits detected.")
