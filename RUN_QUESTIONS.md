# 🎮 HOW TO RUN YOUR PHYSICS QUESTIONS

This guide shows you exactly how to run each question and see the solutions!

---

## 📍 Step 1: Open Terminal/Command Prompt

**On Windows:**
- Press `Windows Key + R`
- Type `cmd` and press Enter

**On Mac:**
- Press `Command + Space`
- Type `terminal` and press Enter

**On Linux:**
- Press `Ctrl + Alt + T`

---

## 📍 Step 2: Navigate to Your Project

Type this command and press Enter:

```bash
cd /home/user/spm_trials_kedah
```

*(This takes you to your project folder)*

---

## 📍 Step 3: Run Any Question!

### **QUESTION 1 - Photoelectric Effect (Theory)**
```bash
python subjects/physics/question_1.py
```
What you'll see: Complete explanation of photoelectric effect, diagrams, equations, exam tips

---

### **QUESTION 2 - Newton's First Law (Theory)**
```bash
python subjects/physics/question_2.py
```
What you'll see: Law of inertia, examples (car braking, bus), diagrams, exam structure

---

### **QUESTION 3 - Kinetic Energy (Calculation)**
```bash
python subjects/physics/question_3.py
```
What you'll see: Complete calculation showing KE = 250 J, step-by-step working, practice problems

---

### **QUESTION 4 - Thermionic Emission (Theory)**
```bash
python subjects/physics/question_4.py
```
What you'll see: Explanation of heat-caused electron emission, comparison with photoelectric effect

---

### **QUESTION 5 - Gravitational Potential Energy (Calculation)**
```bash
python subjects/physics/question_5.py
```
What you'll see: Complete calculation showing PE = 392.4 J, comparison with kinetic energy

---

## 🚀 Quick Command List (Copy & Paste!)

Run all 5 questions one after another:

```bash
# Navigate to project
cd /home/user/spm_trials_kedah

# Run Question 1
python subjects/physics/question_1.py

# Run Question 2
python subjects/physics/question_2.py

# Run Question 3
python subjects/physics/question_3.py

# Run Question 4
python subjects/physics/question_4.py

# Run Question 5
python subjects/physics/question_5.py
```

---

## 💡 Pro Tips:

### **Tip 1: Run Multiple Questions**
If you want to run all questions in sequence without stopping:

```bash
python subjects/physics/question_1.py && \
python subjects/physics/question_2.py && \
python subjects/physics/question_3.py && \
python subjects/physics/question_4.py && \
python subjects/physics/question_5.py
```

### **Tip 2: Save Output to a File**
If you want to save the output to read later:

```bash
python subjects/physics/question_1.py > my_answer.txt
```

Then open `my_answer.txt` to see the output!

### **Tip 3: Print Output**
To save ALL outputs to one file for printing:

```bash
python subjects/physics/question_1.py > all_answers.txt
python subjects/physics/question_2.py >> all_answers.txt
python subjects/physics/question_3.py >> all_answers.txt
python subjects/physics/question_4.py >> all_answers.txt
python subjects/physics/question_5.py >> all_answers.txt
```

Now `all_answers.txt` has everything!

---

## 🎯 What Each Question Shows:

| Question | Type | Main Content | Answer |
|----------|------|--------------|---------|
| Question 1 | Theory | Photoelectric effect explanation | Full explanation |
| Question 2 | Theory | Newton's First Law | Full explanation |
| Question 3 | Calculation | Kinetic energy formula | 250 J |
| Question 4 | Theory | Thermionic emission | Full explanation |
| Question 5 | Calculation | Potential energy formula | 392.4 J |

---

## ❓ Troubleshooting:

### **Error: "python: command not found"**
Try using `python3` instead:
```bash
python3 subjects/physics/question_1.py
```

### **Error: "No such file or directory"**
Make sure you're in the right folder first:
```bash
cd /home/user/spm_trials_kedah
pwd  # This shows where you are
```

### **Error: "No module named..."**
Install the required packages:
```bash
pip install -r requirements.txt
```

---

## 🎓 Before Your Exam:

Run all questions to review:

```bash
# Quick review - run all 5 questions
cd /home/user/spm_trials_kedah
python subjects/physics/question_1.py
python subjects/physics/question_2.py
python subjects/physics/question_3.py
python subjects/physics/question_4.py
python subjects/physics/question_5.py
```

**Take notes on:**
- Key formulas
- Common mistakes to avoid
- Exam tips sections

---

## 📱 Even Easier: Create Shortcuts!

### **Windows Batch File:**
Create a file called `run_all.bat` with:
```batch
@echo off
cd /home/user/spm_trials_kedah
python subjects/physics/question_1.py
python subjects/physics/question_2.py
python subjects/physics/question_3.py
python subjects/physics/question_4.py
python subjects/physics/question_5.py
pause
```

Double-click to run all questions!

### **Mac/Linux Shell Script:**
Create a file called `run_all.sh` with:
```bash
#!/bin/bash
cd /home/user/spm_trials_kedah
python subjects/physics/question_1.py
python subjects/physics/question_2.py
python subjects/physics/question_3.py
python subjects/physics/question_4.py
python subjects/physics/question_5.py
```

Make it executable and run:
```bash
chmod +x run_all.sh
./run_all.sh
```

---

## 🎉 You're All Set!

Now you can:
✅ Run any question anytime
✅ Review before exams
✅ Show your friends
✅ Practice with different values

**Good luck with your SPM trial!** 💪

