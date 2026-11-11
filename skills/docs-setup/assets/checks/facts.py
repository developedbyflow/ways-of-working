"""Checks every count the documents state against the source it comes from.

A count written in many places goes stale when a later step changes it: "132 addresses" in one file
when the API map holds 140. This script counts each fact from its source (a table's rows, a file's lines,
the files in a folder, an OpenAPI file) and reads every Markdown file under docs/ for "N tables",
"N addresses"... A different number fails the check, with the file and the line to fix.

FACTS below holds one guard per count that many documents repeat, grouped by the Design step that writes
its source. Each guard reads its source by the header line or the pattern that step's skill writes, so keep
the tables' header lines as the templates write them; when a project words a count differently, change the
guard's words, and add a guard for every other count its documents repeat. A fact whose source isn't
written yet is skipped: on a new project every fact is skipped and the check passes.

Not checked:
  - the journal lines ("- 2026-10-14: ..."), which record what was true that day;
  - the proposals in 02-design/09-architecture-overview/changes/, frozen when they were decided;
  - a number followed by "at step", "at this decision", "before" or "when drafted", which says when it was true;
  - a number under the fact's floor: a part, not the total ("the module's 4 tables");
  - a count inside a text listed in facts-history.txt, a past count kept on purpose (one "path: text in the
    line" per line); the rest of that line is still checked.

Run by ../diagrams.sh, or alone: python3 docs/02-design/checks/facts.py
Standard library only.
"""

import pathlib
import re
import sys

here = pathlib.Path(__file__).resolve().parent
design = here.parent       # docs/02-design
docs = design.parent       # docs


def where(path):
    """A source's path: from docs/02-design for the Design steps' files, from docs/ for the project's (00-project/adr)."""
    return design / path if (design / path).exists() else docs / path


def read(path):
    return where(path).read_text(encoding="utf-8")


# ---------------------------------------------------------------------------------------------------------
# How a fact is counted. Each function reads one kind of source; a guard in FACTS calls it with its own file
# and pattern. A table or a block that isn't found counts 0, and the summary at the end says so.

SEPARATOR = re.compile(r"^\|[\s:|-]+$")          # the |---|:---:| line under a table's header
CELL = re.compile(r"(?<!\\)\|")                   # a cell's border, not an escaped \| inside a cell


def table_rows(path, header, only=None, every=False, until=None):
    """How many rows the first Markdown table whose header line starts with `header` has.

    only:  a test on the row's cells (a list of stripped strings): only the rows that pass it count,
           e.g. lambda cells: cells[-1].startswith("**") for "its threshold, the last cell, is in bold";
    every: count the rows of every table with that header in the file (one per area), not only the first;
    until: stop at the first line that starts with it (a section whose tables aren't part of the count).
    """
    rows, inside = 0, False
    for line in read(path).splitlines():
        if until and line.startswith(until):
            break
        if line.startswith(header):
            inside = True
            continue
        if inside and SEPARATOR.match(line.strip()):
            continue
        if inside and line.startswith("|"):
            cells = [cell.strip() for cell in CELL.split(line.strip().strip("|"))]
            rows += only is None or bool(only(cells))
            continue
        if inside and not every:
            break
        inside = False
    return rows


def lines(path, pattern, value=None):
    """How many lines of a file match `pattern` (a regular expression, matched at the line's start);
    with `value`, only the lines whose first group is `value` (an answer in a column, such as "gap")."""
    regex = re.compile(pattern)
    return sum(1 for line in read(path).splitlines()
               if (m := regex.match(line)) and (value is None or m[1] == value))


API_ROW = re.compile(r"^\| *\d+[a-z]? *\| *(GET|POST|PUT|PATCH|DELETE|HEAD|OPTIONS) *\| *`([^`]+)`[^|]*\|(?:([^|]*)\|)?")


