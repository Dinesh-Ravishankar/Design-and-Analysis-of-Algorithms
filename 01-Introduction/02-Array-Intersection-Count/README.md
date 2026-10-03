# Experiment 02 — Array Intersection Count

## Aim

To find the number of common elements between two arrays.

## Problem Statement

Given two arrays, determine the number of elements that are present in both arrays.

## Algorithm

1. Read the elements of the first array.
2. Read the elements of the second array.
3. Traverse each element of the first array.
4. Check whether the element is present in the second array.
5. If the element is present, increase the count.
6. Display the intersection count.

## Approach

Brute Force / Sequential Search

## Complexity Analysis

Let:

* `n` = size of the first array
* `m` = size of the second array

| Case    | Time Complexity |
| ------- | --------------- |
| Best    | O(n)            |
| Average | O(n × m)        |
| Worst   | O(n × m)        |

Space Complexity: O(1)

## Input

```text
5
1 2 3 4 5
4
3 4 5 6
```

## Output

```text
Intersection count: 3
```

## Test Cases

### Test Case 1

Input:

```text
5
1 2 3 4 5
4
3 4 5 6
```

Expected Output:

```text
Intersection count: 3
```

### Test Case 2

Input:

```text
4
10 20 30 40
3
50 60 70
```

Expected Output:

```text
Intersection count: 0
```

## Key Concepts

* Arrays
* Sequential Search
* Brute Force
* Array Intersection

## Source Code

`array_intersection_count.py`
