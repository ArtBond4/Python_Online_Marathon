import cmath

def solve_quadric_equation(a, b, c):
    try:
        
        x1 = (-b - (b * b - 4 * a * c) ** 0.5) / (2 * a)
        x2 = (-b + (b * b - 4 * a * c) ** 0.5) / (2 * a)
        
        return f"The solution are x1={complex(x1)} and x2={complex(x2)}"

    except ZeroDivisionError:
        return f"Zero Division Error"

    except TypeError:
        return f"Could not convert string to float"
