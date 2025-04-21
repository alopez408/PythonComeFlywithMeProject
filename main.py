# Come Fly with Me - Airplane Seat Booking System

# Constants
TOTAL_SEATS = 20
FIRST_CLASS_SEATS = [1, 2, 3, 4]
EMERGENCY_SEATS = [9, 10, 11, 12]
FIRST_CLASS_FEE = 50.00

# Initialize seat map: dictionary with seat number and availability
seats = {i: {"taken": False, "type": "regular"} for i in range(1, TOTAL_SEATS + 1)}
for seat in FIRST_CLASS_SEATS:
    seats[seat]["type"] = "first-class"
for seat in EMERGENCY_SEATS:
    seats[seat]["type"] = "emergency"

def display_seat_map():
    print("\nSeat Map:")
    for i in range(1, TOTAL_SEATS + 1):
        seat_status = "X" if seats[i]["taken"] else str(i)
        print(f"[{seat_status:^3}]", end=' ')
        if i % 4 == 0:
            print()  # New row
    print()

def get_seat_choice():
    while True:
        try:
            seat_number = int(input("Enter seat number you want to purchase (1-20): "))
            if seat_number < 1 or seat_number > TOTAL_SEATS:
                print("Invalid seat number. Please choose between 1 and 20.")
            elif seats[seat_number]["taken"]:
                print("Sorry, that seat is already taken.")
            elif seats[seat_number]["type"] == "emergency":
                confirm = input("You selected an emergency seat. Do you agree to assist in an emergency? (yes/no): ").strip().lower()
                if confirm != "yes":
                    print("You must agree to the terms to sit in an emergency seat.")
                else:
                    return seat_number
            else:
                return seat_number
        except ValueError:
            print("Please enter a valid number.")

def purchase_seats():
    total_cost = 0.0
    while True:
        display_seat_map()
        seat = get_seat_choice()

        seat_type = seats[seat]["type"]
        if seat_type == "first-class":
            print(f"Seat {seat} is a first-class seat. A fee of ${FIRST_CLASS_FEE:.2f} applies.")
            confirm = input("Do you want to proceed with the purchase? (yes/no): ").strip().lower()
            if confirm != "yes":
                print("Purchase cancelled.")
                continue
            total_cost += FIRST_CLASS_FEE

        seats[seat]["taken"] = True
        print(f"Seat {seat} has been successfully booked.\n")

        another = input("Would you like to book another seat? (yes/no): ").strip().lower()
        if another != "yes":
            break

    print(f"\nTotal cost for your booking: ${total_cost:.2f}")
    print("Thank you for booking with us!")

# Start the program
def main():
    print("✈️ Welcome to Come Fly with Me - Airplane Seat Booking System ✈️")
    purchase_seats()

if __name__ == "__main__":
    main()
