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
            digits = digits[0:i+1] + sorted(digits[i+1:len(digits)])
                
            return int("".join([str(digit) for digit in digits]))
    
    return -1
