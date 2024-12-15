
def longest_substring(string: str) -> int:
    dic = {}
    start = 0
    max_length = 0

    for i in range(len(string)):
        if string[i] in dic:
            start = max(start,dic[string[i]]+1)
        dic[string[i]] = i
        max_length = max(max_length,i-start+1)

    return max_length

s = input("Enter any String ")
print(longest_substring(s))

