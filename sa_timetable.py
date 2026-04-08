import random
import math
import matplotlib.pyplot as plt
import os

EXAMS = [
    "Mathematics","Physics","Chemistry","English","History",
    "Computer Science","Economics","Biology","Statistics","Geography"
]

NUM_EXAMS = len(EXAMS)
NUM_SLOTS = 5

STUDENTS = [
    [0,1,5],[0,2,6],[1,3,7],[2,4,8],[3,5,9],
    [0,4,7],[1,6,8],[2,5,9],[3,6,0],[4,7,1],
    [5,8,2],[6,9,3],[7,0,4],[8,1,5],[9,2,6],
    [0,3,8],[1,4,9],[2,7,5],[3,8,6],[4,9,7],
    [0,5,2],[1,6,3],[2,7,4],[3,8,0],[4,9,1],
    [5,0,6],[6,1,7],[7,2,8],[8,3,9],[9,4,0],
]

# =========================
# OBJECTIVE FUNCTION
# =========================
def count_clashes(timetable):
    clashes = 0
    for student in STUDENTS:
        seen = set()
        for exam in student:
            slot = timetable[exam]
            if slot in seen:
                clashes += 1
            seen.add(slot)
    return clashes

# =========================
# NEIGHBOR
# =========================
def generate_neighbor(timetable):
    new_tt = timetable[:]
    exam = random.randint(0, NUM_EXAMS-1)
    current = timetable[exam]
    new_slot = random.choice([s for s in range(NUM_SLOTS) if s != current])
    new_tt[exam] = new_slot
    return new_tt

# =========================
# SA ALGORITHM
# =========================
def run_sa(initial_temp=100.0, cooling_rate=0.995,
           min_temp=0.1, max_iterations=5000, seed=42):

    random.seed(seed)

    current = [random.randint(0, NUM_SLOTS-1) for _ in range(NUM_EXAMS)]
    current_c = count_clashes(current)

    best = current[:]
    best_c = current_c

    T = initial_temp
    clash_log = []
    temp_log = []

    for _ in range(max_iterations):
        if T < min_temp:
            break

        neighbour = generate_neighbor(current)
        neighbour_c = count_clashes(neighbour)

        delta = neighbour_c - current_c

        if delta < 0 or random.random() < math.exp(-delta / T):
            current = neighbour
            current_c = neighbour_c

        if current_c < best_c:
            best = current[:]
            best_c = current_c

        clash_log.append(best_c)
        temp_log.append(T)

        T *= cooling_rate

        if best_c == 0:
            break

    return best, best_c, clash_log, temp_log

# =========================
# PRINT
# =========================
def print_timetable(timetable):
    print("\nFinal Timetable")
    print("-"*40)
    for slot in range(NUM_SLOTS):
        exams = [EXAMS[i] for i in range(NUM_EXAMS) if timetable[i]==slot]
        print(f"Slot {slot+1}: {', '.join(exams)}")
    print("-"*40)
    print("Clashes:", count_clashes(timetable))

# =========================
# PLOT
# =========================
def save_plot(clash_log, temp_log, filename, title):
    os.makedirs("plots", exist_ok=True)

    fig, (ax1, ax2) = plt.subplots(2,1,figsize=(8,6))

    ax1.plot(clash_log)
    ax1.set_title(title)
    ax1.set_ylabel("Clashes")
    ax1.grid()

    ax2.plot(temp_log)
    ax2.set_ylabel("Temperature")
    ax2.set_xlabel("Iteration")
    ax2.grid()

    plt.savefig(filename)
    plt.close()

# =========================
# MAIN
# =========================
if __name__ == "__main__":

    # ===== EXPERIMENT 1 =====
    print("=== EXPERIMENT 1 ===")

    tt, c, cl, tl = run_sa(cooling_rate=0.995)
    print_timetable(tt)
    print("Final clashes:", c)

    save_plot(cl, tl, "plots/experiment_1.png", "Baseline 0.995")

    # ===== EXPERIMENT 2 =====

    print("\n=== COOLING 0.80 ===")
    tt2, c2, cl2, tl2 = run_sa(cooling_rate=0.80)
    print_timetable(tt2)
    print("Final clashes:", c2)
    save_plot(cl2, tl2, "plots/experiment_2a.png", "Cooling 0.80")

    print("\n=== COOLING 0.95 ===")
    tt3, c3, cl3, tl3 = run_sa(cooling_rate=0.95)
    print_timetable(tt3)
    print("Final clashes:", c3)
    save_plot(cl3, tl3, "plots/experiment_2b.png", "Cooling 0.95")

    print("\n=== COOLING 0.995 ===")
    tt4, c4, cl4, tl4 = run_sa(cooling_rate=0.995)
    print_timetable(tt4)
    print("Final clashes:", c4)
    save_plot(cl4, tl4, "plots/experiment_2c.png", "Cooling 0.995")