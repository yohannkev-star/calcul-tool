# calcul.py - Version main
def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

if __name__ == "__main__":
    result_add = addition(5, 3)
    result_sub = soustraction(5, 3)
    print(f"Addition : {result_add}")
    print(f"Soustraction : {result_sub}")