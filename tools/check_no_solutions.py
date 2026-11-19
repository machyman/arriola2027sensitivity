"""check_no_solutions.py -- fail if the repository holds a worked-solution file or solution markup.

Usage:
  python3 tools/check_no_solutions.py [ROOT]     scan ROOT (default: the repository root)
  python3 tools/check_no_solutions.py --self-test

A public repository keeps every pushed file in its history, so this check is an alarm, not a lock: run it
before uploading, and the workflow runs it after every push. It flags
  - a file whose name suggests solutions (solution, answer key, instructor, held set), and
  - LaTeX solution markup in a text file: \\begin{solution}, \\solpart, \\solnote.
This script and its workflow are the only names allowed to contain "solution".
Exit status: 0 clean, 1 if anything is flagged.
"""
import re
import sys
import tempfile
from pathlib import Path

NAME = re.compile(r"solution|answer[-_ ]?key|instructor|held[-_ ]?set", re.I)
MARKUP = re.compile(r"\\begin\{solution\}|\\solpart\b|\\solnote\b")
TEXT = {".tex", ".md", ".txt", ".ipynb", ".py", ".m", ".json", ".yml", ".yaml", ".cff", ".bib", ".html"}
ALLOWED = {"tools/check_no_solutions.py", ".github/workflows/no_solutions_check.yml"}


def scan(root):
    root = Path(root)
    hits = []
    for p in sorted(root.rglob("*")):
        rel = p.relative_to(root).as_posix()
        if not p.is_file() or rel.startswith(".git/") or rel in ALLOWED:
            continue
        if NAME.search(p.name):
            hits.append(f"file name: {rel}")
        if p.suffix.lower() in TEXT or p.suffix.lower() == ".pdf":
            data = p.read_bytes()
            if p.suffix.lower() == ".pdf":
                if re.search(rb"(?i)solution", data[:200000]):
                    hits.append(f"PDF mentions solutions (check by eye): {rel}")
            elif MARKUP.search(data.decode("utf-8", errors="ignore")):
                hits.append(f"solution markup: {rel}")
    return hits


def self_test():
    with tempfile.TemporaryDirectory() as d:
        d = Path(d)
        (d / "software").mkdir()
        (d / "software" / "ok.py").write_text("print('fine')\n")
        clean = scan(d)
        (d / "docs").mkdir()
        (d / "docs" / "solutions_manual_v2.pdf").write_bytes(b"%PDF-1.5 Solutions")
        (d / "ch3.tex").write_text("\\begin{solution} x \\end{solution}\n")
        (d / "notes.md").write_text("\\solpart{a} 42\n")
        dirty = scan(d)
    ok = clean == [] and len(dirty) == 4
    print("self-test:", "PASS" if ok else f"FAIL clean={clean} dirty={dirty}")
    return 0 if ok else 1


if __name__ == "__main__":
    if sys.argv[1:] == ["--self-test"]:
        sys.exit(self_test())
    root = sys.argv[1] if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent
    hits = scan(root)
    for h in hits:
        print("FLAG", h)
    print(f"{len(hits)} flagged")
    sys.exit(1 if hits else 0)
