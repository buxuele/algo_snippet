from string import ascii_letters


# a = "Test1ng-Leet=code-Q!"
# a = "a-bC-dEf-ghIj"
# a = "7_28]"

a = "?6C40E"        #

s = list(a)

# 2个指针，分别从头和尾部开始走。
i = 0
j = len(s)-1
while i < j:
    while s[i] not in ascii_letters :
        i += 1
        print(i)
    while s[j] not in ascii_letters:
        j -= 1

    print("hahahhahahhah", i, j, s[i], s[j])

    if i < j :

        s[i], s[j] = s[j], s[i]
        print(''.join(s))
        print()

        i += 1
        j -= 1
    else:
        break
print("yes")
print(''.join(s))











