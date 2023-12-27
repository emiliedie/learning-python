from sympy import symbols, solve, Eq

x = symbols('x')

answer = solve(Eq(x * 2 + 2 * x + 1, 5), x)

print(answer)

x = 8
y = 6

print(x + y)

x = 10

print(x + y)