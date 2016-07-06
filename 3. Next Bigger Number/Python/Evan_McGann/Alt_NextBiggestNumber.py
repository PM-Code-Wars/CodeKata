def next_bigger(n):
    digits = [int(digit) for digit in str(n)]
    for i in range(len(digits) - 2, -1, -1):
        curr_digit = digits[i]
        next_largest_digit = min([digit for digit in digits[i+1:len(digits)] if digit > curr_digit] or [-1])
        
        if next_largest_digit > curr_digit:
            next_largest_index = len(digits) - digits[::-1].index(next_largest_digit) - 1
            digits[i] = next_largest_digit
            digits[next_largest_index] = curr_digit
            digits = digits[0:i+1] + sorted(digits[i+1:len(digits)])
                
            return int("".join([str(digit) for digit in digits]))
    
    return -1
