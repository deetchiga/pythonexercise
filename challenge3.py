def is_Power_of_four(n):
    while (n % 4 == 0):
         n = n/4;         
    return n == 1;

print(is_Power_of_four(16))
