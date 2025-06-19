import numpy as np

def solve_polynomial(coefficients):
    coefficients = np.trim_zeros(coefficients, trim='f')
    
    if len(coefficients) <= 1:
        print("Not a valid polynomial.")
        return []

    roots = np.roots(coefficients)
    return roots

def display_polynomial(coeffs):
    degree = len(coeffs) - 1
    terms = []
    for i, coef in enumerate(coeffs):
        power = degree - i
        if coef == 0:
            continue
        
        sign = "+" if coef > 0 and i > 0 else ""
        coef_str = f"{abs(coef)}" if abs(coef) != 1 or power == 0 else ""
        var_str = "" if power == 0 else "x" if power == 1 else f"x^{power}"
        terms.append(f"{sign}{'-' if coef < 0 else ''}{coef_str}{var_str}")
    return " ".join(terms) + " = 0"

def main():
    print("Polynomial Equation Solver")
    print("You will enter the degree of the polynomial, then the coefficients.")
    print("Example: for 2x^3 - 4x + 1, degree is 3 and coefficients are: 2 0 -4 1")
    
    degree_input = input("Enter the degree of the polynomial: ")
    if degree_input.lower() == 'quit':
        print("Goodbye!")

    try:
        degree = int(degree_input)
        if degree < 1:
            print("Degree must be at least 1.")

        coefficients = []
        for i in range(degree, -1, -1):
            while True:
                coef_input = input(f"Enter the coefficient for x^{i}: ")
                if coef_input.lower() == 'quit':
                    print("Goodbye!")
                    return
                try:
                    coef = float(coef_input)
                    coefficients.append(coef)
                    break
                except ValueError:
                    print("Invalid number, please try again.")

        print("\nPolynomial entered:")
        print(display_polynomial(coefficients))

        roots = solve_polynomial(coefficients)
        print("\nThe roots of the equation are:")
        for i, root in enumerate(roots, start=1):
            print(f"x{i} = {root}")
        print("\n---\n")
    except ValueError:
        print("Invalid degree! Please enter a whole number.")

# Run the program
if __name__ == '__main__':
    main()
