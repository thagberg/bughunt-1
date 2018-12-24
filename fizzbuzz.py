def fb_test(n):
    if n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    elif n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    else:
        return n

def fizz_buzz(num):
   for n in range(num+1):
       print(fb_test(n))

if __name__ == "__main__":
    fizz_buzz(15)