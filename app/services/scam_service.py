def detect_scam(text: str) -> bool:
    text = text.lower()

    scam_keywords = [
        "otp", "urgent", "verify", "verification",
        "bank", "account", "payment", "lottery",
        "police", "kYC", "seize", "freeze"
    ]

    return any(word in text for word in scam_keywords)
