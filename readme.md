# Lab: Hash Tables – Ransom Note Construction  
**Lab GitHub Repo**: [Hash Tables – Ransom Note](https://github.com/learn-co-curriculum/hash-table-ransom-note-lab)

---

## Overview
In this lab, you’ll apply **hash tables** to solve a classic technical challenge. You’ll implement a function that determines whether a **ransom note** can be constructed using the letters from a given **magazine**—with each letter only used once.

This is a realistic application of **frequency counting** and **fast lookup** using key-value data structures. Hash tables are essential in real-world systems where performance matters, such as caching, text indexing, or validating data availability.

---

## Task 1: Define the Problem

1. Implement a function that returns `True` if a `ransomNote` can be built using letters from `magazine`, and `False` otherwise.
2. Each letter in `magazine` may only be used **once**.
3. You must use a **hash table (dictionary)** to track character counts.

**The Challenge**: Demonstrate your ability to use a hash table for character tracking and conditional logic to support a frequency-matching use case.

---

## Task 2: Determine the Design

### Hash Table Functionality

- **File**: `ransom_note.py`
- **Function**:  
  - `can_construct(ransomNote: str, magazine: str) -> bool`  
  - Returns `True` if the ransom note can be formed from magazine letters, `False` otherwise.

---

## Task 3: Develop, Test, and Refine the Code

### Set Up

#### Fork and Clone
1. Go to the provided **GitHub repository link**.  
2. Fork the repository to your GitHub account.  
3. Clone the forked repository to your local machine.

#### Open and Run
1. Open the project in your Python-friendly IDE (VSCode, PyCharm, etc.).  

### Implementation Details

1. **Starter code uses `pass`**:
   - You’ll see `pass` in the `can_construct` function.
   - Replace it with your actual logic.

2. **Build the function**:
   - Track letter counts using a dictionary.
   - Decrement counts as you check the ransom note.
   - Return `False` early if a character is missing or depleted.

3. **Run Tests**:
   - Execute the test file with:
     ```bash
     python test_ransom_note.py
     ```
   - Ensure all tests pass before submission.

4. **Push and Merge**:
   - Commit your work regularly.
   - Push to your feature branch.
   - Open a Pull Request (PR).
   - Merge to `main` after review.

---

## Task 4: Document and Maintain

### Best Practice Documentation Steps

- **Comment your logic**: Especially around the hash table operations.
- **Explain your thinking** in your function definitions.
- **README**: Ensure this file accurately reflects how to run the project.
- **Clean Up**:
  - Remove any debug prints.
  - Make sure `.gitignore` ignores `.pyc`, `__pycache__`, etc.

---

## Submission
Once your lab is complete and all tests are passing:

- Push your code to GitHub.
- Submit the link to your repo through **Canvas using CodeGrade**.
