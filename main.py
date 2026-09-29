import argparse
import asyncio
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from generator import generate_copy

console = Console()


def parse_args():
    parser = argparse.ArgumentParser(
        description="Automated Copywriting & Tone Transformer | DecodeLabs Generative AI Project 2",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("--product", required=True, help="Product name")
    parser.add_argument("--tone", required=True, help="Desired tone (e.g. witty, professional, persuasive)")
    parser.add_argument("--description", required=True, help="Raw product description")
    parser.add_argument(
        "--platform",
        choices=["LinkedIn", "Instagram", "Email"],
        help="Target platform (required in realtime mode)"
    )
    parser.add_argument(
        "--mode",
        choices=["realtime", "bulk"],
        default="realtime",
        help="realtime = single platform | bulk = all platforms concurrently"
    )
    parser.add_argument("--temperature", type=float, default=None, help="Optional temperature override")
    return parser.parse_args()


async def run_realtime(args):
    if not args.platform:
        console.print("[red]Error: --platform is required in realtime mode[/red]")
        return

    console.print("\n[bold cyan]🚀 Real-time Mode[/bold cyan]")
    console.print("[dim]Generating single platform copy...[/dim]\n")

    result = await generate_copy(
        product_name=args.product,
        platform=args.platform,
        tone=args.tone,
        raw_description=args.description,
        temperature=args.temperature
    )

    summary = (
        f"[bold]Product:[/bold] {result.product_name}\n"
        f"[bold]Platform:[/bold] {result.platform}\n"
        f"[bold]Tone:[/bold] {result.tone}\n"
        f"[bold]Temperature Used:[/bold] {result.temperature_used}\n"
        f"[bold]Characters:[/bold] {result.character_count}  |  [bold]Words:[/bold] {result.word_count}"
    )

    console.print(Panel.fit(summary, title="[bold green]Generation Summary[/bold green]", border_style="green"))
    console.print("\n[bold green]📝 Final Marketing Copy:[/bold green]\n")
    console.print(Panel(result.generated_copy, border_style="blue"))
    console.print()


async def run_bulk(args):
    console.print("\n[bold cyan]⚡ Bulk Mode (Async Concurrent Generation)[/bold cyan]")
    console.print("[dim]Generating LinkedIn + Instagram + Email simultaneously using asyncio.gather...[/dim]\n")

    platforms = ["LinkedIn", "Instagram", "Email"]

    tasks = [
        generate_copy(
            product_name=args.product,
            platform=platform,
            tone=args.tone,
            raw_description=args.description,
            temperature=args.temperature
        )
        for platform in platforms
    ]

    results = await asyncio.gather(*tasks)

    # Summary Table
    table = Table(title="Bulk Generation Summary", show_header=True, header_style="bold magenta")
    table.add_column("Platform", style="cyan")
    table.add_column("Tone", style="green")
    table.add_column("Temp", justify="center")
    table.add_column("Chars", justify="right")
    table.add_column("Words", justify="right")

    for r in results:
        table.add_row(r.platform, r.tone, str(r.temperature_used), str(r.character_count), str(r.word_count))

    console.print(table)
    console.print()

    for r in results:
        console.print(Panel(
            r.generated_copy,
            title=f"[bold]{r.platform} Copy[/bold]",
            border_style="blue"
        ))
        console.print()


async def main():
    args = parse_args()

    console.print("\n[bold cyan]Automated Copywriting & Tone Transformer[/bold cyan]")
    console.print("[dim]DecodeLabs Generative AI Project 2 | Dual Pipeline (Realtime + Bulk)[/dim]")

    if args.mode == "bulk":
        await run_bulk(args)
    else:
        await run_realtime(args)


if __name__ == "__main__":
    asyncio.run(main())