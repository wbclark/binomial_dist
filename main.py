import scipy.special

# binomial distribution probability density function with probability p, trials n, successes k
def binom_pdf(p, n, k):
    return scipy.special.comb(n, k)*(p**k)*((1-p)**(n-k))

P_one = 0.1852  # C'thun drop rate
P_two = 0.2030  # Faerlina drop rate
P_three = 0.1740 # Kel'thuzad drop rate

def compute_probability(min_successes = 10, num_weeks = 12):
    total_probability = 0
    for K_one in range(min_successes):
        for K_two in range(min_successes-K_one):
            for K_three in range(min_successes-K_two-K_one):
                current_probability = binom_pdf(P_one, num_weeks, K_one)*binom_pdf(P_two, num_weeks, K_two)*binom_pdf(P_three, num_weeks, K_three)
                total_probability += current_probability
                # print(f'{K_one} drops from C\'thun, {K_two} drops from Faerlina, and {K_three} drops from Kel\'thuzad has probability: {current_probability}')
                # print(f'cumulative probability at this point in the calculation is {total_probability}')
    print(f'The probability of having less than {min_successes} total drops of the three items in {num_weeks} weeks is {total_probability}.')
    print(f'The probability of having {min_successes} or more total drops of the three items in {num_weeks} weeks is {1-total_probability}.')


compute_probability(min_successes = 5, num_weeks = 12)
compute_probability(min_successes = 6, num_weeks = 12)
compute_probability(min_successes = 8, num_weeks = 12)
compute_probability(min_successes = 10, num_weeks = 12)
compute_probability(min_successes = 5, num_weeks = 16)
compute_probability(min_successes = 6, num_weeks = 16)
compute_probability(min_successes = 8, num_weeks = 16)
compute_probability(min_successes = 10, num_weeks = 16)
