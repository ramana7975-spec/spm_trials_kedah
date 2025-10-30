#!/bin/bash

# ============================================================================
# RUN ALL PHYSICS QUESTIONS
# ============================================================================
# This script runs all 5 SPM physics trial questions in sequence
# ============================================================================

echo "╔══════════════════════════════════════════════════════════════╗"
echo "║        SPM 2025 TRIAL - KEDAH PHYSICS SOLUTIONS              ║"
echo "║        Running ALL 5 Questions                               ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""
echo "Press Enter after each question to continue to the next one..."
echo ""

# Question 1
echo "════════════════════════════════════════════════════════════════"
echo "                    QUESTION 1 of 5"
echo "════════════════════════════════════════════════════════════════"
python subjects/physics/question_1.py
echo ""
read -p "Press Enter to continue to Question 2..."
echo ""

# Question 2
echo "════════════════════════════════════════════════════════════════"
echo "                    QUESTION 2 of 5"
echo "════════════════════════════════════════════════════════════════"
python subjects/physics/question_2.py
echo ""
read -p "Press Enter to continue to Question 3..."
echo ""

# Question 3
echo "════════════════════════════════════════════════════════════════"
echo "                    QUESTION 3 of 5"
echo "════════════════════════════════════════════════════════════════"
python subjects/physics/question_3.py
echo ""
read -p "Press Enter to continue to Question 4..."
echo ""

# Question 4
echo "════════════════════════════════════════════════════════════════"
echo "                    QUESTION 4 of 5"
echo "════════════════════════════════════════════════════════════════"
python subjects/physics/question_4.py
echo ""
read -p "Press Enter to continue to Question 5..."
echo ""

# Question 5
echo "════════════════════════════════════════════════════════════════"
echo "                    QUESTION 5 of 5 - FINAL QUESTION!"
echo "════════════════════════════════════════════════════════════════"
python subjects/physics/question_5.py
echo ""

# Summary
echo ""
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║                 🎉 ALL QUESTIONS COMPLETE! 🎉                ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""
echo "Summary of Your Answers:"
echo "------------------------"
echo "✅ Question 1: Photoelectric Effect (Theory)"
echo "✅ Question 2: Newton's First Law (Theory)"
echo "✅ Question 3: Kinetic Energy = 250 J"
echo "✅ Question 4: Thermionic Emission (Theory)"
echo "✅ Question 5: Potential Energy = 392.4 J"
echo ""
echo "You're ready for your SPM trial exam! Good luck! 💪"
echo ""
