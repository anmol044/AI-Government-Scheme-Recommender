from data.schemes import schemes
from utils.eligibility import check_eligibility

def get_user():
    user = {}
    user["name"] = input("Enter your name: ")
    user["age"] = int(input("Enter your age: "))
    user["gender"] = input("Enter gender: ").strip().lower()
    user["income"] = int(input("Enter income: "))
    user["occupation"] = input("Enter occupation: ").strip().lower()
    user["category"] = input("Enter category: ").strip().upper()
    user["state"] = input("Enter state: ").strip().lower()
    user["locality"] = input("Enter locality: ").strip().lower()
    return user

user = get_user()
results = check_eligibility(user, schemes)

if results:
    for r in results:
        print("\n📌", r["scheme_name"])
        print("Why:", r["eligibility_reason"])
        print("Apply:", r["link"])
else:
    print("No schemes found.")
