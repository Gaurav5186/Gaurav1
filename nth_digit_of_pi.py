from mpmath import mp

def nth_digit_of_pi(n):
    mp.dps = n + 2  # Set precision to get N digits
    pi_str = str(mp.pi)
    return int(pi_str[n + 1])

result = nth_digit_of_pi(100)
print(result)
