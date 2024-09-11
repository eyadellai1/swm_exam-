
coverage_tracker = {
    'ldexp_line_1': 0,
    'ldexp_line_2': 0,
    'ldexp_line_3': 0
}

def tracked_ldexp(x, i):

    coverage_tracker['ldexp_line_1'] += 1
    

    result = x * (2 ** i)
    

    coverage_tracker['ldexp_line_2'] += 1
    
    return result
