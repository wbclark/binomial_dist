import scipy.special

# binomial distribution probability density function with probability p, trials n, successes k
def binom_pdf(p, n, k):
    return scipy.special.comb(n, k)*(p**k)*((1-p)**(n-k))

# P_one = 0.1852  # C'thun drop rate
# P_two = 0.2030  # Faerlina drop rate
# P_three = 0.1740 # Kel'thuzad drop rate

# Per Larry, these probabilities are probably more accurate. P_three is the most uncertain due to low sample size.
P_one = 0.05
P_two = 0.20
P_three = 0.11

def compute_probability(min_successes, num_weeks):
    total_probability = 0
    for K_one in range(min_successes):
        for K_two in range(min_successes-K_one):
            for K_three in range(min_successes-K_two-K_one):
                current_probability = binom_pdf(P_one, num_weeks, K_one)*binom_pdf(P_two, num_weeks, K_two)*binom_pdf(P_three, num_weeks, K_three)
                total_probability += current_probability
                # print(f'{K_one} drops from C\'thun, {K_two} drops from Faerlina, and {K_three} drops from Kel\'thuzad has probability: {current_probability}')
                # print(f'cumulative probability at this point in the calculation is {total_probability}')
    print(f'The probability of having {min_successes} or more total drops of the three items in {num_weeks} weeks is {1-total_probability}.')

for weeks in [12,14,16]:
    for successes in [5,6,7,8,9,10]:
        compute_probability(min_successes = successes, num_weeks = weeks)
