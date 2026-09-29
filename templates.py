def build_master_prompt(product_name: str, platform: str, tone: str, raw_description: str) -> str:
    platform_rules = {
        "LinkedIn": (
            "Write professional, value-driven LinkedIn post. "
            "Length: 120-250 words. Focus on benefits and credibility. Soft call-to-action."
        ),
        "Instagram": (
            "Write catchy, engaging Instagram caption. "
            "Use emojis and 3-5 hashtags. Strong hook in first line. Max 2200 characters."
        ),
        "Email": (
            "Write a persuasive marketing email. "
            "Start with a compelling subject line, then the email body. "
            "Length: 100-180 words. Clear call-to-action at the end."
        )
    }

    rule = platform_rules.get(platform, "Write professional high-converting marketing copy.")

    prompt = f"""
You are an expert marketing copywriter.

Product: {product_name}
Platform: {platform}
Tone: {tone}
Product Description: {raw_description}

Instructions:
- Write in {tone} tone
- Follow these platform rules: {rule}
- Make it high-converting and natural
- Output only the final copy (no extra explanations)
"""
    return prompt.strip()