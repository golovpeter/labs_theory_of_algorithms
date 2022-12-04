import math

x = 0.5
y = 0.75

# Выражение u1
u1 = math.cos(x/y)**3 + math.sin(y/x)**3
# Выражение u2
u2 = math.cos(x*y)**2 + math.sin(x+y)**3

if u1 == u2:
    print("Выражение u1 равно u2")
elif u1 > u2:
    print("Выражение u1 больше u2")
else:
    print("Выражение u1 меньше u2")