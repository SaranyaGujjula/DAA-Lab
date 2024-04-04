import time
import matplotlib.pyplot as plt

def iter_sum(N):
    total = 0
    for num in range(1, N + 1):
        total += num
    return total

def recur_sum(N):
    if N == 0:
        return 0
    else:
        return N + recur_sum(N - 1)

def measure_time(func, N):
    start_time = time.time()
    func(N)
    end_time = time.time()
    return end_time - start_time

N_values = range(1, 1001)

recursive_times = [measure_time(recur_sum, n) for n in N_values]
iterative_times = [measure_time(iter_sum, n) for n in N_values]

plt.plot(N_values, recursive_times, label='Recursive')
plt.plot(N_values, iterative_times, label='Iterative')
plt.xlabel('N')
plt.ylabel('Time (s)')
plt.title('Execution Time for Sum of First N Natural Numbers')
plt.legend()
plt.grid(True)
plt.show()
