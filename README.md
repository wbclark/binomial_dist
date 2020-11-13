The purpose of this script is to compute for a friend the probability of a certain number of events occurring in a game.

Given three probabilities: P_one = 0.1852, P_two = 0.2030, and P_three = 0.1740, the challenge is to compute the total probability of 10 or more successes on 12 independent trials with probability P_one, 12 independent trials with probability P_two, and 12 independent trials with probably P_three.

The strategy is to take the product of three binomial distribution probability density functions, and sum over success counts less than 10 in order to compute the probability of having less than 10 successes. The result is then subtracted from 1 to compute the probability of at least 10 successes.

The result of the calculation is below. The results are generalized to show the probability of at least 5, 6, 8, and 10 total drops, over periods of 12 or 16 weeks:

```
(env) [wclark@mercury binomial_dist]$ python main.py
The probability of having less than 5 total drops of the three items in 12 weeks is 0.16904214282448324.
The probability of having 5 or more total drops of the three items in 12 weeks is 0.8309578571755167.
The probability of having less than 6 total drops of the three items in 12 weeks is 0.3091339724208954.
The probability of having 6 or more total drops of the three items in 12 weeks is 0.6908660275791045.
The probability of having less than 8 total drops of the three items in 12 weeks is 0.641144265758637.
The probability of having 8 or more total drops of the three items in 12 weeks is 0.35885573424136297.
The probability of having less than 10 total drops of the three items in 12 weeks is 0.8780662653414533.
The probability of having 10 or more total drops of the three items in 12 weeks is 0.12193373465854673.
The probability of having less than 5 total drops of the three items in 16 weeks is 0.039338422703614734.
The probability of having 5 or more total drops of the three items in 16 weeks is 0.9606615772963852.
The probability of having less than 6 total drops of the three items in 16 weeks is 0.09203894095674144.
The probability of having 6 or more total drops of the three items in 16 weeks is 0.9079610590432585.
The probability of having less than 8 total drops of the three items in 16 weeks is 0.29981097926312683.
The probability of having 8 or more total drops of the three items in 16 weeks is 0.7001890207368732.
The probability of having less than 10 total drops of the three items in 16 weeks is 0.5885968999053196.
The probability of having 10 or more total drops of the three items in 16 weeks is 0.4114031000946804.
```
