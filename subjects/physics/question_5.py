"""
==============================================================================
PHYSICS QUESTION 5 - THE FINAL QUESTION! 🎉
==============================================================================
Question: Calculate the gravitational potential energy when mass is 8 kg
          and height is 5 meters.

Topic: Energy - Gravitational Potential Energy
==============================================================================
"""

def solve_question():
    """
    Calculate gravitational potential energy using the formula PE = mgh
    """

    # STEP 1: Write down what you know (the "given" values)
    mass = 8            # kg (kilograms)
    height = 5          # m (meters)
    gravity = 9.81      # m/s² (acceleration due to gravity on Earth)

    # Note: Sometimes in exams, g = 10 m/s² is used for simplicity
    # But the more accurate value is g = 9.81 m/s²

    # STEP 2: Write the formula you need
    # Formula: PE = m × g × h
    # Where:
    #   PE = gravitational potential energy (Joules)
    #   m = mass (kg)
    #   g = acceleration due to gravity (9.81 m/s²)
    #   h = height (m)

    # STEP 3: Calculate the answer
    # In Python, we use * for multiply
    # So: PE = mass × gravity × height

    potential_energy = mass * gravity * height

    # STEP 4: Return (give back) the answer
    return potential_energy


def show_working():
    """
    Show your working like you would write on paper
    """
    print("=" * 60)
    print("SOLUTION:")
    print("=" * 60)

    print("\nStep 1: What do we know? (Given)")
    print("  - Mass (m) = 8 kg")
    print("  - Height (h) = 5 m")
    print("  - Gravity (g) = 9.81 m/s²")
    print("  - We need to find: Gravitational Potential Energy (PE)")

    print("\nStep 2: What formula do we use?")
    print("  - Formula: PE = m × g × h")
    print("  - Or: PE = mgh")
    print("  - Where: PE is in Joules (J)")

    print("\nStep 3: Substitute values into formula")
    print("  - PE = 8 × 9.81 × 5")
    print("  - PE = 78.48 × 5")

    print("\nStep 4: Calculate")
    print("  - PE = 78.48 × 5")
    print("  - PE = 392.4 J")

    print("\n" + "=" * 60)


def explain_concept():
    """
    Explain what gravitational potential energy is
    """
    print("\n" + "=" * 60)
    print("WHAT IS GRAVITATIONAL POTENTIAL ENERGY?")
    print("=" * 60)
    print("""
    Gravitational Potential Energy is the energy an object has because
    of its POSITION (height) above the ground.

    Key Points:
    -----------
    • The higher something is → More potential energy
    • The heavier something is → More potential energy
    • If something is at ground level (h=0) → Zero potential energy

    Formula: PE = mgh
    --------
    Notice that height is NOT squared (unlike kinetic energy!)
    - Double the height → Double the potential energy
    - Double the mass → Double the potential energy

    Real-World Examples:
    -------------------
    1. Water at top of waterfall:
       - Has high PE
       - Falls down → PE converts to KE (kinetic energy)
       - Hits bottom → KE converts to sound, heat, splash

    2. Roller coaster at the top:
       - Maximum PE
       - Rolls down → PE → KE
       - Goes fast at bottom (maximum KE, minimum PE)

    3. Book on a shelf:
       - Has PE because it's above ground
       - Falls → PE converts to KE
       - Hits floor → Makes sound (energy transfer)

    Units:
    ------
    • Potential Energy: Joules (J)
    • Mass: kilograms (kg)
    • Gravity: meters per second squared (m/s²)
    • Height: meters (m)

    SI Unit of Energy = Joule (J) = kg⋅m²/s²

    Important Constant:
    ------------------
    g = 9.81 m/s² (on Earth)
    g = 10 m/s² (often used in exams for simplicity)

    On other planets, g is different:
    - Moon: g ≈ 1.6 m/s²
    - Mars: g ≈ 3.7 m/s²
    - Jupiter: g ≈ 24.8 m/s²
    """)


def check_calculation():
    """
    Verify the calculation step by step
    """
    print("=" * 60)
    print("VERIFICATION (Double-check our answer):")
    print("=" * 60)

    mass = 8
    gravity = 9.81
    height = 5

    print(f"\nGiven: m = {mass} kg, g = {gravity} m/s², h = {height} m")
    print(f"\nStep-by-step calculation:")
    print(f"  1. Multiply m × g: {mass} × {gravity} = {mass * gravity}")
    print(f"  2. Multiply result by h: {mass * gravity} × {height} = {mass * gravity * height}")
    print(f"\n✓ Answer confirmed: {mass * gravity * height} J")

    print(f"\nAlternative (if g = 10 m/s²):")
    print(f"  PE = {mass} × 10 × {height} = {mass * 10 * height} J")
    print(f"  (This is the simpler version sometimes used in exams)")


