# HackerRank Python Practice Workspace 🚀

Welcome to your offline **HackerRank Python Practice Suite**! This directory is equipped with 30 curated Python challenges structured identically to HackerRank problem statements, complete with input parsing stubs, test case runners, and score tracking.

---

## 📁 Directory Structure

```text
d:\py\
├── 01_syntax_and_basics\       # Print, If-Else, Arithmetic, Division, Loops, Functions, Leap Year
├── 02_data_structures\         # List Comprehensions, Runner-Up, Nested Lists, Dictionaries, Counter, DefaultDict
├── 03_strings_and_regex\       # Swap Case, Split/Join, Substrings, Text Wrap, Door Mat, Capitalize
├── 04_functional_and_builtins\ # Zipped, Any/All, Map & Lambda (Fibonacci)
├── 05_classes_and_oop\         # Complex Numbers, Torsional Angle (3D Vector operations)
├── 06_algorithms_and_math\     # Itertools Product, Permutations, Merge the Tools
├── 07_leetcode_hackerrank_medium\ # 10 Medium Problems (Two Sum II, Group Anagrams, 3Sum, Product Except Self, etc.)
├── test_helper.py              # Test suite execution engine
├── run_tests.py                # Master scoreboard and progress tracker
└── README.md
```

---

## 🎯 How to Practice

### Step 1: Open any challenge file
Open a challenge file in your editor (e.g. `01_syntax_and_basics/q01_say_hello_world.py`).

### Step 2: Read the Problem Statement
Each file starts with a detailed docstring header formatted like HackerRank:
- **Problem Statement** & Task
- **Input Format** & **Constraints**
- **Output Format**
- **Sample Input** & **Sample Output** with **Explanation**

### Step 3: Write your solution in `solve()`
Find the `def solve():` function stub (or specific function stub) and write your Python code.

### Step 4: Test your solution!
Run the Python script directly from your terminal:
```bash
python 01_syntax_and_basics/q01_say_hello_world.py
```
Your code will automatically run against **Sample Test Cases** and **Hidden Test Cases**, outputting a HackerRank test matrix with timing and status:
```text
============================================================
 Running Tests for: Say Hello, World! With Python
============================================================

  [✓ PASSED] Testcase 0 (Sample) (0.12 ms)

============================================================
 CONGRATULATIONS! All 1/1 test cases passed! 🎉
============================================================
```

### Step 5: Stuck? Check the Solution Hint!
At the very bottom of each file, a commented solution block is provided so you can check how to write clean, idiomatic Python code.

---

## 📊 Check Your Score & Progress

To see your overall score across all tracks, run:
```bash
python run_tests.py
```

To run tests for a specific track:
```bash
python run_tests.py 01_syntax
```

Happy Coding! 🐍✨
