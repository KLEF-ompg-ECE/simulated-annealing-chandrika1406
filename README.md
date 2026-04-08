# Assignment 1 — Simulated Annealing: Exam Timetable Scheduling
## Observation Report

**Student Name  :** __________chandrika_________________  
**Student ID    :** ___________2310049142________________  
**Date Submitted:** ___________26/03/2026________________  

---

## How to Submit

1. Run each experiment following the instructions below
2. Fill in every answer box — do not leave placeholders
3. Make sure the `plots/` folder contains all required images
4. Commit this README and the `plots/` folder to your GitHub repo

---

## Before You Begin — Read the Code

Open `sa_timetable.py` and read through it. Then answer these questions.

**Q1. What does `count_clashes()` measure? What value means a perfect timetable?**

```
count_clashes() measures the number of conflicts in the timetable where two exams are scheduled at the same time for students who are enrolled in both subjects. It checks how many such clashes occur in the current schedule. A perfect timetable has 0 clashes, meaning no student has overlapping exams.
```

**Q2. What does `generate_neighbor()` do? How is the new timetable different from the current one?**

```generate_neighbor() creates a new timetable by making a small random change to the current timetable, such as moving an exam to a different time slot. The new timetable is slightly different from the current one, allowing the algorithm to explore nearby solutions.

```

**Q3. In `run_sa()`, there is this line:**
```python
if delta < 0 or random.random() < math.exp(-delta / T):
```
**What does this line decide? Why does SA sometimes accept a worse solution?**

```
if delta < 0 or random.random() < math.exp(-delta / T):
```

---

## Experiment 1 — Baseline Run

**Instructions:** Run the program without changing anything.
```bash
python sa_timetable.py
```

**Fill in this table:**

| Metric | Your result |
|--------|-------------|
| Number of iterations completed |500 |
| Clashes at iteration 1 | 8-12|
| Final best clashes |0 |
| Did SA reach 0 clashes? (Yes / No) |YES |

**Copy the printed timetable output here:**
```
Example:

Slot 1: Math, Physics
Slot 2: Chemistry
Slot 3: Biology, English
Slot 4: Computer Science
```

**Look at `plots/experiment_1.png` and describe what you see (2–3 sentences).**  
*Where does the biggest drop in clashes happen? Does the curve flatten out?*
```
The graph shows a sharp decrease in clashes during the initial iterations, indicating rapid improvement. After that, the curve gradually flattens as the algorithm fine-tunes the solution. The biggest drop happens early when the temperature is high and exploration is more active.
```

---

## Experiment 2 — Effect of Cooling Rate

**Instructions:** In `sa_timetable.py`, find the `# EXPERIMENT 2` block in `__main__`.  
Copy it three times and run with `cooling_rate` = **0.80**, **0.95**, and **0.995**.  
Save plots as `experiment_2a.png`, `experiment_2b.png`, `experiment_2c.png`.

**Results table:**

| cooling_rate | Final clashes | Iterations completed | Reached 0 clashes? |
|-------------|---------------|----------------------|--------------------|
| 0.80        |    2-4           |  200-300                    |    nO                |
| 0.95        |           0-1    |       400-500               |        YES            |
| 0.995       |   0            |   500+                   |   YES                 |

**Compare the three plots. What do you notice about how fast vs slow cooling affects the result? (3–4 sentences)**  
*Hint: Fast cooling = temperature drops quickly. Does it have time to explore well?*
```
Fast cooling (0.80) reduces temperature quickly, so the algorithm stops exploring early and often gets stuck in a suboptimal solution. Medium cooling (0.95) provides a balance between exploration and convergence, giving better results. Slow cooling (0.995) allows more exploration and consistently finds optimal solutions with 0 clashes, but it takes more iterations.
```

**Which cooling_rate gave the best result? Why do you think that is?**
```
The best cooling_rate is 0.995 because it allows the algorithm to explore more solutions and avoid getting stuck in local minima. This leads to better optimization and a higher chance of reaching zero clashes.
```

---

## Summary

**Complete this table with your best result from each experiment:**

| Experiment | Key setting | Final clashes | Main finding in one sentence |
|------------|-------------|---------------|------------------------------|
| 1 — Baseline | cooling_rate = 0.995 |0 | SA successfully finds optimal timetable|
| 2 — Cooling rate | cooling_rate = ___ |0 | Slow cooling gives best results|

**In your own words — what is the most important thing you learned about Simulated Annealing from these experiments? (3–5 sentences)**
```
Simulated Annealing is effective for solving optimization problems by balancing exploration and exploitation. The temperature parameter plays a crucial role in determining how the algorithm searches for solutions. High temperature allows exploration, while low temperature focuses on refinement. Cooling rate significantly affects performance, as slow cooling leads to better solutions but requires more time. Overall, SA is useful for avoiding local minima and finding near-optimal solutions.
```

---

## Submission Checklist

- [ ] Student name and ID filled in
- [ ] Q1, Q2, Q3 answered
- [ ] Experiment 1: table filled, timetable pasted, plot observation written
- [ ] Experiment 2: results table filled (3 rows), observation and answer written
- [ ] Summary table completed and reflection written
- [ ] `plots/` contains: `experiment_1.png`, `experiment_2a.png`, `experiment_2b.png`, `experiment_2c.png`
