"""
==============================================================================
PHYSICS QUESTION 2
==============================================================================
Question: Explain Newton's First Law of Motion.

Topic: Mechanics - Newton's Laws of Motion
==============================================================================
"""

def explain_newtons_first_law():
    """
    Complete explanation of Newton's First Law
    """

    explanation = """

    NEWTON'S FIRST LAW OF MOTION
    ============================

    DEFINITION (Simple Version):
    ---------------------------
    An object will remain at rest or continue moving at constant velocity
    unless acted upon by an external force.


    DEFINITION (Formal Version):
    ---------------------------
    Every body continues in its state of rest or uniform motion in a straight
    line unless it is compelled to change that state by an external force
    acting on it.


    KEY CONCEPTS:
    -------------

    1. TWO STATES OF MOTION:

       a) Object at REST:
          - If nothing pushes or pulls it
          - It will stay at rest FOREVER
          - Example: A book on a table stays there until you move it

       b) Object in MOTION:
          - If moving at constant speed in straight line
          - It will keep moving FOREVER (if no force acts on it)
          - Example: A puck on frictionless ice keeps sliding


    2. WHAT IS "CONSTANT VELOCITY"?
       - Same speed
       - Same direction
       - No speeding up or slowing down
       - No turning or changing direction


    3. INERTIA:
       - This law is also called the "Law of Inertia"
       - Inertia = tendency of an object to resist changes in motion
       - Objects "want" to keep doing what they're already doing
       - More mass = more inertia = harder to change motion


    4. REAL-WORLD UNDERSTANDING:

       Why do things stop moving on Earth?
       - NOT because of Newton's First Law failing!
       - Because of FORCES acting on them:
         * Friction (rubbing against surface)
         * Air resistance (drag)
         * Gravity (pulling down)

       In space (no friction):
       - A spacecraft can drift forever
       - No need for engines once at cruising speed!


    5. EXAMPLES IN EVERYDAY LIFE:

       a) Car Suddenly Stops:
          - You jerk forward
          - Why? Your body wants to keep moving (inertia)
          - Seatbelt provides the force to stop you

       b) Pulling Tablecloth:
          - Quick pull leaves dishes in place
          - Why? Dishes' inertia keeps them at rest

       c) Shaking Thermometer:
          - Mercury moves down
          - Why? Mercury's inertia makes it "want" to keep moving

       d) Standing in Bus:
          - Bus accelerates, you fall backward
          - Why? Your body wants to stay at rest (inertia)


    6. IMPORTANT POINTS FOR EXAM:

       ✓ Force is needed to CHANGE motion, not maintain it
       ✓ No force = No change in motion
       ✓ This law explains INERTIA
       ✓ Inertia depends on MASS (not weight!)
       ✓ This law applies in all directions (x, y, z)


    7. COMMON MISCONCEPTIONS (What's WRONG):

       ✗ "Force is needed to keep things moving"
         → NO! Force is needed to CHANGE motion

       ✗ "Things naturally slow down"
         → NO! They slow down because of friction forces

       ✗ "Heavier objects fall faster"
         → NO! (That's a different topic, but still wrong!)


    8. MATHEMATICAL EXPRESSION:

       If ΣF = 0 (sum of forces is zero)
       Then: v = constant (velocity is constant)

       Or: a = 0 (acceleration is zero)

       This means:
       - No net force → No acceleration
       - No acceleration → Constant velocity (or at rest)

    """

    return explanation


def show_diagram():
    """
    Text representation of Newton's First Law scenarios
    """
    print("\n" + "=" * 60)
    print("VISUAL EXAMPLES:")
    print("=" * 60)
    print("""

    SCENARIO 1: Object at Rest
    ===========================

         📦  ←  No forces acting

    The box stays at rest forever (unless a force acts on it)


    SCENARIO 2: Object in Motion (No Friction)
    ===========================================

         →→→→→  🚗  →→→→→

    The car keeps moving at constant speed forever
    (no friction, no air resistance)


    SCENARIO 3: Real World (With Friction)
    =======================================

         →→→→  🚗  →→  🚗  →  🚗  ⏹
                        ↑
                   Friction force

    Friction force opposes motion → Car slows down


    SCENARIO 4: Car Suddenly Stops
    ===============================

    Before:    🚗 →→→     😊 →→→
               Car         Person (both moving)

    After:     🚗 ⏹       😊 →→→ 💥
               Car stops   Person keeps moving (inertia!)
                           → Hits windshield!
                           → WEAR SEATBELT!

    """)


def related_concepts():
    """
    Related physics concepts
    """
    print("=" * 60)
    print("RELATED CONCEPTS:")
    print("=" * 60)
    print("""
    1. MASS vs INERTIA:
       - Mass is a measure of inertia
       - More mass → More inertia → Harder to move/stop
       - SI unit: kilogram (kg)

    2. FORCE:
       - A push or pull on an object
       - Required to change motion
       - SI unit: Newton (N)

    3. VELOCITY:
       - Speed in a specific direction
       - Has magnitude (how fast) and direction
       - SI unit: m/s

    4. ACCELERATION:
       - Rate of change of velocity
       - If a = 0, velocity is constant (First Law!)
       - SI unit: m/s²

    5. NET FORCE (ΣF):
       - Sum of all forces acting on object
       - If ΣF = 0 → Newton's First Law applies
       - If ΣF ≠ 0 → Newton's Second Law applies (F = ma)

    6. EQUILIBRIUM:
       - When ΣF = 0 (forces are balanced)
       - Object is in equilibrium
       - Can be at rest OR moving at constant velocity
    """)


def exam_tips():
    """
    Tips for answering in exams
    """
    print("=" * 60)
    print("📝 HOW TO ANSWER IN YOUR EXAM:")
    print("=" * 60)
    print("""
    STRUCTURE YOUR ANSWER:
    ----------------------

    1. STATE THE LAW:
       "Newton's First Law states that an object will remain at rest
        or continue moving at constant velocity in a straight line
        unless acted upon by an external force."

    2. EXPLAIN INERTIA:
       "This is also known as the Law of Inertia. Inertia is the
        tendency of an object to resist changes in its motion."

    3. GIVE AN EXAMPLE:
       "For example, when a car suddenly brakes, passengers jerk
        forward because their bodies tend to maintain their state
        of motion due to inertia."

    4. MENTION KEY POINT:
       "This law explains why force is needed to CHANGE motion,
        not to maintain it."

    KEYWORDS TO USE:
    ----------------
    ✓ State of rest
    ✓ Uniform motion / Constant velocity
    ✓ External force
    ✓ Inertia
    ✓ Tendency to resist change
    ✓ Straight line
    """)


# Main execution
if __name__ == "__main__":
    print("\n🔬 PHYSICS QUESTION 2: NEWTON'S FIRST LAW")
    print("=" * 60)

    # Show the explanation
    explanation = explain_newtons_first_law()
    print(explanation)

    # Show diagrams
    show_diagram()

    # Show related concepts
    related_concepts()

    # Show exam tips
    exam_tips()

    print("\n" + "=" * 60)
    print("✅ EXPLANATION COMPLETE")
    print("=" * 60)
    print("\n💡 Remember: This is the EASIEST of Newton's laws!")
    print("   Just remember: No force = No change in motion")
    print("=" * 60)
