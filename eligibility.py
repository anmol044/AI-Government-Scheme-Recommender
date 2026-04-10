from utils.ai_reason import get_reason

def check_eligibility(user, schemes):
    results = []

    for scheme in schemes:
        try:
            if scheme["condition"](user):
                reason = get_reason(user, scheme["name"])
                results.append({
                    "scheme_name": scheme["name"],
                    "eligibility_reason": reason,
                    "link": scheme["link"]
                })
        except:
            continue

    return results
