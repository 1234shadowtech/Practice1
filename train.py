class Train:
    def __init__(self):
        self.__TotalSeats = 20  # Total number of seats in the train
        self.Seats = [  # 2D list representing seat layout with 'W' (Window) and 'M' (Middle) seats
            ['W', 'M', 'M', 'W'],
            ['W', 'M', 'M', 'W'],
            ['W', 'M', 'M', 'W'],
            ['W', 'M', 'M', 'W'],
            ['W', 'M', 'M', 'W']
        ]
        
    def SeatsAwailable(self):
        count = 0  # Initialize seat count
        for i in self.Seats:  # Iterate through each row
            for a in i:  # Iterate through each seat in the row
                if a != 'B':  # Check if the seat is not booked
                    count += 1  # Increment count for available seats
        return count  # Return the total count of available seats

    def BookSeat(self, Option):
        a = self.Seats  # Reference to the seat layout
        for i in range(0, len(a)):  # Iterate through rows
            for j in range(0, len(a[0])):  # Iterate through columns
                if a[i][j] == Option and a[i][j] != 'B':  # Check if the seat matches the option and is not booked
                    a[i][j] = 'B'  # Mark the seat as booked
                    self.Seats = a  # Update the seat layout (unnecessary assignment)
                    return [i, j]  # Return the position of the booked seat
        return "No Seates are awailable for your selected option"  # Return message if no seat is available

    def CancelSeat(self, SeatID):
        a, b = SeatID  # Unpack the seat ID into row and column indices
        c = self.Seats  # Reference to the seat layout
        if c[a][b] != 'B':  # Check if the seat is not booked
            return "Entered Wrong SeatID"  # Return error message for invalid seat ID
        digit = a * 10 + b  # Calculate a unique identifier for the seat (used for determining seat type)
        if digit % 10 == 0 or digit % 10 == 3:  # Check if the seat is a window seat
            c[a][b] = 'W'  # Reset the seat to 'W' (Window)
            self.Seats = c  # Update the seat layout
            print(self.Seats)  # Print the updated seat layout (debugging purpose)
            return "the seat has been canceled"  # Return success message
        c[a][b] = 'M'  # Reset the seat to 'M' (Middle)
        self.Seats = c  # Update the seat layout
        return "the seat has been canceled"  # Return success message

    def SeatPositions(self):
        return self.Seats  # Return the current seat layout
               
def speak():
    print("Thank you")  # Print a thank-you message