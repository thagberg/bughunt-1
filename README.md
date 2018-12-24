# Bug Hunt

## FizzBuzz

FizzBuzz is a common programming "challenge" which tests the programmer's understanding of common constructs like branching, iteration, and discrete logic.  

The rules are simple:
* Iterate over a range of integers
* For each value which is a multiple of 3, print "Fizz"
* For each value which is a multiple of 5, print "Buzz"
* For each value which is a multipole of both 3 and 5, print "FizzBuzz"
* For all other values, simply print the value itself

When iterating over the range `[1, 2, ..., 5]`, we would expect the following output:
```
> 1
> 2
> Fizz
> 4
> Buzz
```

The included file `fizzbuzz.py` has a simple implementation of the FizzBuzz challenge, however something is not quite right.  Running `run.sh` will execute the unit tests defined in `test.py` for the FizzBuzz challenge.  Fix any bugs in the given FizzBuzz implementation and ensure that all unit tests are passing.