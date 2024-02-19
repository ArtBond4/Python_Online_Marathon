def run_calc(a, b, op):
    try:
        print(calc(a, b, op))

    except TypeError:
        print("TypeError")
        
    except ZeroDivisionError:
        print("Division by zero")
        
    except ValueError:
        print("Incorrect operation is obtained")

    finally:
        print("End of calculation")
