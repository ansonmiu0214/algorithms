## Problem
The `i`-th person has weight `people[i]`, and each boat can carry a maximum weight of `limit`.

Each boat carries at most 2 people at the same time, provided the sum of the weight of those people is at most `limit`.

Return the minimum number of boats to carry every given person.  (It is guaranteed each person can be carried by a boat.)

**Note:**
* `1 <= people.length <= 50000`
* `1 <= people[i] <= limit <= 30000`

## Examples
```
Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)
```
```
Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)
```
```
Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)
```

[Source](https://leetcode.com/problems/boats-to-save-people/description/)

## Approach
Greedy approach to match the heaviest passenger with the lightest on the same boat. If the weight exceeds, load the heavier one first and try match the next alternative with the lightest one.

* O(n(log(n))) for sorting the passengers + O(n) boat-matching iteratino = O(n(log(n))) running time complexity, where n is the number of people
* O(1) space complexity since in-place sorting is used
