from operations.basic import add

def multiply(a, b):
    result = 0
    for _ in range(b):
        result = add(result, a)
    return result

def power(base, exponent):
    result = 1
    for _ in range(exponent):
        result = multiply(result, base)
    return result