BLACKLIST = ["phish.example.local", "bank.fake.local"]

def check_url(url: str) -> str:
    score = 0

    if not url.startswith("https://"):
        score += 1

    if "@" in url or url.count("//") > 1:
        score += 1

    if len(url) > 75:
        score += 1

    suspicious_keywords = ["login", "secure", "verify", "update", "bank"]
    if any(word in url.lower() for word in suspicious_keywords):
        score += 1

    if any(domain in url for domain in BLACKLIST):
        return "Phishing"

    if score >= 3:
        return "Phishing"
    elif score == 2:
        return "Suspicious"
    else:
        return "Safe"
