"""
==============================================================================
PHYSICS QUESTION 1
==============================================================================
Question: Explain the photoelectric effect.

Topic: Quantum Physics - Photoelectric Effect
==============================================================================
"""

def explain_photoelectric_effect():
    """
    Complete explanation of the photoelectric effect
    """

    explanation = """

    THE PHOTOELECTRIC EFFECT
    ========================

    DEFINITION:
    -----------
    The photoelectric effect is a phenomenon where electrons are emitted from
    a metal surface when light (electromagnetic radiation) of sufficient
    frequency shines on it.


    KEY CONCEPTS:
    -------------

    1. WHAT HAPPENS?
       - Light shines on a metal surface
       - Electrons are ejected from the metal
       - These ejected electrons are called "photoelectrons"


    2. IMPORTANT CONDITIONS:
       - Light must have a MINIMUM frequency (threshold frequency)
       - Below this frequency, NO electrons are emitted, no matter how
         bright the light is
       - Above this frequency, electrons ARE emitted


    3. KEY OBSERVATIONS:

       a) Threshold Frequency (f₀):
          - Each metal has a minimum frequency needed
          - Below f₀: NO emission occurs
          - Above f₀: Emission occurs

       b) Intensity of Light:
          - Higher intensity = MORE electrons emitted
          - But does NOT affect the energy of each electron

       c) Frequency of Light:
          - Higher frequency = Higher energy per electron
          - Affects the kinetic energy of ejected electrons


    4. EINSTEIN'S EXPLANATION (1905):
       - Light consists of particles called "photons"
       - Each photon has energy: E = hf
         where: h = Planck's constant (6.63 × 10⁻³⁴ J·s)
                f = frequency of light

       - One photon gives its energy to one electron
       - If photon energy > work function, electron is emitted


    5. ENERGY EQUATION:

       Energy of photon = Work function + Kinetic energy of electron

       hf = φ + KE

       or

       KE = hf - φ

       where: h = Planck's constant
              f = frequency of light
              φ = work function (minimum energy to remove electron)
              KE = kinetic energy of ejected electron


    6. WHY IS THIS IMPORTANT?
       - Proved light has particle properties (wave-particle duality)
       - Led to development of quantum mechanics
       - Used in: solar panels, light sensors, burglar alarms
       - Einstein won Nobel Prize for this explanation!


    7. CANNOT BE EXPLAINED BY CLASSICAL PHYSICS:
       - Classical physics says brighter light (more energy) should
         always eject electrons
       - But experiment shows: low frequency light NEVER ejects electrons,
         no matter how bright!
       - This proved light behaves as particles (photons)

    """

    return explanation


def show_diagram():
    """
    Text representation of photoelectric effect setup
    """
    print("\n" + "=" * 60)
    print("DIAGRAM (TEXT VERSION):")
    print("=" * 60)
    print("""

         Light (photons)
              ↓↓↓↓↓
         ═══════════════
         ║   Metal     ║
         ║   Surface   ║  ←── Electrons ejected (photoelectrons)
         ═══════════════        →  e⁻
                               →  e⁻
                              →  e⁻

    When light hits the metal:
    - Photons transfer energy to electrons
    - If energy is enough, electrons escape the metal
    - These are called photoelectrons

    """)


def key_equations():
    """
    Important equations for photoelectric effect
    """
    print("=" * 60)
    print("KEY EQUATIONS:")
    print("=" * 60)
    print("""
    1. Energy of a photon:
       E = hf = hc/λ

       where: h = Planck's constant = 6.63 × 10⁻³⁴ J·s
              f = frequency (Hz)
              c = speed of light = 3 × 10⁸ m/s
              λ = wavelength (m)

    2. Photoelectric equation (Einstein):
       hf = φ + KEₘₐₓ

       or

       KEₘₐₓ = hf - φ

       where: φ = work function (minimum energy needed)
              KEₘₐₓ = maximum kinetic energy of electron

    3. Threshold frequency:
       f₀ = φ/h

       (minimum frequency needed to emit electrons)

    4. Kinetic energy of electron:
       KE = ½mv²

       where: m = mass of electron
              v = velocity of electron
    """)


# Main execution
if __name__ == "__main__":
    print("\n🔬 PHYSICS QUESTION 1: PHOTOELECTRIC EFFECT")
    print("=" * 60)

    # Show the explanation
    explanation = explain_photoelectric_effect()
    print(explanation)

    # Show diagram
    show_diagram()

    # Show equations
    key_equations()

    print("\n" + "=" * 60)
    print("✅ EXPLANATION COMPLETE")
    print("=" * 60)
    print("""
    📝 EXAM TIP:
    In your exam, remember to include:
    - Definition of photoelectric effect
    - Mention threshold frequency
    - Explain Einstein's photon theory
    - State the equation: hf = φ + KE
    - Mention it proves wave-particle duality
    """)
    print("=" * 60)
