s = input()
print(s[::-1] == s)

# TODO оптимизируйте код, написанный ниже
for i in range(len(s)):
    if s[i] != s[-1 - i]:
        print(False)
        break
else:
    print(True)
