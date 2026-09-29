import asyncio
import os
from groq import AsyncGroq
from tenacity import retry, wait_exponential, stop_after_attempt, retry_if_exception_type
from dotenv import load_dotenv

from models import MarketingCopy
from templates import build_master_prompt
from config import get_generation_config

load_dotenv()

client = AsyncGroq(api_key=os.getenv("GROQ_API_KEY"))
semaphore = asyncio.Semaphore(5)


@retry(
    wait=wait_exponential(multiplier=1, min=2, max=12),
    stop=stop_after_attempt(4),
    retry=retry_if_exception_type(Exception),
    reraise=True
)
async def generate_copy(
    product_name: str,
    platform: str,
    tone: str,
    raw_description: str,
    temperature: float = None
) -> MarketingCopy:

    async with semaphore:
        prompt = build_master_prompt(product_name, platform, tone, raw_description)
        config = get_generation_config(platform, tone, temperature)

        response = await client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {
                    "role": "system",
                    "content": "You are a world-class marketing copywriter who creates high-converting, platform-optimized content."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=config["temperature"],
            max_tokens=config["max_tokens"],
            top_p=config["top_p"]
        )

        copy_text = response.choices[0].message.content.strip()

        # Safety fallback if model returns empty
        if not copy_text or len(copy_text) < 30:
            if platform == "Email":
                copy_text = f"""Subject: Experience the Difference with {product_name}

Hi there,

Looking for better performance and comfort? The {product_name} is designed with {raw_description}.

Elevate your daily routine and feel the difference.

Shop now and step into comfort.

Best regards,
The Team"""
            else:
                copy_text = f"Discover the new {product_name} – {raw_description}. Perfect for those who demand more."

        return MarketingCopy(
            product_name=product_name,
            platform=platform,
            tone=tone,
            generated_copy=copy_text,
            character_count=len(copy_text),
            word_count=len(copy_text.split()),
            temperature_used=config["temperature"]
        )