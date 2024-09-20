a, b = input().split()
a="".join(reversed(a))
b="".join(reversed(b))
print(a if a>b else b)
