print("Name-hanan seid, ID-UGR/5797/16, section-17")
print("a.")
i = 5
k = 0
while k < i:
    n = 0
    while n < k + 1:
        print("*", end=" ")
        n += 1
    n = 0
    while n < (i - k):
        print(" ", end=" ")
        n += 1
    print()
    k += 1


print("b.")
k = 5
i = 0
while i < k:
    j = 0
    while j < (k-i):
        print(" ", end=" ")
        j += 1
    j = 0
    while j < i + 1:
        print("*", end=" ")
        j += 1
    print()
    i += 1


print("c.")
h = 4
i = 0
while i < h:
    j = 0
    while j < (h-i):
        print(" ", end=" ")
        j += 1
    j = 0
    while j < i + 1:
        print("*", end=" ")
        j += 1
    j = 0
    while j < i:
        print("*", end=" ")
        j += 1
    print()
    i += 1


print("d.")
k = 4
i = 0
while i < k:
    j = 0
    while j < i + 1:
        print("*", end=" ")
        j += 1
    j = 0
    while j < (k - i):
        print(" ", end=" ")
        j += 1
    print()
    i += 1

n = 5
i = 0
while i <= 5:
    j = 0
    while j < (n - i):
        print("*", end=" ")
        j += 1
    j = 0
    while j < n + 1:
        print(" ", end=" ")
        j += 1
    print()
    i += 1
