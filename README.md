The purpose of this script is to compute for a friend the probability of a certain number of events occurring in a game.

Given three probabilities: P_one = 0.1852, P_two = 0.2030, and P_three = 0.1740, the challenge is to compute the total probability of 10 or more successes on 12 independent trials with probability P_one, 12 independent trials with probability P_two, and 12 independent trials with probably P_three.

The strategy is to take the product of three binomial distribution probability density functions, and sum over success counts less than 10 in order to compute the probability of having less than 10 successes. The result is then subtracted from 1 to compute the probability of at least 10 successes.

The result of the calculation is below. The results are generalized to show the probability of at least 5, 6, 7, 8, 9, or 10 total drops, over periods of 12, 14, or 16 weeks:

UPDATE: Apparently the initial P values were probably off. Per someone who would know, P_one should be around 0.05, P_two around 0.20, and P_three around 0.10-0.12 (lower certainty here due to low sample size). The updated calculation is

```
(env) [wclark@mercury binomial_dist]$ python main.py
The probability of having 5 or more total drops of the three items in 12 weeks is 0.4380531313103446.
The probability of having 6 or more total drops of the three items in 12 weeks is 0.25629006661661835.
The probability of having 7 or more total drops of the three items in 12 weeks is 0.12924679205335687.
The probability of having 8 or more total drops of the three items in 12 weeks is 0.05634308203677996.
The probability of having 9 or more total drops of the three items in 12 weeks is 0.021323740981913253.
The probability of having 10 or more total drops of the three items in 12 weeks is 0.00703848091740511.
The probability of having 5 or more total drops of the three items in 14 weeks is 0.5813774417526356.
The probability of having 6 or more total drops of the three items in 14 weeks is 0.3910150935801887.
The probability of having 7 or more total drops of the three items in 14 weeks is 0.23102950460315597.
The probability of having 8 or more total drops of the three items in 14 weeks is 0.11986394452159643.
The probability of having 9 or more total drops of the three items in 14 weeks is 0.05472790787214088.
The probability of having 10 or more total drops of the three items in 14 weeks is 0.022063664037083486.
The probability of having 5 or more total drops of the three items in 16 weeks is 0.7025044875004827.
The probability of having 6 or more total drops of the three items in 16 weeks is 0.5253178582526653.
The probability of having 7 or more total drops of the three items in 16 weeks is 0.35130993447197767.
The probability of having 8 or more total drops of the three items in 16 weeks is 0.2093106579410423.
The probability of having 9 or more total drops of the three items in 16 weeks is 0.11107841810440233.
The probability of having 10 or more total drops of the three items in 16 weeks is 0.05259701566799979.
```

The calculation with the older P values is presented here to see the difference:

```
(env) [wclark@mercury binomial_dist]$ python main.py
The probability of having 5 or more total drops of the three items in 12 weeks is 0.8309578571755167.
The probability of having 6 or more total drops of the three items in 12 weeks is 0.6908660275791045.
The probability of having 7 or more total drops of the three items in 12 weeks is 0.5238973559229865.
The probability of having 8 or more total drops of the three items in 12 weeks is 0.35885573424136297.
The probability of having 9 or more total drops of the three items in 12 weeks is 0.22089345156005358.
The probability of having 10 or more total drops of the three items in 12 weeks is 0.12193373465854673.
The probability of having 5 or more total drops of the three items in 14 weeks is 0.9158279107972028.
The probability of having 6 or more total drops of the three items in 14 weeks is 0.824850880604856.
The probability of having 7 or more total drops of the three items in 14 weeks is 0.6954163998219784.
The probability of having 8 or more total drops of the three items in 14 weeks is 0.5418639022795981.
The probability of having 9 or more total drops of the three items in 14 weeks is 0.38692084872661014.
The probability of having 10 or more total drops of the three items in 14 weeks is 0.2519374163817394.
The probability of having 5 or more total drops of the three items in 16 weeks is 0.9606615772963852.
The probability of having 6 or more total drops of the three items in 16 weeks is 0.9079610590432585.
The probability of having 7 or more total drops of the three items in 16 weeks is 0.8208162385709346.
The probability of having 8 or more total drops of the three items in 16 weeks is 0.7001890207368732.
The probability of having 9 or more total drops of the three items in 16 weeks is 0.5575840407116046.
The probability of having 10 or more total drops of the three items in 16 weeks is 0.4114031000946804.
```