def addresses(path, method=None, address=None, who=None):
    """The API map's addresses: its rows "| 12 | POST | `/api/v1/...` | logged in | ...", joined on the method and
    the path without its query, so an address written in two rows counts once (as a script that tests every
    address sees them). With `method`, `address` (a regular expression the whole path must match) or `who`
    (the "Who" cell, exactly), only the addresses that match: a part of the map that one rule covers."""
    found = set()
    for line in read(path).splitlines():
        m = API_ROW.match(line)
        if not m:
            continue
        verb, url, cell = m[1], m[2].split("?")[0], (m[3] or "").strip()
        if ((method is None or verb == method) and (address is None or re.fullmatch(address, url))
                and (who is None or cell == who)):
            found.add((verb, url))
    return len(found)


def yaml_block(text, key, indent):
    """The lines under `key:` at `indent` spaces, up to the next key at that indentation or less."""
    start = re.search(rf"^{' ' * indent}{key}:[ \t]*$", text, re.M)
    if not start:
        return ""
    rest = text[start.end():]
    end = re.search(rf"^ {{0,{indent}}}\S", rest, re.M)
    return rest[:end.start()] if end else rest


def operations(path):
    """The operations in an OpenAPI file: a method under a path (two spaces per level, as linters write it)."""
    return len(re.findall(r"^    (?:get|put|post|delete|options|head|patch|trace):",
                          yaml_block(read(path), "paths", 0), re.M))


def operations_behind(path, scheme):
    """The operations in an OpenAPI file that need the login: `scheme` is its name under components/securitySchemes.
    An operation without a `security:` of its own takes the file's; it needs the login when every alternative of
    that list names the scheme ("- session: []"). Open (`security: []`), the login optional ("- {}") or another
    scheme (a provider's token) isn't behind the login. A `security:` written another way (inline, as
    `[{session: []}]`) stops the check: count it by hand once, then teach this function to read it."""
    alternative = re.compile(rf"- {re.escape(scheme)}: \[[^\]]*\]$")

    def needs_login(items):
        return bool(items) and all(alternative.match(item.strip()) for item in items)

    text = read(path)
    top = re.search(r"^security:\n((?:  - .*\n)+)", text, re.M)
    default = needs_login(top[1].splitlines()) if top else False
    count = 0
    methods = r"^    (?:get|put|post|delete|options|head|patch|trace):"
    for op in re.split(methods, yaml_block(text, "paths", 0), flags=re.M)[1:]:
        op = re.split(r"^ {0,4}\S", op, maxsplit=1, flags=re.M)[0]   # it ends at the next path or path-level key
        own = re.search(r"^      security:(.*)\n((?:        - .*\n)*)", op, re.M)
        if not own:
            count += default
        elif own[1].strip() == "[]":
            continue
        elif own[1].strip() == "" and own[2]:
            count += needs_login(own[2].splitlines())
        else:
            raise ValueError(f"facts.py: a security: written in a way operations_behind() doesn't read: {own[0]!r}")
    return count


def schemas_with_fields(path):
    """The schemas under components/schemas of an OpenAPI file with a `properties:` of their own
    (an enum, or an allOf of other schemas, isn't one)."""
    schemas = yaml_block(read(path), "schemas", 2)
    blocks = re.split(r"^    (?=[^\s#][^:\n]*:[ \t]*$)", schemas, flags=re.M)
    return sum(1 for block in blocks if re.search(r"^      properties:", block, re.M))


def array_items(path, name, themes=1):
    """How many items a script's array `const NAME = [ ... ];` holds, each an inner array ['a', 'b', ...],
    times the themes each one is checked in (a pair checked in light and in dark is two checks)."""
    text = read(path)
    if f"const {name} = [" not in text:
        return 0
    block = text.split(f"const {name} = [", 1)[1].split("];", 1)[0]
    return themes * len(re.findall(r"\[\s*['\"]", block))


def files(folder, pattern="*", skip=None):
    """How many files in a folder match `pattern`; with `skip`, leaving out those whose text contains it
    (a gallery page that says <meta name="checks" content="skip"> isn't one of the pages)."""
    return sum(1 for p in where(folder).glob(pattern)
               if p.is_file() and (skip is None or skip not in p.read_text(encoding="utf-8")))


# ---------------------------------------------------------------------------------------------------------
# How a count is written in the documents: a number, in digits ("1,240") or one of these words, then the
# fact's words. A number word that isn't in this list is never checked: add the ones your documents write.

