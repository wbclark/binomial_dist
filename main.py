import scipy.special

# binomial distribution probability density function with probability p, trials n, successes k
def binom_pdf(p, n, k):
    return scipy.special.comb(n, k)*(p**k)*((1-p)**(n-k))

P_one = 0.1852  # C'thun drop rate
P_two = 0.2030  # Faerlina drop rate
P_three = 0.1740 # Kel'thuzad drop rate

# to compute the probability of 10 or more drops with 12 trials on each boss, we first compute the probability of 9 or less drops
# we sum over products of PDFs with K_one + K_two + K_three < 10

total_probability = 0
for K_one in range(10):
    for K_two in range(10-K_one):
        for K_three in range(10-K_two-K_one):
            current_probability = binom_pdf(P_one, 12, K_one)*binom_pdf(P_two, 12, K_two)*binom_pdf(P_three, 12, K_three)
            total_probability += current_probability
            print(f'{K_one} drops from C\'thun, {K_two} drops from Faerlina, and {K_three} drops from Kel\'thuzad has probability: {current_probability}')
            print(f'cumulative probability at this point in the calculation is {total_probability}')

# total_probability is the probability of less than 10 drops on 12 kills each of the three bosses
# 1 - total_probability then is the probability of 10 or more drops on 12 kills each of the three bosses

print('Calculation done!')
print(f'The probability of having less than 10 total drops of the three items in 12 weeks is {total_probability}.')
print(f'The probability of having 10 or more total drops of the three items in 12 weeks is {1-total_probability}.')
