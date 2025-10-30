"""
==============================================================================
PHYSICS QUESTION 3
==============================================================================
Question: Calculate the kinetic energy when mass is 5 kg and velocity is 10 m/s.

Topic: Energy - Kinetic Energy
==============================================================================
"""

def solve_question():
    """
    Calculate kinetic energy using the formula KE = 1/2 × m × v²
    """

    # STEP 1: Write down what you know (the "given" values)
    mass = 5        # kg (kilograms)
    velocity = 10   # m/s (meters per second)

    # STEP 2: Write the formula you need
    # Formula: KE = 1/2 × m × v²
    # Where:
    #   KE = kinetic energy (Joules)
    #   m = mass (kg)
    #   v = velocity (m/s)

    # STEP 3: Calculate the answer
    # In Python, we use ** for "power" (so v² is written as v**2)
    # We use * for multiply
    # So: KE = 0.5 × mass × velocity²

    kinetic_energy = 0.5 * mass * velocity**2

    # STEP 4: Return (give back) the answer
    return kinetic_energy


def show_working():
    """
    Show your working like you would write on paper
    """
    print("=" * 60)
    print("SOLUTION:")
    print("=" * 60)

    print("\nStep 1: What do we know? (Given)")
    print("  - Mass (m) = 5 kg")
    print("  - Velocity (v) = 10 m/s")
    print("  - We need to find: Kinetic Energy (KE)")

    print("\nStep 2: What formula do we use?")
    print("  - Formula: KE = ½ × m × v²")
    print("  - Or: KE = 0.5 × m × v²")
    print("  - Where: KE is in Joules (J)")

    print("\nStep 3: Substitute values into formula")
    print("  - KE = 0.5 × 5 × (10)²")
    print("  - KE = 0.5 × 5 × 100")

    print("\nStep 4: Calculate")
    print("  - KE = 0.5 × 5 × 100")
    print("  - KE = 2.5 × 100")
    print("  - KE = 250 J")

    print("\n" + "=" * 60)


def explain_concept():
    """
    Explain what kinetic energy is
    """
    print("\n" + "=" * 60)
    print("WHAT IS KINETIC ENERGY?")
    print("=" * 60)
    print("""
    Kinetic Energy is the energy an object has because it is MOVING.

    Key Points:
    -----------
    • The faster something moves → More kinetic energy
    • The heavier something is → More kinetic energy
    • If something is NOT moving → Zero kinetic energy

    Formula: KE = ½mv²
    --------
    Notice that velocity is SQUARED (v²)!
    This means: If you double the speed, kinetic energy increases 4 times!

    Example:
    --------
    A moving car has kinetic energy.
    When you brake, that energy is converted to:
    - Heat (in the brakes)
    - Sound
    - Deformation (if you crash)

    Units:
    ------
    • Kinetic Energy: Joules (J)
    • Mass: kilograms (kg)
    • Velocity: meters per second (m/s)

    SI Unit of Energy = Joule (J) = kg⋅m²/s²
    """)


def check_calculation():
    """
    Verify the calculation step by step
    """
    print("=" * 60)
    print("VERIFICATION (Double-check our answer):")
    print("=" * 60)

    mass = 5
    velocity = 10

    print(f"\nGiven: m = {mass} kg, v = {velocity} m/s")
    print(f"\nStep-by-step calculation:")
    print(f"  1. Calculate v² = {velocity}² = {velocity**2}")
    print(f"  2. Multiply by mass: {mass} × {velocity**2} = {mass * velocity**2}")
    print(f"  3. Multiply by 0.5: 0.5 × {mass * velocity**2} = {0.5 * mass * velocity**2}")
    print(f"\n✓ Answer confirmed: {0.5 * mass * velocity**2} J")


def practice_problems():
    """
    Similar practice problems
    """
    print("\n" + "=" * 60)
    print("PRACTICE PROBLEMS (Try these!):")
    print("=" * 60)
    print("""
    1. Calculate KE when m = 10 kg, v = 5 m/s
       Answer: KE = 0.5 × 10 × 5² = 0.5 × 10 × 25 = 125 J

    2. Calculate KE when m = 2 kg, v = 20 m/s
       Answer: KE = 0.5 × 2 × 20² = 0.5 × 2 × 400 = 400 J

    3. A car (m = 1000 kg) moves at 15 m/s. Find KE.
       Answer: KE = 0.5 × 1000 × 15² = 0.5 × 1000 × 225 = 112,500 J

    TIP: To solve these, just change the values of 'mass' and 'velocity'
         in the solve_question() function above!
    """)


def exam_tips():
    """
    Tips for answering kinetic energy questions in exams
    """
    print("=" * 60)
    print("📝 EXAM TIPS:")
    print("=" * 60)
    print("""
    ✓ ALWAYS write the formula first: KE = ½mv²

    ✓ Show EVERY step:
      1. Write what is given
      2. Write the formula
      3. Substitute values
      4. Calculate step by step

    ✓ Don't forget to SQUARE the velocity!
      (This is the most common mistake!)

    ✓ Include UNITS in your answer (Joules or J)

    ✓ Check if your answer makes sense:
      - Larger mass OR faster speed = More KE
      - Answer should be positive (energy can't be negative!)

    ✓ Common values to remember:
      - ½ = 0.5
      - KE is always positive (or zero if not moving)

    COMMON MISTAKES TO AVOID:
    -------------------------
    ✗ Forgetting to square the velocity
    ✗ Using wrong units (check kg and m/s!)
    ✗ Forgetting the ½ (or 0.5)
    ✗ Not showing working
    """)


# Main execution
if __name__ == "__main__":
    print("\n🔬 PHYSICS QUESTION 3: KINETIC ENERGY CALCULATION")
    print("=" * 60)

    # Calculate the answer
    answer = solve_question()

    # Show the working
    show_working()

    # Display the final answer
    print(f"\n✅ FINAL ANSWER: {answer} J (Joules)")
    print("=" * 60)

    # Explain the concept
    explain_concept()

    # Verify calculation
    check_calculation()

    # Show practice problems
    practice_problems()

    # Show exam tips
    exam_tips()

    print("\n" + "=" * 60)
    print("🎉 CALCULATION COMPLETE!")
    print("=" * 60)
    print("\n💡 TIP: This is your first CALCULATION question!")
    print("   See how Python does all the math for you?")
    print("   Just change the numbers to solve similar problems!")
    print("=" * 60)
