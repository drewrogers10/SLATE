import re
from pathlib import Path

source_path = Path("SLATE_Agent_Prompts.md")
output_dir = Path("prompts")

lines = source_path.read_text(encoding="utf-8").splitlines()

output_dir.mkdir(exist_ok=True)

current_slug: str | None = None
current_lines: list[str] = []


def parse_heading(heading: str) -> tuple[bool, str, str]:
    parts = heading.split(")", 1)
    if len(parts) == 2 and parts[0].strip().isdigit():
        number = parts[0].strip()
        return True, parts[1].strip(), number
    return False, heading.strip(), ""


def slugify(heading: str) -> str:
    _, name_part, number = parse_heading(heading)
    slug_base = re.sub(r"[^0-9a-zA-Z]+", "_", name_part.lower()).strip("_")
    if number:
        return f"{number}_{slug_base}"
    return slug_base or "section"


def write_file(slug: str, content_lines: list[str]) -> None:
    text = "\n".join(content_lines).rstrip() + "\n"
    (output_dir / f"{slug}.md").write_text(text, encoding="utf-8")


for line in lines:
    if line.startswith("## "):
        heading = line[3:].strip()
        is_agent_section, _, _ = parse_heading(heading)

        if current_slug is not None:
            write_file(current_slug, current_lines)

        if is_agent_section:
            current_slug = slugify(heading)
            current_lines = [line]
        else:
            current_slug = None
            current_lines = []
    else:
        if current_slug is not None:
            current_lines.append(line)

if current_slug is not None:
    write_file(current_slug, current_lines)