def energy_comparison():
    """
    Compare with kinetic energy (Question 3)
    """
    print("\n" + "=" * 60)
    print("COMPARISON: POTENTIAL ENERGY vs KINETIC ENERGY")
    print("=" * 60)
    print("""
    Remember Question 3? We calculated Kinetic Energy!
    Now let's compare both types of energy:

    POTENTIAL ENERGY (PE)      |  KINETIC ENERGY (KE)
    ===========================|==========================
    Energy due to POSITION     |  Energy due to MOTION
    (height above ground)      |  (speed of object)
                               |
    Formula: PE = mgh          |  Formula: KE = ½mv²
                               |
    Depends on HEIGHT          |  Depends on VELOCITY
    Higher → More PE           |  Faster → More KE
                               |
    Can be zero (at ground)    |  Can be zero (at rest)
                               |
    Example: Book on shelf     |  Example: Moving car
    Example: Water at top      |  Example: Flying bullet
                               |

    ENERGY CONVERSION:
    ------------------
    PE can convert to KE and vice versa!

    Example: Dropping a ball
    - At top: Maximum PE, Zero KE (not moving yet)
    - Falling: PE converts to KE
    - At bottom: Zero PE (ground level), Maximum KE (moving fast!)

    Total Energy = PE + KE (Conservation of Energy!)
    """)


def practice_problems():
    """
    Similar practice problems
    """
    print("\n" + "=" * 60)
    print("PRACTICE PROBLEMS (Try these!):")
    print("=" * 60)
    print("""
    1. Calculate PE when m = 10 kg, h = 3 m (use g = 10)
       Answer: PE = 10 × 10 × 3 = 300 J

    2. Calculate PE when m = 5 kg, h = 20 m (use g = 10)
       Answer: PE = 5 × 10 × 20 = 1000 J

    3. A person (m = 60 kg) stands on a 2m platform. Find PE. (use g = 10)
       Answer: PE = 60 × 10 × 2 = 1200 J

    4. An apple (m = 0.2 kg) on a tree at h = 4 m. Find PE. (use g = 10)
       Answer: PE = 0.2 × 10 × 4 = 8 J

    TIP: To solve these, just change the values of 'mass' and 'height'
         in the solve_question() function above!

    BONUS: What if the apple falls?
    At the top: PE = 8 J, KE = 0 J
    At the bottom: PE = 0 J, KE = 8 J
    (All PE converted to KE!)
    """)


def exam_tips():
    """
    Tips for answering potential energy questions in exams
    """
    print("=" * 60)
    print("📝 EXAM TIPS:")
    print("=" * 60)
    print("""
    ✓ ALWAYS write the formula first: PE = mgh

    ✓ Show EVERY step:
      1. Write what is given
      2. Write the formula
      3. Substitute values
      4. Calculate step by step

    ✓ Check which value of g to use:
      - If question says "use g = 10 m/s²", use 10
      - If it says "use g = 9.81 m/s²", use 9.81
      - If it doesn't specify, ask or use 10 for simplicity

    ✓ Include UNITS in your answer (Joules or J)

    ✓ Make sure all units match:
      - Mass in kg (if in grams, divide by 1000)
      - Height in m (if in cm, divide by 100)

    ✓ Height is measured from a reference point:
      - Usually from the ground (h = 0 at ground level)
      - Sometimes from a table or platform

    ✓ Check if your answer makes sense:
      - Higher height OR more mass = More PE
      - Answer should be positive (energy can't be negative!)

    COMMON MISTAKES TO AVOID:
    -------------------------
    ✗ Forgetting to multiply by g (gravity)
    ✗ Squaring the height (NO! PE is NOT mgh²)
    ✗ Using wrong value of g
    ✗ Forgetting units
    ✗ Not converting cm to m, or grams to kg
    ✗ Confusing PE with KE

    REMEMBER:
    ---------
    PE = mgh    (m-g-h, think "mega height!")
    KE = ½mv²   (has ½ and v is squared)
    """)


# Main execution
if __name__ == "__main__":
    print("\n🔬 PHYSICS QUESTION 5: GRAVITATIONAL POTENTIAL ENERGY")
    print("=" * 60)
    print("🎉 THIS IS YOUR FINAL QUESTION! Let's finish strong! 🎉")
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

    # Compare with kinetic energy
    energy_comparison()

    # Show practice problems
    practice_problems()

    # Show exam tips
    exam_tips()

    print("\n" + "=" * 60)
    print("🎉 CALCULATION COMPLETE!")
    print("=" * 60)
    print("\n💡 CONGRATULATIONS! You've completed ALL 5 QUESTIONS!")
    print("   You now have:")
    print("   ✅ Question 1: Photoelectric Effect")
    print("   ✅ Question 2: Newton's First Law")
    print("   ✅ Question 3: Kinetic Energy = 250 J")
    print("   ✅ Question 4: Thermionic Emission")
    print("   ✅ Question 5: Potential Energy = 392.4 J")
    print("\n   You're ready for your SPM trial exam! 💪")
    print("=" * 60)
