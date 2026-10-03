# Experiment 01 — First Palindromic String

## Aim

To find the first palindromic string from a given list of strings.

## Problem Statement

Given a list of strings, find and display the first string that reads the same forward and backward.

## Algorithm

1. Read the number of strings.
2. Read each string one by one.
3. Check whether the current string is a palindrome.
4. If the string is a palindrome, display it as the first palindromic string.
5. Stop the search.
6. If no palindromic string is found, display an appropriate message.

## Approach

Sequential Search with Palindrome Checking

## Complexity Analysis

Let:

* `n` = number of strings
* `m` = length of the string

| Case    | Time Complexity |
| ------- | --------------- |
| Best    | O(m)            |
| Average | O(n × m)        |
| Worst   | O(n × m)        |

Space Complexity: O(m)

## Input

```text
5
hello
world
level
radar
madam
```

## Output

```text
First palindromic string: level
```

## Test Cases

### Test Case 1

Input:

```text
4
apple
banana
level
computer
```

Expected Output:

```text
First palindromic string: level
```

### Test Case 2

Input:

```text
3
hello
world
computer
```

Expected Output:

```text
No palindromic string found.
```

## Key Concepts

* String processing
* Palindrome checking
* Sequential search
* String slicing

## Source Code

`first_palindromic_string.py`
