import math
import time

def gauss_legendre(iterations):
    a = 1.0
    b = 1 / math.sqrt(2)
    t = 0.25
    p = 1.0

    for _ in range(iterations):
        a_next = (a + b) / 2
        b = math.sqrt(a * b)
        t -= p * (a - a_next) ** 2
        a = a_next
        p *= 2

    return (a + b) ** 2 / (4 * t)

start_time = time.time()
iterations = 3
pi = gauss_legendre(iterations)
end_time = time.time()

proc_time = end_time - start_time

print("円周率π:", pi)
print(f"処理時間: {proc_time * 1000:.3f} msec : {proc_time * 1000000:.3f} µsec : {proc_time * 1000000000:.3f} nsec")