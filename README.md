This repo contains a testing program for [42](https://42.fr/)'s project push_swap.

_I made this to check that my small input count sorting algorithms won't take an unreasonable amount of time,
or exceed the max instruction count._

What this does:
- Test all possible combinations of valid inputs, from argument count 1 to 5 included.
- Check that operation count is within limits.
- Display your program's execution time.
- Run the `checker` executable to verify that your outputs actually sort the inputs.
- Show the sequence of inputs that was given into each test.
- Clean and coloured output :)

> ⚠️ **Due to the limited argument count, you CAN'T rely on this test alone to validate your project.**
> 
> You'll need to go elsewhere to check: bad inputs error handling, negative numbers in inputs, input counts higher than 5.
> 
> From my experience, you should verify your code with a few different testers anyway.

# How to run

1. Clone this repo parallel to your project repo.
    ```
    ./push_swap/ (your project repo)
    ./this_tester/
    ```
    > ℹ️ The tester's folder name is not important: change it as you like.

2. The `./checker` executable included in this repository is the one downloaded from the exercise page, **for MacOS.**

   If you are on another OS or want to use another executable, just replace that file with the same name. 

3. `cd` inside this repo and run the tester:
    ```bash
   ./run.sh
    ```
   It will now check all combinations, for argument sizes 1-5 included.

# Important notes

At the time of writing this, there is no recap of how all tests went: you just have to scroll through the results.

Green parameters are good.

Orange parameters are still good, but a bit closer to the limit.

> ℹ️ **Note that the thresholds for orange are just my arbitrary choice.**

Red means it's beyond the limits **with the exception of execution time, read below**.

> ⚠️ **Note that execution time will show up for 10 seconds and more, which, as far as I know, is only my arbitrary choice of value.**
> 
> I don't actually know if that should count as a timeout in an evaluation.
