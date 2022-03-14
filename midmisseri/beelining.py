import math

(b, c) = tuple(float(x) for x in input().split())
target = c / math.log(b)
low = 0
high = 100
t = (high + low) / 2
calc = pow(b, t) * pow(t + 1, 2)
while abs(calc - target) < 100000:
    if calc < target:
        low = t
    if calc > target:
        high = t

    t = (high + low) / 2
    calc = pow(b, t) * pow(t + 1, 2)
time = pow(b, t) + c / (t + 1)
print(time)
