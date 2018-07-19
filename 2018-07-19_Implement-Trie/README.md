## Problem
Implement a trie with `insert`, `search`, and `startsWith` methods.

**Notes:**
* You may assume that all inputs are consist of lowercase letters `a-z`.
* All inputs are guaranteed to be non-empty strings.

## Example
```
Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
```

[Source](https://leetcode.com/problems/implement-trie-prefix-tree/description/)
