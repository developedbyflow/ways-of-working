"""Checks every count the documents state against the source it comes from.

A count written in many places goes stale when a later step changes it: "132 addresses" in one file
when the API map holds 140. This script counts each fact from its source (schema.sql, the API map,
openapi.yaml, the threats, the secrets' inventory, the ADRs, the screens, the alerts) and reads every
Markdown file under docs/ for "N tables", "N addresses"... A different number fails the check.

Not checked:
  - the journal lines ("- 2026-10-14: ..."), which record what was true that day;
  - the proposals in 02-design/changes/, frozen when they were decided;
  - a number followed by "at step", "at this decision" or "before", which says when it was true;
  - a number under the fact's floor (e.g. "39 addresses" for the admin's part, "100 operations" in a batch);
  - the lines in facts-history.txt, a past count kept on purpose (one "path: text in the line" per line).

Run by ../diagrams.sh, or alone: python3 docs/02-design/checks/facts.py
"""

import pathlib
import re
import sys

here = pathlib.Path(__file__).resolve().parent
design = here.parent
docs = design.parent


def read(path):
    return (design / path).read_text(encoding="utf-8")


def table_rows(path, header):
    """The rows of the first table whose header line starts with `header`."""
    rows, inside = 0, False
    for line in read(path).splitlines():
        if line.startswith(header):
            inside = True
            continue
        if inside and line.startswith("|---"):
            continue
        if inside and line.startswith("|"):
            rows += 1
            continue
        if inside:
            break
    return rows


def screens():
    """The rows of every "| Screen |" table in the UI map's eight areas (section 9 is the navigation)."""
    rows, inside = 0, False
    for line in read("06-ui-design/02-map.md").splitlines():
        if line.startswith("## 9"):
            break
        if line.startswith("| Screen |"):
            inside = True
            continue
        if inside and line.startswith("|---"):
            continue
        if inside and line.startswith("|"):
            rows += 1
            continue
        inside = False
    return rows


def addresses():
    """The API map's rows, joined on method and path, as 07-security/checks/ways-in.py counts them."""
    row = re.compile(r"^\| *\d+[a-z]? *\| *(GET|POST|PUT|PATCH|DELETE) *\| *`([^`]+)`")
    found = set()
    for line in read("05-api-design/02-map.md").splitlines():
        m = row.match(line)
        if m:
            found.add((m[1], m[2].split("?")[0]))
    return len(found)


def operations():
    """The operations in openapi.yaml: a method under a path."""
    text = read("05-api-design/openapi.yaml")
    paths = text.split("\npaths:", 1)[1].split("\ncomponents:", 1)[0]
    return len(re.findall(r"^    (get|post|put|patch|delete):", paths, re.M))


def security_alerts():
    """The security events whose "Alert when" cell holds a threshold (in bold), not "—"."""
    rows, inside = 0, False
    for line in read("07-security/10-detection-and-response.md").splitlines():
        if line.startswith("| Event | Logged | Alert when"):
            inside = True
            continue
        if inside and line.startswith("|---"):
            continue
        if inside and line.startswith("|"):
            rows += line.rstrip(" |").split("|")[-1].strip().startswith("**")
            continue
        if inside:
            break
    return rows


def adrs():
    return len(list((docs / "00-project" / "adr").glob("[0-9][0-9][0-9][0-9]-*.md")))


WORDS = {"six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13}
NUMBER = r"(\d{1,3}(?:,\d{3})?|" + "|".join(WORDS) + r")"

# name, how it's counted, where, the words after the number, the floor under which a number is a part
FACTS = [
    ("tables", lambda: len(re.findall(r"^CREATE TABLE", read("04-data-model/schema.sql"), re.M)),
     "04-data-model/schema.sql", r"tables\b", 40),
    ("database schemas", lambda: len(re.findall(r"^CREATE SCHEMA", read("04-data-model/schema.sql"), re.M)),
     "04-data-model/schema.sql", r"schemas\b(?! with)", 8),
    ("entities", lambda: table_rows("04-data-model/01-entities.md", "| Entity |"),
     "04-data-model/01-entities.md", r"entities\b", 40),
    ("API addresses", addresses, "05-api-design/02-map.md", r"(?:API )?addresses\b", 120),
    ("operations in openapi.yaml", operations, "05-api-design/openapi.yaml", r"operations\b", 125),
    ("threats", lambda: len(re.findall(r"^\| T-\d+ ", read("07-security/03-threats.md"), re.M)),
     "07-security/03-threats.md", r"threats\b", 70),
    ("secrets", lambda: table_rows("07-security/07-data-and-secrets.md", "| Secret | Opens"),
     "07-security/07-data-and-secrets.md", r"secrets\b", 15),
    ("flows on the security map", lambda: table_rows("07-security/02-map.md", "| # | From"),
     "07-security/02-map.md", r"flows\b", 15),
    ("screens", screens, "06-ui-design/02-map.md", r"screens\b", 40),
    ("ADRs", adrs, "00-project/adr/", r"(?:ADRs|architecture decisions)\b", 25),
    ("alerts to the phone", lambda: table_rows("01-system-design/09-monitoring.md", "| Alert | When"),
     "01-system-design/09-monitoring.md", r"alerts to (?:my|the) phone\b", 6),
    ("security alerts", security_alerts,
     "07-security/10-detection-and-response.md", r"(?:security alerts|alerts on patterns)\b", 4),
]

WHEN = re.compile(r"^[^.;,()]{0,20}?\b(at step|at this decision|at the decision|before )")
JOURNAL = re.compile(r"^\s*- \d{4}-\d{2}-\d{2}")


def history():
    allowed = []
    path = here / "facts-history.txt"
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.strip() and not line.startswith("#"):
                file, _, text = line.partition(": ")
                allowed.append((file.strip(), text.strip()))
    return allowed


def main():
    # a fact whose source isn't written yet (a new project) is skipped
    counts = [(name, count(), source, re.compile(r"(?<![\w.,-])" + NUMBER + r"\** " + words, re.I), floor)
              for name, count, source, words, floor in FACTS
              if (design / source).exists() or (docs / source).exists()]
    allowed = history()
    wrong = []
    for md in sorted(docs.rglob("*.md")):
        rel = md.relative_to(docs).as_posix()
        if rel.startswith("02-design/changes/") or "/node_modules/" in rel:
            continue
        for n, line in enumerate(md.read_text(encoding="utf-8").splitlines(), 1):
            if JOURNAL.match(line) or any(rel == f and t in line for f, t in allowed):
                continue
            for name, true, source, claim, floor in counts:
                for m in claim.finditer(line):
                    said = m[1].lower()
                    said = WORDS[said] if said in WORDS else int(said.replace(",", ""))
                    if said < floor or said == true or WHEN.match(line[m.end():]):
                        continue
                    wrong.append(f"{rel}:{n}: says {m[0]!r}; {source} has {true} {name}")
    for name, true, source, _, _ in counts:
        print(f"{name}: {true} ({source})")
    if wrong:
        print(f"\n{len(wrong)} stale counts (fix them, or list a past count kept on purpose in checks/facts-history.txt):")
        print("\n".join(wrong))
        sys.exit(1)
    print("\nEvery count in the documents matches its source.")


if __name__ == "__main__":
    main()
