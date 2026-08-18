"""
HackerRank Terminal Practice Test Runner Helper
Provides input/output redirection, test evaluation, and formatted output.
"""

import sys
import io
import time
from typing import List, Dict, Callable, Any

# ANSI Color formatting
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"


def normalize_output(text: str) -> str:
    """Strip trailing spaces from each line and trailing newline for clean comparisons."""
    if not text:
        return ""
    lines = [line.rstrip() for line in text.strip().splitlines()]
    return "\n".join(lines)


def run_single_test(solve_func: Callable, input_str: str, expected_str: str) -> Dict[str, Any]:
    """Runs a single test case against solve_func using sys.stdin and sys.stdout mocking."""
    old_stdin = sys.stdin
    old_stdout = sys.stdout

    sys.stdin = io.StringIO(input_str)
    sys.stdout = io.StringIO()

    start_time = time.perf_counter()
    error = None
    actual_out = ""

    try:
        # Call the user's solve function
        result = solve_func()
        # If solve_func returned a string/number (instead of printing), write to stdout
        if result is not None:
            sys.stdout.write(str(result) + "\n")
    except Exception as e:
        error = e
    finally:
        elapsed = (time.perf_counter() - start_time) * 1000
        actual_out = sys.stdout.getvalue()
        sys.stdin = old_stdin
        sys.stdout = old_stdout

    norm_expected = normalize_output(expected_str)
    norm_actual = normalize_output(actual_out)

    passed = (error is None) and (norm_expected == norm_actual)

    return {
        "passed": passed,
        "input": input_str,
        "expected": expected_str,
        "actual": actual_out,
        "norm_expected": norm_expected,
        "norm_actual": norm_actual,
        "error": error,
        "elapsed_ms": elapsed
    }


def run_tests(solve_func: Callable, test_cases: List[Dict[str, str]], problem_title: str = "Challenge Test Suite"):
    """
    Main runner function invoked by challenge files.
    """
    print(f"\n{BOLD}{CYAN}{'='*60}{RESET}")
    print(f"{BOLD}{CYAN} Running Tests for: {problem_title}{RESET}")
    print(f"{BOLD}{CYAN}{'='*60}{RESET}\n")

    passed_count = 0
    total_cases = len(test_cases)

    for i, tc in enumerate(test_cases):
        input_data = tc.get("input", "")
        expected_data = tc.get("expected", "")
        is_hidden = tc.get("hidden", False)
        tc_label = f"Testcase {i} {'(Hidden)' if is_hidden else '(Sample)'}"

        res = run_single_test(solve_func, input_data, expected_data)

        if res["passed"]:
            passed_count += 1
            print(f"  [{GREEN}PASS{RESET}] {tc_label} ({res['elapsed_ms']:.2f} ms)")
        else:
            print(f"  [{RED}FAIL{RESET}] {tc_label} ({res['elapsed_ms']:.2f} ms)")
            if res["error"]:
                print(f"     {RED}Runtime Error:{RESET} {res['error']}")
            else:
                if not is_hidden or tc.get("show_input_on_fail", True):
                    print(f"     {YELLOW}Input:{RESET}")
                    for line in input_data.strip().splitlines():
                        print(f"       {line}")
                    print(f"     {YELLOW}Expected Output:{RESET}")
                    for line in res["norm_expected"].splitlines():
                        print(f"       {line}")
                    print(f"     {YELLOW}Your Output:{RESET}")
                    for line in res["norm_actual"].splitlines():
                        print(f"       {line}")
            print()

    print(f"\n{BOLD}{'='*60}{RESET}")
    if passed_count == total_cases:
        print(f" {BOLD}{GREEN}CONGRATULATIONS! All {passed_count}/{total_cases} test cases passed! [SUCCESS]{RESET}")
    else:
        print(f" {BOLD}{RED}Result: {passed_count}/{total_cases} test cases passed.{RESET} Keep trying!")
    print(f"{BOLD}{'='*60}{RESET}\n")
