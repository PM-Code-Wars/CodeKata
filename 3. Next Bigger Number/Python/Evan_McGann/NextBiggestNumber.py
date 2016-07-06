def next_bigger(n):
    digits = [int(digit) for digit in str(n)]
    for i in range(len(digits) - 2, -1, -1):
        curr_digit = digits[i]
        next_largest_digit = -1
        next_largest_index = -1
        
        for j in range(i + 1, len(digits)):
            next_digit = digits[j]
            if next_digit > curr_digit and (next_largest_digit == -1 or next_digit < next_largest_digit):
                next_largest_digit = next_digit
                next_largest_index = j
        
        if next_largest_index >= 0:
            digits[i] = next_largest_digit
            digits[next_largest_index] = curr_digit
            
            sorted_latter_digits = sorted([digits[k] for k in range(i + 1, len(digits))])
            
            for k in range(len(sorted_latter_digits)):
                digits[i + 1 + k] = sorted_latter_digits[k]
                
            return int("".join([str(digit) for digit in digits]))
    
    return -1
