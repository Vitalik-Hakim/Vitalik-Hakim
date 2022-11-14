###
# Define range
import random
#Guess a numebr between 1-100

FROM = 1

TO = 1000000
ai_guess = random.randint(FROM,TO)
roulette_list =  list(range(FROM, TO))

print(ai_guess)
# print(roulette_list)
steps = 0
while True:
    roulette_guess = random.choice(roulette_list)
    steps += 1
    if roulette_guess == ai_guess:
        print(f"Got it {ai_guess}")
        print('steps',steps)
        break
    else:
        print(f"I chose {roulette_guess} but its wrong!")
        print(f"{ai_guess} is the answer :(")
        roulette_list.remove(roulette_guess)
        if ai_guess > roulette_guess:
            roulette_list = roulette_list =  list(range(roulette_guess, TO))
            # print(roulette_list)
        elif ai_guess < roulette_guess:
            roulette_list = roulette_list =  list(range(FROM, roulette_guess))
            # print(roulette_list)
        continue
