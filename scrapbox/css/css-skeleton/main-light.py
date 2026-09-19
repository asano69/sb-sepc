from pathlib import Path
import tinycss2

css = Path("app.css").read_text(encoding="utf-8")

rules = tinycss2.parse_stylesheet(
    css,
    skip_comments=True,
    skip_whitespace=True,
)

out = []

for rule in rules:
    if rule.type != "qualified-rule":
        continue

    selector = tinycss2.serialize(rule.prelude).strip()
    out.append(f"{selector} {{}}")

print("\n".join(out))
