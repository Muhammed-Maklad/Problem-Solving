def multiply(num1: str, num2: str) -> str:
    if num1 == "0" or num2 == "0":
        return "0"

    m, n = len(num1), len(num2)
    arr = [0] * (m + n) 

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            mul = int(num1[i]) * int(num2[j])      
            sum_ = mul + arr[i + j + 1]            
            arr[i + j + 1] = sum_ % 10           
            arr[i + j] += sum_ // 10           

    result = "".join(map(str, arr)).lstrip("0")
    return result if result else "0"


# ✅ Test cases
print(multiply("2", "3"))       
print(multiply("123", "456"))   # 56088
print(multiply("99", "99"))     # 9801
print(multiply("0", "52"))      # 0
