import sys


def levenstein(a, b):
    dp = [[0] * (len(b) + 1) for i in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            dp[i][j] = min(min(dp[i - 1][j] + 1, dp[i][j - 1] + 1), dp[i - 1][j - 1] + int(a[i - 1] != b[j - 1]))
    print(1 - dp[len(a)][len(b)] / len(a))


def normalize(s):
    newS = ""
    for i in range(len(s)):
        if s[i] == '#':
            while i < len(s) and s[i] != '\n':
                i += 1
        newS += s[i]
    newS = newS.replace(" ", "")
    newS = newS.replace("\n", "")
    return newS


arguments = sys.argv
with open(arguments[1], 'r') as file:
    lines = [line.rstrip() for line in file]
for line in lines:
    file1, file2 = line.split()
    with open(file1, 'r') as file:
        lines1 = file.read()
    with open(file2, 'r') as file:
        lines2 = file.read()
    normal_lines1 = normalize(lines1)
    normal_lines2 = normalize(lines2)
    levenstein(normal_lines1, normal_lines2)
