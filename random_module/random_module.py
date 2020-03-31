###############################################
#                                             #
#       Created by Youssef Sully              #
#       Beginner 2 python                     #
#       Random module                         #
#                                             #
###############################################

import random

# uniform (START, STOP) (1, 10) returns FLOAT
# NOTE that the stop value (10) IS included

print("\n{} {} {}\n".format("-" * 9, "uniform, randrange and randint", "-" * 9))

random_value_1 = random.uniform(1, 10)
print(random_value_1)

# randrange (START, STOP, STEP) (1, 10, 5) returns INTEGER
# NOTE that the stop value (10) is NOT included therefore the output will always be 1 or 6

random_value_2 = random.randrange(1, 10, 5)  # another variant random.randrange(10)
print(random_value_2)

# randint (START, STOP) (1, 10) returns INTEGER
# NOTE that the stop value (10) IS included

random_value_3 = random.randint(1, 10)
print(random_value_3)

print("\n{} {} {}\n".format("-" * 9, "shuffle, sample, choice and choices", "-" * 9))


num_list_1 = [1, 2, 3]
num_list_2 = [1, 2, 3, 4, 5]
str_list = ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'i']

# NOTE that shuffle overwrite (mutated) the original num_list
random.shuffle(num_list_2)
print(num_list_2)

# NOTE that sample DOESN'T overwrite (mutated) the original str_list
# (str_list, 4) 4 is the number of output elements
# NOTE there are no similar elements in the output list
shuffled_str = random.sample(str_list, k=4)
print(shuffled_str)

choice_num_1 = random.choice(num_list_1)
print(choice_num_1)

choice_num_2 = random.choices(num_list_1, k=9)
print(choice_num_2)

print(num_list_1)
choice_num_3 = random.choices(num_list_1, weights=[5, 50, 45], k=9)
print(choice_num_3)
