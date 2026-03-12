def isHappy(n):
    """
    :type n: int
    :rtype: bool
    """
    if n == 11 or n == 7 :
        return True
    elif n < 10 :
        return False
    
    else:
        sum = 0 
        while n > 0 :
            temp = n%10
            sum += temp*temp
            n= n//10
        return isHappy(sum) 
    

print(isHappy(19))