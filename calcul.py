# calcul.py - Version main
def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

# Fonction principale - VERSION MAIN
def main():
    print("=== Calculatrice v1.0 (Main) ===")
    print(f"5 + 3 = {addition(5, 3)}")
    print(f"5 - 3 = {soustraction(5, 3)}")

if __name__ == "__main__":
    main()