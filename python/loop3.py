# home task 3 lab3
num = int(input("Enter an integer: "))

prime = True
perfect = False
divisors_sum = 1

for i in range(2, num):
    if num % i == 0:
        prime = False
        divisors_sum += i

if divisors_sum == num:
    perfect = True

if prime and not perfect:
    print(num, "is a prime number.")
elif perfect and not prime:
    print(num, "is a perfect number.")
elif not prime and not perfect:
    print(num, "is not prime or perfect.")

