# Automated Copywriting & Tone Transformer
**DecodeLabs Generative AI – Project 2 | Industrial Training Kit (Batch 2026)**

A production-style CLI application that transforms raw product descriptions into high-converting, platform-optimized marketing copy with precise tone and creativity control.

---

## Project Overview

This project implements **Dynamic Orchestration** of generative AI for automated copywriting.  
It takes user-defined variables (Product Name, Platform, Tone) and injects them into a Master Instruction Template, while intelligently controlling inference parameters (Temperature, Top-P) to produce brand-safe, platform-ready content.

### Key Highlights
- Dynamic Prompt Template Compilation using Python f-strings
- Intelligent Temperature & Top-P tuning based on platform + tone
- Platform-specific constraints (LinkedIn, Instagram, Email)
- Dual Pipeline Architecture:
  - **Realtime Mode** → Single platform generation
  - **Bulk Mode** → Concurrent generation for all platforms using `asyncio.gather`
- Async execution with Semaphore (rate-limit protection)
- Automatic retry with exponential backoff (Tenacity)
- Strict output validation using Pydantic
- Clean, modular, production-ready code structure

---

## Features Mapped to Project Requirements

| Requirement                          | Implementation                          | Status |
|--------------------------------------|-----------------------------------------|--------|
| Dynamic string templates (f-strings) | `templates.py` – Master Instruction Template | ✅ |
| User variables (Product, Platform, Tone) | CLI via `argparse`                     | ✅ |
| Temperature & Top-P control          | `config.py` – Smart auto-tuning         | ✅ |
| Platform-specific filtering          | LinkedIn / Instagram / Email rules      | ✅ |
| Async Pipeline                       | `asyncio` + `Semaphore`                 | ✅ |
| Retry & Resilience                   | Tenacity exponential backoff            | ✅ |
| Output Validation                    | Pydantic models                         | ✅ |
| Dual Pipeline (Realtime + Bulk)      | `--mode realtime` / `--mode bulk`       | ✅ |
| CLI Entry Point                      | Fully featured argparse                 | ✅ |

---

## Tech Stack

- **Python 3.10+**
- **Groq API** (OpenAI-compatible, fast inference)
- `asyncio` + `Semaphore`
- `tenacity` (retry logic)
- `pydantic` (data validation)
- `rich` (beautiful terminal output)
- `python-dotenv`

---

## Project Structure
