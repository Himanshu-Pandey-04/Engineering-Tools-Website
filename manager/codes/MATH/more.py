def addNums(lst1, lst2, *args):
    """
    Numbers Adder
    =============
    Given a list of list of digits of numbers, the function returns the list of digits of the resulting sum.
    The lists(numbers) can be of different sizes
    
    Parameters
    ----------
    1. lst1 : list - digits of first number
    2. lst2 : list - digits of second number
    3. *args : (Optional) list of lists - more numbers

    Returns
    -------
    the list of digits of the resulting Sum (carry considered)

    Example
    -------
    >>> num1 = [7, 6, 9, 8, 8]              # Depicts number 76988
    >>> num2 = [5, 9, 2]                    # Depicts number 592
    >>> num3 = [3, 5, 1, 7, 4]              # Depicts number 35174
    >>> print(addNums(num1, num2, num3))    # Output: [1, 1, 2, 7, 5, 4] (112754)
    """

    numsIters = [iter(num[::-1]) for num in [lst1, lst2] + list(args)]  # make the iterators for each list
    carry, final = 0, []                                                # Initially carry is 0, 'final' will store the result
    
    while True:
        nums = [next(num, None) for num in numsIters]                   # for every num in numIters, get the next element if exists, else None
        if all(nxt is None for nxt in nums): break                      # If all numIters returned None, it means all numbers have exhausted, hence break from the loop
        nums = [(0 if num is None else num) for num in nums]            # Convert all 'None' to '0'
        digit = sum(nums) + carry                                       # Sum up all digits and carry
        final.append(digit % 10)                                        # Insert the 'ones' digit of result into final list
        carry = digit // 10                                             # get the 'tens' digit and update it to carry

    if carry: final.append(carry)                                       # If carry is non-zero, insert it
    return final[::-1]                                                  # return the fully generated final list

