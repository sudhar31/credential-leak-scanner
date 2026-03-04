import requests

def check_email_breach(email):

    url = f"https://api.xposedornot.com/v1/check-email/{email}"

    response = requests.get(url)

    def calculate_risk(count):

        if count == 0:
            return "SAFE"

        elif count <= 10:
            return "LOW"

        elif count <= 50:
            return "MEDIUM"

        else:
            return "HIGH"

    if response.status_code == 200:

        data = response.json()

        if "breaches" in data and data["breaches"]:

            breaches = data["breaches"]

            # This will help for me to Flatten nested list
            if isinstance(breaches[0], list):
                breaches = breaches[0]

            risk = calculate_risk(len(breaches))

            return {
                "breached": True,
                "count": len(breaches),
                "sites": breaches,
                "risk": risk
            }

    return {"breached": False}