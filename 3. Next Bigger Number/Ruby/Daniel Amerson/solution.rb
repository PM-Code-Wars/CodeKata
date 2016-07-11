require 'ostruct'

def next_bigger(n)
  if n < 10
    return -1
  end

  indexes_to_swap = get_indexes_to_swap(n)
  
  if indexes_to_swap.sink == -1
    return -1
  else
    digits = n.to_s.each_char.each_slice(1).map{|num| num.join()}
    source_val = digits[indexes_to_swap.source]
    digits[indexes_to_swap.source] = digits[indexes_to_swap.sink]
    digits[indexes_to_swap.sink] = source_val
    
    head = digits[0..indexes_to_swap.sink]
    tail = digits[indexes_to_swap.sink + 1..digits.length - 1].sort_by {|x| x}
    
    return head.concat(tail).join().to_i
  end
end
  
  
def get_indexes_to_swap(n)
  result = OpenStruct.new
  result.sink = -1
  result.source = -1
  
  if n < 10
    return result
  end

  digits = n.to_s.each_char.each_slice(1).map{|num| num.join()}
  last_digit = digits[digits.length - 1]
  rest = digits[0..digits.length - 2]
  
  best_result_from_rest = get_indexes_to_swap(rest.join().to_i)
  
  result.source = digits.length - 1
  
  for index in (digits.length - 2).downto(0)
    if digits[index] < last_digit
      result.sink = index
      
      break
    end
  end
  
  if result.sink == -1 && best_result_from_rest.sink == -1
    return result
  elsif result.sink > best_result_from_rest.sink
    return result
  elsif best_result_from_rest.sink > result.sink
    return best_result_from_rest
  elsif digits[result.source] < digits[best_result_from_rest.source]
    return result
  else
    return best_result_from_rest
  end
end