# 🎲 Draw & Sum Even Numbers

A non-interactive command-line script that demonstrates modular programming in Python. It has one function to generate a list of five random numbers and a second function to process that list and calculate the sum of all its even numbers.

## Features

* **Modular Design**: The script is separated into two distinct functions: `draw()` for data generation and `sumeven()` for data processing.
* **Random Number Generation**: The `draw()` function populates a list with five random integers between 1 and 10.
* **Even Number Summation**: The `sumeven()` function iterates through the list, identifies all even numbers, and calculates their sum.

## How to Use

1.  Ensure you have Python installed.
2.  Save the code as a `.py` file (e.g., `draw_number_sum_even.py`).
3.  Run the script from your terminal:
    ```sh
    python draw_number_sum_even.py
    ```
4.  The script will automatically run, first displaying the numbers as they are "drawn," and then printing the final sum of the even numbers.

### Example Output

```sh
> python draw_number_sum_even.py
Drawing 5 values ​​from the list:  8, 3, 10, 2, 7, Done!
Adding the even values ​​of [8, 3, 10, 2, 7], we have 20
```
