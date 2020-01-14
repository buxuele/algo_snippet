# 这个基本上是自己完成的。

def sovle(s):
    s = s.strip()
    if " " in s:
        if s.endswith(" "):
            return len(s.replace(" ", ""))
        else:
            temp = s.split(" ")[-1]
            if temp:
                return len(temp)
            else:
                return 0
    else:
        return len(s)

s = "b a "
print(sovle(s))
