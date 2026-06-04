# Given a string, determine the length of the longest contiguous substring in which every character appears only once. Input 1: s="abcadefgh" Output 1: 8 Input 2 : s="aaaaa" Output 2: 1

# Input Format

# A single string containing lowercase English letters.

# Constraints

# 1 <= len(s) <= 10^5

# Output Format

# Print the length of the longest substring without repeating characters.

def longest_substring_without_repeating_characters(s):
    char_index_map = {}
    max_length = 0
    start = 0

    for end in range(len(s)):
        if s[end] in char_index_map and char_index_map[s[end]] >= start:
            start = char_index_map[s[end]] + 1
        char_index_map[s[end]] = end
        max_length = max(max_length, end - start + 1)

    return max_length


if __name__ == "__main__":
    import sys

    data = sys.stdin.read().strip()
    if not data:
        try:
            data = input().strip()
        except Exception:
            data = ""

    if not data:
        sys.exit(0)

    if (data[0] == '"' and data[-1] == '"') or (data[0] == "'" and data[-1] == "'"):
        data = data[1:-1]

    print(longest_substring_without_repeating_characters(data))