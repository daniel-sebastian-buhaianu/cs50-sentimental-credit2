# Main function to start the program
def main():
    card_number = getUserInput()

    if isValid(card_number):
        print(getCardType(card_number))
    else:
        print("INVALID")

# Function to ask for user input (card number) and return it as a string
def getUserInput():
    while True:
        card_number = input("Number: ")
        if card_number.isnumeric():
            return card_number

# Function to check if card number is valid according to Luhn's Algorithm
def isValid(card_number):
    total_sum = 0
    reverse_digits = card_number[::-1]  # Reverse the card number to process right-to-left

    # Apply Luhn's algorithm
    for i, digit in enumerate(reverse_digits):
        num = int(digit)
        if i % 2 == 1:  # Every second digit, starting from the right (i.e., after reversal)
            num *= 2
            if num > 9:
                num -= 9  # If doubling results in a number > 9, subtract 9 (same as sum of digits)
        total_sum += num

    # Return True if total sum is divisible by 10
    return total_sum % 10 == 0

# Function to determine card type based on its number
def getCardType(card_number):
    n = len(card_number)

    if n == 15 and card_number[:2] in ("34", "37"):
        return "AMEX"

    if n == 16 and card_number[:2] in ("51", "52", "53", "54", "55"):
        return "MASTERCARD"

    if card_number[0] == "4" and n in (13, 16):
        return "VISA"

    return "INVALID"

# Run the main function
if __name__ == "__main__":
    main()

