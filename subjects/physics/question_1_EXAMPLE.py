"""
==============================================================================
PHYSICS QUESTION 1 - COMPLETE EXAMPLE
==============================================================================
Question: A car travels at a constant speed of 20 m/s for 10 seconds.
          Calculate the distance traveled.

Topic: Kinematics - Distance and Speed

THIS IS A COMPLETE EXAMPLE - Look at this to understand how to fill in your questions!
==============================================================================
"""

def solve_question():
    """
    This is where you write your solution
    """

    # STEP 1: Write down what you know (the "given" values)
    speed = 20      # meters per second (m/s)
    time = 10       # seconds (s)

    # STEP 2: Write the formula you need
    # Formula: distance = speed × time
    # In math: s = v × t

    # STEP 3: Calculate the answer
    distance = speed * time

    # STEP 4: Return (give back) the answer
    return distance


def show_working():
    """
    Show your working like you would on paper
    """
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


if __name__ == "__main__":
    print("\n🔬 PHYSICS QUESTION 1 - COMPLETE EXAMPLE")
    print("=" * 60)

    # Calculate the answer
    answer = solve_question()

    # Show the working
    show_working()

    # Display the final answer
    print(f"\n✅ FINAL ANSWER: {answer} meters")
    print("=" * 60)
    print("\n💡 TIP: Now you know how to fill in question_1.py!")
    print("   Just copy this pattern and use your own question!")
