# calcul.py - Version hotfix
def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

# Fonction principale - VERSION HOTFIX
def main():
    print("=== Calculatrice v1.1 (Hotfix) ===")
    print(f"5 + 3 = {addition(5, 3)}")
    print(f"5 - 3 = {soustraction(5, 3)}")
    print(f"4 * 2 = {multiplication(4, 2)}")

if __name__ == "__main__":
    main()