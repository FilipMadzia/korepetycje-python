import random
import time

def rzuc_kostka(n):
    rzuty = [0, 0, 0, 0, 0, 0]

    for i in range(n):
        wylosowana = random.randint(1, 6)

        rzuty[wylosowana - 1] += 1

    return rzuty

for n in [10, 1_000_000]:
    print(f"-- n = {n} --")

    czasy_time = []
    czasy_perf = []

    for i in range(5):
        start_time = time.time()
        start_perf = time.perf_counter()

        rzuc_kostka(n)

        end_time = time.time()
        end_perf = time.perf_counter()

        czasy_time.append(end_time - start_time)
        czasy_perf.append(end_perf - start_perf)

    min_time = min(czasy_time)
    avg_time = sum(czasy_time) / len(czasy_time)

    print("time:\t", end="")

    for czas in czasy_time:
        print(f"{czas:.7f}", end=", ")

    print(f"/ min: {min_time} / srednia: {avg_time}")

    min_perf = min(czasy_perf)
    avg_perf = sum(czasy_perf) / len(czasy_perf)

    print("perf_counter:\t", end="")
    
    for czas in czasy_perf:
        print(f"{czas:.7f}", end=", ")

    print(f"/ min: {min_perf} / srednia: {avg_perf}")