# Given a string s and an integer k, repeatedly remove any group of exactly k consecutive identical characters.

# Continue until no more removals are possible.

# Return the final string. Input : s = "deeedbbcccbdaa" k = 3

# Explanation : deeedbbcccbdaa

# remove "eee" ddbbcccbdaa

# remove "ccc" ddbbbdaa

# remove "bbb" dddaa

# remove "ddd" aa

# Output : aa

# Input Format

# First line contains a string s.

# Second line contains an integer k.

# Constraints

# 1 ≤ len(s) ≤ 100000 2 ≤ k ≤ 10000 s contains lowercase English letters

# Output Format

# Print the final string after all removals.

def removeDuplicates(s: str, k: int) -> str:
    stack = []
    for ch in s:
        if stack and stack[-1][0] == ch:
            stack[-1][1] += 1
            if stack[-1][1] == k:
                stack.pop()
        else:
            stack.append([ch, 1])
    return ''.join(ch * count for ch, count in stack)


def main() -> None:
    import sys

    data = sys.stdin.read().strip().split()
    if len(data) < 2:
        return

    s = data[0]
    try:
        k = int(data[1])
    except ValueError:
        return

    print(removeDuplicates(s, k))


if __name__ == '__main__':
    main()