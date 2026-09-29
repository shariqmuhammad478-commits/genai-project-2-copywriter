def get_generation_config(platform: str, tone: str, user_temp: float = None) -> dict:
    """
    Intelligent parameter tuning based on platform and tone.
    High temperature → creative / social platforms
    Low temperature  → professional / email
    """

    if user_temp is not None:
        temperature = max(0.0, min(1.0, user_temp))  # clamp between 0-1
    else:
        creative_tones = ["witty", "fun", "casual", "playful", "bold", "humorous"]
        if platform == "Instagram" or any(t in tone.lower() for t in creative_tones):
            temperature = 0.85
        elif platform == "Email":
            temperature = 0.35
        else:  # LinkedIn default
            temperature = 0.45

    return {
        "temperature": temperature,
        "max_tokens": 700,
        "top_p": 0.9,
    }
