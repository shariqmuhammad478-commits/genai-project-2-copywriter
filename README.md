# Automated Copywriting & Tone Transformer

**DecodeLabs Generative AI – Project 2 | Industrial Training Kit (Batch 2026)**

A production-style CLI application that transforms raw product descriptions into high-converting, platform-optimized marketing copy with precise tone and creativity control.

---

## Project Overview

This project implements **Dynamic Orchestration** of generative AI for automated copywriting.
It takes user-defined variables (Product Name, Platform, Tone) and injects them into a Master Instruction Template, while intelligently controlling inference parameters (Temperature, Top-P) to produce brand-safe, platform-ready content.

### Key Highlights

- Dynamic Prompt Template Compilation using Python f-strings
- Intelligent Temperature and Top-P tuning based on platform and tone
- Platform-specific constraints for LinkedIn, Instagram, and Email
- Dual Pipeline Architecture:
  - Realtime Mode: single platform generation
  - Bulk Mode: concurrent generation for all platforms using asyncio.gather
- Async execution with Semaphore for rate-limit protection
- Automatic retry with exponential backoff using Tenacity
- Strict output validation using Pydantic
- Clean modular production-ready code structure

---

## Features Mapped to Project Requirements

| Requirement | Implementation | Status |
|---|---|---|
| Dynamic string templates (f-strings) | templates.py Master Instruction Template | Yes |
| User variables (Product, Platform, Tone) | CLI via argparse | Yes |
| Temperature and Top-P control | config.py smart auto-tuning | Yes |
| Platform-specific filtering | LinkedIn, Instagram, Email rules | Yes |
| Async Pipeline | asyncio and Semaphore | Yes |
| Retry and Resilience | Tenacity exponential backoff | Yes |
| Output Validation | Pydantic models | Yes |
| Dual Pipeline (Realtime + Bulk) | --mode realtime / --mode bulk | Yes |
| CLI Entry Point | Fully featured argparse | Yes |

---

## Tech Stack

- Python 3.10+
- Groq API (OpenAI-compatible, fast inference)
- asyncio + Semaphore
- tenacity (retry logic)
- pydantic (data validation)
- rich (beautiful terminal output)
- python-dotenv

---

## Project Structure

    project2_automated_copywriter/
    ├── main.py              # CLI entry point + Dual Pipeline router
    ├── generator.py         # Async generation engine + retry + semaphore
    ├── templates.py         # Master Instruction Template (f-strings)
    ├── config.py            # Temperature and parameter tuning logic
    ├── models.py            # Pydantic output schemas
    ├── requirements.txt
    ├── .env.example
    ├── .gitignore
    └── README.md

---

## Setup Instructions

1. Clone the repository
2. Create virtual environment:
   - python -m venv venv
   - venv\Scripts\activate
3. Install dependencies:
   - pip install -r requirements.txt
4. Create .env file and add:
   - GROQ_API_KEY=your_key_here

---

## Usage

### 1. Realtime Mode (Single Platform)

    python main.py --product "Nike Air Zoom" --platform Instagram --tone witty --description "Lightweight running shoes with responsive cushioning" --mode realtime

### 2. Bulk Mode (All Platforms Concurrently)

    python main.py --product "Nike Air Zoom" --tone professional --description "Lightweight running shoes with responsive cushioning and breathable mesh upper" --mode bulk

---

## Architecture Flow

    CLI Input (argparse)
            |
            v
    Mode Router
       |-- Realtime -> Single Async Call
       |-- Bulk     -> asyncio.gather (LinkedIn + Instagram + Email)
            |
            v
    Master Prompt Compiler (f-strings + platform rules)
            |
            v
    Parameter Tuner (Temperature / Top-P)
            |
            v
    Async Generator + Semaphore + Tenacity Retry
            |
            v
    Pydantic Validation
            |
            v
    Rich Terminal Output

---

## What This Project Demonstrates

- Mastery of Dynamic Prompt Engineering
- Inference parameter control for creative variance
- Production-ready async concurrency patterns
- Rate-limit resilience and error handling
- Clean software engineering practices suitable for real-world AI systems

---

## Author

**Muhammad Shariq Naseer**
DecodeLabs Generative AI Industrial Training – Batch 2026  
Project 2: Automated Copywriting & Tone Transformer

Built with focus on scalability, precision, and professional AI engineering standards.
```