WORDS = {"six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14}
NUMBER = r"(\d{1,3}(?:,\d{3})?|" + "|".join(WORDS) + r")"
BEFORE = r"(?<![\w.,-])"       # not inside "1.5", "v2-3" or "12,5"; "**40** tables" is read as 40

# One guard per line:
#   (name, how it's counted, its source, the words after the number, the floor[, a pattern of its own])
# - its source: the file or folder the count comes from, from docs/02-design (or from docs/ for 00-project);
#   while it doesn't exist, the guard is skipped;
# - the words: a regular expression right after the number ("tables\b" reads "40 tables"); None when the
#   guard gives a pattern of its own;
# - the floor: a number under it is a part, not the total ("the Accounts module's 4 tables"), and isn't
#   checked. None means half the source's count. When a part above that trips the check, set the floor just
#   above the part, with a comment naming it (110: "100 operations in one sync batch" is a limit, not the count);
# - a pattern of its own, instead of "the number, then the words": for a count whose number sits inside
#   the phrase ("the other 30 screens"); its first group that matched is the number.
# Two guards that share a word ("flows") are kept apart by their words (a lookahead) or by their floors.

ASVS = next((p.relative_to(design).as_posix() for p in sorted(design.glob("07-security/asvs-l[123].md"))),
            "07-security/asvs-l2.md")      # the list is named after the chosen level
ASVS_ROW = r"^\| `v\d+\.\d+\.\d+-[\d.]+` \| \d \| [^|]* \| (\w+) \|"   # | `v5.0.0-1.2.3` | 2 | What it asks | Applies |

FACTS = [
    # 01 System design --------------------------------------------------------------------------------
    # the alerts that reach the owner's phone: the rows of 09-monitoring's | Alert | When | What I do |
    ("alerts to the phone", lambda: table_rows("01-system-design/09-monitoring.md", "| Alert | When"),
     "01-system-design/09-monitoring.md", r"alerts to (?:my|the) phone\b", None),

    # 04 Data model -----------------------------------------------------------------------------------
    # the tables and the database schemas schema.sql creates, one statement at a line's start
    ("tables", lambda: lines("04-data-model/schema.sql", r"CREATE TABLE\b"),
     "04-data-model/schema.sql", r"tables\b", None),
    # "(?! with)": "90 schemas with fields" is the API's count, below
    ("database schemas", lambda: lines("04-data-model/schema.sql", r"CREATE SCHEMA\b"),
     "04-data-model/schema.sql", r"schemas\b(?! with)", None),
    # the entities: the rows of 01-entities' | Entity | Module | What it is |
    ("entities", lambda: table_rows("04-data-model/01-entities.md", "| Entity |"),
     "04-data-model/01-entities.md", r"entities\b", None),

    # 05 API design -----------------------------------------------------------------------------------
    # the API map's addresses: | # | Method | Path | Who | ..., one per method and path
    ("API addresses", lambda: addresses("05-api-design/02-map.md"),
     "05-api-design/02-map.md", r"(?:API )?addresses\b", None),
    # A part of the map that one rule covers, when the documents repeat its count: fill in the method, the
    # paths and the "Who" cell, then uncomment. E.g. "4 shared-item deletion addresses", each with its test:
    # ("shared-item deletion addresses",
    #  lambda: addresses("05-api-design/02-map.md", "DELETE", r"/api/v1/(?:<items>|<other items>)/\{id\}", "logged in"),
    #  "05-api-design/02-map.md", None, 1, BEFORE + NUMBER + r"\** shared-item deletion addresses\b"),
    # every operation in the contract; "(?! ...)": the operations behind the login are the next guard's
    ("operations in openapi.yaml", lambda: operations("05-api-design/openapi.yaml"),
     "05-api-design/openapi.yaml", r"operations\b(?! behind (?:a|the) login| that need (?:a|the) login)", None),
    # the operations that need the login, those the "no login, 401" guard test covers; "session": the login
    # scheme's name in your contract's components/securitySchemes
    ("operations behind a login", lambda: operations_behind("05-api-design/openapi.yaml", "session"),
     "05-api-design/openapi.yaml", r"operations (?:behind (?:a|the) login|that need (?:a|the) login)\b", None),
    ("schemas with fields in openapi.yaml", lambda: schemas_with_fields("05-api-design/openapi.yaml"),
     "05-api-design/openapi.yaml", r"schemas with fields\b", None),

    # 06 UI design ------------------------------------------------------------------------------------
    # the screens: the rows of every area's | Screen | Address | ... | Designed | table in the map;
    # "(?<!other )": "the other 30 screens" are the next guard's
    ("screens", lambda: table_rows("06-ui-design/02-map.md", "| Screen |", every=True),
     "06-ui-design/02-map.md", None, None, r"(?<!other )" + BEFORE + NUMBER + r"\** screens\b"),
    # the screens designed one slice ahead of their code: the "Designed" cell, the last, starts with "slice";
    # written "the other 30 screens", "the other 30 with their slice", "every other screen (30)"
    ("screens designed with their slice",
     lambda: table_rows("06-ui-design/02-map.md", "| Screen |", lambda cells: cells[-1].startswith("slice"), every=True),
     "06-ui-design/02-map.md", None, None,
     r"\bother (?:" + NUMBER + r"\** (?:screens\b|with their slice\b)|screens? \(" + NUMBER + r"\))"),
    # the main flows: one heading per flow in 03-flows ("## Flow 3 – ..."; change it to your heading);
    # written "eight flows with their failure paths", "the eight flows, UML activity diagrams"
    ("UI flows", lambda: lines("06-ui-design/03-flows.md", r"## Flow \d+ "),
     "06-ui-design/03-flows.md", None, None,
     BEFORE + NUMBER + r"\** flows\b(?= with their failure paths|, UML activity diagrams)"),
    # the contrast check's text/background pairs and two-band focus rings, each checked in the light and the dark theme
    ("contrast pairs", lambda: array_items("06-ui-design/checks/contrast.mjs", "PAIRS", themes=2),
     "06-ui-design/checks/contrast.mjs", r"pairs\b", None),
    ("two-band focus rings", lambda: array_items("06-ui-design/checks/contrast.mjs", "RINGS", themes=2),
     "06-ui-design/checks/contrast.mjs", r"(?:two-band (?:focus )?)?rings\b", None),
    # the pages the page check runs on; a gallery marked content="skip" isn't one
    ("UI wireframes", lambda: files("06-ui-design/wireframes", "*.html", skip='content="skip"'),
     "06-ui-design/wireframes", r"wireframe(?:s| pages)\b", None),
    ("UI mockups", lambda: files("06-ui-design/mockups", "*.html", skip='content="skip"'),
     "06-ui-design/mockups", r"mockup(?:s| pages)\b", None),

    # 07 Security -------------------------------------------------------------------------------------
    # the threats: one | T-nn | row each in 03-threats
    ("threats", lambda: lines("07-security/03-threats.md", r"\| T-\d+ "),
     "07-security/03-threats.md", r"threats\b", None),
    # the numbered flows on the security map (| # | From → to | ...); the lookahead leaves the UI flows above out
    ("flows on the security map", lambda: table_rows("07-security/02-map.md", "| # | From"),
     "07-security/02-map.md", r"flows\b(?! with their failure paths|, UML activity diagrams)", None),
    # the map's other ways in, not the API's addresses (a webhook's sender, the admin's shell, a backup's bucket)
    ("ways in that aren't addresses", lambda: table_rows("07-security/02-map.md", "| Way in |"),
     "07-security/02-map.md", r"ways in that aren't addresses\b", None),
    # the secrets' inventory: | Secret | Opens | Lives in | ...
    ("secrets", lambda: table_rows("07-security/07-data-and-secrets.md", "| Secret | Opens"),
     "07-security/07-data-and-secrets.md", r"(?:secrets|in the inventory)\b", None),
    # the owner's accounts that reach production, each with its second factor: | Account | Opens | Second factor | ...
    ("accounts that reach production", lambda: table_rows("07-security/09-infrastructure.md", "| Account | Opens"),
     "07-security/09-infrastructure.md", r"accounts that reach production\b", None),
    # the security events that alert: | Event | Logged | Alert when |, the threshold in bold, "—" for none
    ("security alerts",
     lambda: table_rows("07-security/10-detection-and-response.md", "| Event | Logged | Alert when",
                        lambda cells: cells[-1].startswith("**")),
     "07-security/10-detection-and-response.md", r"security alerts\b", None),
    # every protection with its check: | Protection | Check | Where | When | Tried on |
    ("protections with their check", lambda: table_rows("07-security/11-checks.md", "| Protection | Check |"),
     "07-security/11-checks.md", r"protections\b", None),
    # the ASVS list's answers, its "Applies" column: yes, no, deviation or gap; each gap is a rule for Build
    ("ASVS requirements met", lambda: lines(ASVS, ASVS_ROW, "yes"), ASVS, r"yes\b", None),
    ("ASVS deviations", lambda: lines(ASVS, ASVS_ROW, "deviation"), ASVS, r"(?:ASVS )?deviations\b", None),
    ("ASVS gaps", lambda: lines(ASVS, ASVS_ROW, "gap"), ASVS, r"(?:(?:ASVS )?gaps|rules for Build)\b", None),

    # 00 The project ----------------------------------------------------------------------------------
    # the decisions: one file each, NNNN-title.md
    ("ADRs", lambda: files("00-project/adr", "[0-9][0-9][0-9][0-9]-*.md"),
     "00-project/adr", r"(?:ADRs|architecture decisions)\b", None),
]

WHEN = re.compile(r"^[^.;,()]{0,20}?\b(at step|at this decision|at the decision|before |when drafted)")
JOURNAL = re.compile(r"^\s*- \d{4}-\d{2}-\d{2}")


def history():
    """The past counts kept on purpose: ("path from docs/", "text in the line") from facts-history.txt."""
    allowed = []
    path = here / "facts-history.txt"
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.strip() and not line.startswith("#"):
                file, _, text = line.partition(": ")
                allowed.append((file.strip(), text.strip()))
    return allowed


def main():
    counts = []
    for name, count, source, words, floor, *own in FACTS:
        if not where(source).exists():
            continue                                  # its source isn't written yet
        if not own and not words:
            sys.exit(f"facts.py: '{name}' needs the words after the number, or a pattern of its own")
        true = count()
        claim = re.compile(own[0] if own else BEFORE + NUMBER + r"\** " + words, re.I)
        counts.append((name, true, source, claim, true / 2 if floor is None else floor))
    allowed = history()
    wrong = []
    for md in sorted(docs.rglob("*.md")):
        rel = md.relative_to(docs).as_posix()
        if rel.startswith("02-design/09-architecture-overview/changes/") or "/node_modules/" in rel:
            continue
        for n, line in enumerate(md.read_text(encoding="utf-8").splitlines(), 1):
            if JOURNAL.match(line):
                continue
            # the spans of the past counts this line keeps on purpose
            kept = [(i, i + len(t)) for f, t in allowed if rel == f
                    for i in [m.start() for m in re.finditer(re.escape(t), line)]]
            for name, true, source, claim, floor in counts:
                for m in claim.finditer(line):
                    said = next(g for g in m.groups() if g).lower()
                    said = WORDS[said] if said in WORDS else int(said.replace(",", ""))
                    if (said < floor or said == true or WHEN.match(line[m.end():])
                            or any(a <= m.start() and m.end() <= b for a, b in kept)):
                        continue
                    wrong.append(f"{rel}:{n}: says {m[0]!r}; {source} has {true} {name}")
    for name, true, source, _, _ in counts:
        hint = "  (0: is its table written, and do the guard's header and pattern still find it?)" if true == 0 else ""
        print(f"{name}: {true} ({source}){hint}")
    skipped = len(FACTS) - len(counts)
    if skipped:
        print(f"({skipped} of {len(FACTS)} facts skipped: their source isn't written yet)")
    if wrong:
        print(f"\n{len(wrong)} stale counts (fix them, or list a past count kept on purpose in checks/facts-history.txt):")
        print("\n".join(wrong))
        sys.exit(1)
    print("\nEvery count in the documents matches its source.")


if __name__ == "__main__":
    main()
