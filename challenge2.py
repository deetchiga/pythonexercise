def is_Power_of_three(n):
    while (n % 3 == 0):
         n /= 3;         
    return n == 1;

print(is_Power_of_three(9))

