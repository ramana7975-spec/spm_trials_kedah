# 👶 Complete Beginner's Guide - Your First Physics Question

## What You Just Got

I created 5 empty files for you:
- `subjects/physics/question_1.py`
- `subjects/physics/question_2.py`
- `subjects/physics/question_3.py`
- `subjects/physics/question_4.py`
- `subjects/physics/question_5.py`

## Let's Fill In Your First Question Together!

### Example: Let's say your physics question is:

**"A car travels at a constant speed of 20 m/s for 10 seconds. Calculate the distance traveled."**

---

## Step-by-Step: How to Fill in question_1.py

### Step 1: Open the file

Navigate to: `subjects/physics/question_1.py`

### Step 2: Replace the question at the top

Change this:
```python
Question: [PASTE YOUR QUESTION HERE]
```

To this:
```python
Question: A car travels at a constant speed of 20 m/s for 10 seconds.
          Calculate the distance traveled.
Topic: Kinematics - Distance and Speed
```

### Step 3: Fill in the solve_question() function

Look for this part in the file and fill it in:

```python
def solve_question():
    # STEP 1: Write down what you know
    speed = 20      # meters per second (m/s)
    time = 10       # seconds (s)

    # STEP 2: Write the formula
    # Formula: distance = speed × time

    # STEP 3: Calculate
    distance = speed * time

    # STEP 4: Return the answer
    return distance
```

### Step 4: Fill in the show_working() function

Update the working section:

```python
def show_working():
    print("=" * 60)
    print("SOLUTION:")
    print("=" * 60)

    print("\nStep 1: What do we know?")
    print("  - Speed (v) = 20 m/s")
    print("  - Time (t) = 10 s")
    print("  - We need to find: Distance (s)")

    print("\nStep 2: What formula do we use?")
    print("  - Formula: distance = speed × time")
    print("  - Formula: s = v × t")

    print("\nStep 3: Substitute values into formula")
    print("  - s = 20 × 10")

    print("\nStep 4: Calculate")
    print("  - s = 200 meters")

    print("\n" + "=" * 60)
```

---

## How to Run Your Solution

Once you've filled in the file, here's how to see your answer:

### Option 1: Using Command Line (Terminal)

1. Open your terminal/command prompt
2. Navigate to your project folder:
   ```bash
   cd /home/user/spm_trials_kedah
   ```

3. Run the question file:
   ```bash
   python subjects/physics/question_1.py
   ```

4. You'll see:
   ```
   🔬 PHYSICS QUESTION 1
   ============================================================
   SOLUTION:
   ============================================================

   Step 1: What do we know?
     - Speed (v) = 20 m/s
     - Time (t) = 10 s
     - We need to find: Distance (s)

   Step 2: What formula do we use?
     - Formula: distance = speed × time
     - Formula: s = v × t

   Step 3: Substitute values into formula
     - s = 20 × 10

   Step 4: Calculate
     - s = 200 meters

   ============================================================

   ✅ FINAL ANSWER: 200
   ============================================================
   ```

---

## Common Physics Formulas to Help You

Here are some formulas you might need:

### 1. Speed, Distance, Time
```python
speed = distance / time
distance = speed * time
time = distance / speed
```

### 2. Force and Motion
```python
force = mass * acceleration  # F = ma
```

### 3. Kinetic Energy
```python
kinetic_energy = 0.5 * mass * speed**2  # KE = ½mv²
```

### 4. Potential Energy
```python
potential_energy = mass * gravity * height  # PE = mgh
# gravity = 9.81 m/s² (on Earth)
```

### 5. Work Done
```python
work = force * distance  # W = F × s
```

### 6. Power
```python
power = work / time  # P = W / t
```

---

## Important Python Symbols

When writing your solutions, use these symbols:

| What You Mean | Python Symbol | Example |
|---------------|---------------|---------|
| Multiply      | `*`          | `5 * 3` = 15 |
| Divide        | `/`          | `10 / 2` = 5 |
| Add           | `+`          | `5 + 3` = 8 |
| Subtract      | `-`          | `5 - 3` = 2 |
| Power/Square  | `**`         | `5**2` = 25 (5²) |
| Equals        | `=`          | `x = 10` |

---

## Quick Checklist

Before running your solution, make sure:

- [ ] You wrote the question at the top
- [ ] You filled in the "given" values in solve_question()
- [ ] You wrote the formula
- [ ] You calculated the answer
- [ ] You added `return answer` at the end of solve_question()
- [ ] You filled in the show_working() section

---

## Need Help?

If you get stuck:

1. **Read the error message** - Python will tell you what's wrong
2. **Check your spelling** - Python is very picky about spelling
3. **Check your indentation** - Lines need to be indented correctly
4. **Make sure you saved the file** before running it

---

## What's Next?

Once you've completed question_1.py:

1. Copy what you did to question_2.py
2. Change the question and values
3. Run it!
4. Repeat for questions 3, 4, and 5

You're doing great! Remember, everyone starts from zero. The more you practice, the easier it gets! 💪

