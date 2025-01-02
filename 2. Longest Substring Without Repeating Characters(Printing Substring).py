
def longest_substring(string: str) -> int:
    dic = {}
    start = 0
    max_length = 0

    for i in range(len(string)):
        if string[i] in dic:
            start = max(start,dic[string[i]]+1)
        dic[string[i]] = i

        current_length = i - start + 1
        if current_length>max_length:
            max_length=current_length
            max_substring = string[start:i+1]
    print(f"Longest Sub String {max_substring}")
    return max_length

s = input("Enter any String ")
print(longest_substring(s))

