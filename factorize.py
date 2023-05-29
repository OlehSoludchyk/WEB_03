# № 1

# import time


# def factorize(*numbers):
#     results_list = []
#     for i in numbers:
#         result_for_i = []
#         for num in range(1, i+1):
#             if i % num == 0:
#                 result_for_i.append(num)
#         results_list.append(result_for_i)

#     return results_list


# start_time = time.time()
# factorize(34574, 26477, 256, 1857, 235355, 3464, 3463463, 34673, 75656322)
# end_time = time.time()

# time_for_factorize = end_time - start_time
# print(f"Час виконання функції: {time_for_factorize} секунд")
# #Час виконання функції: 15.37949809265136719 секунд





# № 2

import time
from multiprocessing import cpu_count, Pool

num_cores = cpu_count()

def factorize(*numbers):
    results_list = []
    for i in numbers:
        result_for_i = []
        for num in range(1, i+1):
            if i % num == 0:
                result_for_i.append(num)
        results_list.append(result_for_i)

    return results_list

if __name__ == '__main__':
    numbers = [34574, 26477, 256, 1857, 235355, 3464, 3463463, 34673, 75656322]
    
    start_time = time.time()
    
    pool = Pool(num_cores)
    results = pool.map(factorize, numbers)
    
    end_time = time.time()
    time_for_factorize = end_time - start_time
    print(f"Час виконання функції: {time_for_factorize} секунд")

# Час виконання функції: 13.22700809265136719 секунд