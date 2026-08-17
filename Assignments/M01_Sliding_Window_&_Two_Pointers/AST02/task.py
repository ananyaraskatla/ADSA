def Check_Palindrome(n: int, s: str) -> bool:
    left, right = 0, n - 1
    deleted = False

    while left < right:
        if s[left] != s[right]:
            if s[left + 1:right + 1] == s[left + 1:right + 1][::-1]:
                return True
            if s[left:right] == s[left:right][::-1]:
                return True
            return False

        left += 1
        right -= 1

    return True


if __name__ == '__main__':
    n = int(input())
    s = input()
    print(Check_Palindrome(n, s))