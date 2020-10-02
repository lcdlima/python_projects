# Read an integer N. This value will be the amount of integer X values that will be read next.
# Show how many of these X values are within the range [10.20] and how many are outside the range, showing this information.

N = int(input())
i = 1
ins = 0
out = 0

while i <= N:
    num = int(input())
    i += 1
    if num >= 10 and num <= 20:
        ins += 1
    else:
        out += 1

print (('{} in').format (ins))
print (('{} out').format (out))