# uv run python main.py
from pathlib import Path
import tinycss2


def process_rules(rules, indent=""):
    out = []

    for rule in rules:
        if rule.type == "qualified-rule":
            selector = tinycss2.serialize(rule.prelude).strip()
            out.append(f"{indent}{selector} {{}}")

        elif rule.type == "at-rule" and rule.content:
            prelude = tinycss2.serialize(rule.prelude).strip()

            nested = tinycss2.parse_rule_list(
                rule.content,
                skip_whitespace=True,
                skip_comments=True,
            )

            body = process_rules(nested, indent + "  ")

            out.append(f"{indent}@{rule.at_keyword} {prelude} {{\n{body}\n{indent}}}")

    return "\n".join(out)


css = Path("app.css").read_text()

rules = tinycss2.parse_stylesheet(
    css,
    skip_whitespace=True,
    skip_comments=True,
)

print(process_rules(rules))
