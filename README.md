# Convolution
Code example of convolution in Python for equal length arrays

Inspired by 3Blue1Brown 
https://youtu.be/KuXjwB4LzSA

For production purposes use numpy.convolve()
https://numpy.org/doc/stable/reference/generated/numpy.convolve.html

## Example of probability using convolution
Given a pair of dice calculate the chance for each roll

```
Dice roll: 2  Chance to drop: 02.78%  Possible combinations: [1] [1]
Dice roll: 3  Chance to drop: 05.56%  Possible combinations: [1, 2] [2, 1]
Dice roll: 4  Chance to drop: 08.33%  Possible combinations: [1, 2, 3] [3, 2, 1]
Dice roll: 5  Chance to drop: 11.11%  Possible combinations: [1, 2, 3, 4] [4, 3, 2, 1]
Dice roll: 6  Chance to drop: 13.89%  Possible combinations: [1, 2, 3, 4, 5] [5, 4, 3, 2, 1]
Dice roll: 7  Chance to drop: 16.67%  Possible combinations: [1, 2, 3, 4, 5, 6] [6, 5, 4, 3, 2, 1]
Dice roll: 8  Chance to drop: 13.89%  Possible combinations: [2, 3, 4, 5, 6] [6, 5, 4, 3, 2]
Dice roll: 9  Chance to drop: 11.11%  Possible combinations: [3, 4, 5, 6] [6, 5, 4, 3]
Dice roll: 10 Chance to drop: 08.33%  Possible combinations: [4, 5, 6] [6, 5, 4]
Dice roll: 11 Chance to drop: 05.56%  Possible combinations: [5, 6] [6, 5]
Dice roll: 12 Chance to drop: 02.78%  Possible combinations: [6] [6]
```