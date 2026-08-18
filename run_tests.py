"""
Master HackerRank Practice Test Runner & Progress Tracker
Scans all subdirectories for practice questions and reports solved status.
Usage:
    python run_tests.py              # Run all challenges
    python run_tests.py 01_syntax    # Run only track 01
"""

import os
import sys
import glob
import importlib.util
from pathlib import Path

# Ensure UTF-8 output if supported, else ASCII fallbacks
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"


def discover_and_run(target_filter: str = None):
    root_dir = Path(__file__).parent.resolve()
    q_files = glob.glob(str(root_dir / "**" / "q*.py"), recursive=True)
    m_files = glob.glob(str(root_dir / "**" / "m*.py"), recursive=True)
    py_files = sorted(q_files + m_files)

    if not py_files:
        print(f"{YELLOW}No challenge files found!{RESET}")
        return

    if target_filter:
        py_files = [f for f in py_files if target_filter in f]

    print(f"\n{BOLD}{CYAN}{'='*70}{RESET}")
    print(f"{BOLD}{CYAN}      HACKERRANK PYTHON PRACTICE SUITE - MASTER SCOREBOARD      {RESET}")
    print(f"{BOLD}{CYAN}{'='*70}{RESET}\n")

    total_challenges = 0
    solved_challenges = 0
    track_stats = {}

    from test_helper import run_single_test

    for filepath in py_files:
        rel_path = os.path.relpath(filepath, root_dir)
        folder = os.path.dirname(rel_path) or "root"
        filename = os.path.basename(rel_path)

        if folder not in track_stats:
            track_stats[folder] = {"total": 0, "solved": 0}

        # Import module dynamically
        spec = importlib.util.spec_from_file_location("module", filepath)
        module = importlib.util.module_from_spec(spec)
        
        try:
            spec.loader.exec_module(module)
        except Exception as e:
            print(f"[{RED}ERROR{RESET}] Could not import {rel_path}: {e}")
            continue

        if not hasattr(module, "solve") or not hasattr(module, "TEST_CASES"):
            continue

        solve_func = getattr(module, "solve")
        test_cases = getattr(module, "TEST_CASES")
        title = getattr(module, "TITLE", filename)
        points = getattr(module, "POINTS", 10)

        total_challenges += 1
        track_stats[folder]["total"] += 1

        # Run test cases
        all_passed = True
        passed_count = 0
        for tc in test_cases:
            res = run_single_test(solve_func, tc.get("input", ""), tc.get("expected", ""))
            if res["passed"]:
                passed_count += 1
            else:
                all_passed = False

        status_badge = f"{GREEN}SOLVED [OK]{RESET}" if all_passed else f"{RED}UNSOLVED ({passed_count}/{len(test_cases)}){RESET}"

        if all_passed:
            solved_challenges += 1
            track_stats[folder]["solved"] += 1

        print(f"  * [{folder}] {title:<38} | {status_badge}")

    print(f"\n{BOLD}{CYAN}{'='*70}{RESET}")
    print(f"{BOLD} SUMMARY BY TRACK:{RESET}")
    for track, data in track_stats.items():
        percent = (data['solved'] / data['total'] * 100) if data['total'] > 0 else 0
        print(f"   - {track:<28}: {data['solved']}/{data['total']} Solved ({percent:.0f}%)")

    overall_percent = (solved_challenges / total_challenges * 100) if total_challenges > 0 else 0
    print(f"\n{BOLD} OVERALL PROGRESS: {GREEN if overall_percent == 100 else YELLOW}{solved_challenges}/{total_challenges} Challenges Solved ({overall_percent:.1f}%){RESET}")
    print(f"{BOLD}{CYAN}{'='*70}{RESET}\n")


if __name__ == "__main__":
    filter_arg = sys.argv[1] if len(sys.argv) > 1 else None
    discover_and_run(filter_arg)
