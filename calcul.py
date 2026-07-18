# calcul.py - Version finale avec documentation complète
# Issue #1 : Documentation à compléter - RÉSOLUE

# calcul.py - Version fusionnée
def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

# Fonction principale - VERSION FUSIONNÉE
def main():
    print("=== Calculatrice v1.2 (Fusion) ===")
    print(f"5 + 3 = {addition(5, 3)}")
    print(f"5 - 3 = {soustraction(5, 3)}")
    print(f"4 * 2 = {multiplication(4, 2)}")

if __name__ == "__main__":
    main()