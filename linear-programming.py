import scipy.optimize

# Objective function: 50x + 80y
# Constraint 1: 5x + 2y <= 20
# Constraint 2: -10x + -12y <= -90

result = scipy.optimize.linprog(
    [50, 80],
    A_ub=[[5, 2], [-10, -12]],
    b_ub=[20, -90],
)

if result.success:
    print("x1: " + str(round(result.x[0], 2)))
    print("x2: " + str(round(result.x[1], 2)))
else:
    print("No possible solution")