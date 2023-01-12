from functions import *

running = True
def main():
    while running:
        clear()
        print("calculator developed by kayla welch")
        print("1; addition")
        print("2: subtraction")
        print("3: multiplication")
        print("4: division")
        print("other: exit")

        operationSelector = input("input number: ")
        clear()

    if operationSelector == "1":
        print(f"sum: {addition()}")
        input()
    elif operationSelector == "2":
        print(f"difference: {subtraction()}")
        input()
    elif operationSelector == "3":
        print(f"product: {multiplication()}")
    elif operationSelector == "4":
        print(f"quotient: {division()}")
    else:
        running = False

# checks if main.py was the file ran
if __name__ == "__main__":

    # if main.py was ran, then start
    main()