from typing import Dict

class Trie:
    """
    A trie (pronounced as "try") or prefix tree is a tree data structure that is used to efficiently store and retrieve keys in a dataset of strings.
    It is particularly useful for tasks such as autocomplete, spell checking, and IP routing.
    The trie is a tree-like data structure where each node represents a character of a string.
    The root node represents an empty string, and each edge represents a character in the string.
    The path from the root to a node represents a prefix of the string.
    The trie has the following properties:
    1. Each node can have multiple children, each representing a different character.
    2. Each node has a boolean value indicating whether it represents the end of a word.
    3. The trie can be traversed from the root to any node to find all words that start with a given prefix.
    4. The trie can be used to find the longest common prefix of a set of strings.
    5. The trie can be used to find all words that start with a given prefix.
    6. The trie can be used to find all words that are anagrams of a given word.
    7. The trie can be used to find all words that are a substring of a given word.
    8. The trie can be used to find all words that are a superstring of a given word.
    9. The trie can be used to find all words that are a subsequence of a given word.
    10. The trie can be used to find all words that are a supersequence of a given word.
    """

    def __init__(self):
        self.terminal: bool = False
        self.children: Dict[str, Trie] = {}

    def insert(self, word: str) -> None:
        if len(word) > 0:   # It can be ignored for leetcode specific problem since len(word) >= 1
            curr_char: str = word[0]
            if not self.children.get(curr_char):
                self.children[curr_char] = Trie()
            if len(word) == 1:
                self.children[curr_char].terminal = True
                return
            self.children[curr_char].insert(word[1:])

    def search(self, word: str) -> bool:
        if len(word) > 0:   # It can be ignored for leetcode specific problem since len(word) >= 1
            curr_char: str = word[0]
            if not self.children.get(curr_char):
                return False
            if len(word) == 1:
                return self.children[curr_char].terminal
            return self.children[curr_char].search(word[1:])
        return False

    def startsWith(self, prefix: str) -> bool:
        if len(prefix) > 0:   # It can be ignored for leetcode specific problem since len(prefix) >= 1
            curr_char: str = prefix[0]
            if not self.children.get(curr_char):
                return False
            if len(prefix) == 1:
                return True
            return self.children[curr_char].startsWith(prefix[1:])
        return False


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("apple")
param_2 = obj.search("apple")
param_3 = obj.search("app")
param_4 = obj.startsWith("app")

print(param_2, param_3, param_4)