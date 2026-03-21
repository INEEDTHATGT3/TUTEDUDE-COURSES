def safe_divide(numerator, denominator):
    try:
        # Attempted conversions
        return float(numerator) / float(denominator)
    
    except ZeroDivisionError:
        raise ZeroDivisionError("Math Error: Denominator cannot be zero.")
    
    except ValueError:
        # Triggered when content is wrong: e.g., float("abc")
        raise ValueError("Value Error: string should contain some numbers.")
    
    except TypeError:
        # Triggered when data type is wrong: e.g., float([10, 20])
        raise TypeError("Type Error: Input must be a string, int, or float.")
    
def calculate_bill(prices):
    # total sum with error handiling 
    total = 0
    for p in prices:
        try:
            if not isinstance(p, (int, float)):
                raise TypeError(f"Invalid type: {type(p)}")
            if p < 0:
                raise ValueError("Negative price skipped")
            total += p
        except (TypeError, ValueError) as e:
            print(f"Internal Log: {e}")
    return total 
