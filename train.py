class Train:
    def __init__(self):
        self.__TotalSeats = 20  # Total number of seats in the train
        self.Seats = [  # 2D list representing seat arrangement; 'W' for window, 'M' for middle, 'B' for booked
            ['W', 'M', 'M', 'W'],
            ['W', 'M', 'M', 'W'],
            ['W', 'M', 'M', 'W'],
            ['W', 'M', 'M', 'W'],
            ['W', 'M', 'M', 'W']
        ]
        
    def SeatsAwailable(self):  # Method to count available seats
        count = 0  # Initialize counter for available seats
        for i in self.Seats:  # Iterate through rows of seats
            for a in i:  # Iterate through individual seats
                if a != 'B':  # Check if the seat is not booked
                    count += 1  # Increment counter for available seats
        return count  # Return the total count of available seats
    
    def BookSeat(self, Option):  # Method to book a seat based on preference ('W' or 'M')
        a = self.Seats  # Reference to the seat arrangement
        for i in range(0, len(a)):  # Iterate through rows
            for j in range(0, len(a[0])):  # Iterate through columns
                if a[i][j] == Option and a[i][j] != 'B':  # Check if the seat matches preference and is not booked
                    a[i][j] = 'B'  # Mark the seat as booked
                    self.Seats = a  # Update the seat arrangement
                    return [i, j]  # Return the position of the booked seat
        return "No Seates are awailable for your selected option"  # Return message if no seat matches preference
    
    def CancelSeat(self, SeatID):  # Method to cancel a booked seat
        a, b = SeatID  # Extract row and column indices from SeatID
        c = self.Seats  # Reference to the seat arrangement
        if c[a][b] != 'B':  # Check if the seat is not booked
            return "Entered Wrong SeatID"  # Return error message for invalid SeatID
        digit = a * 10 + b  # Calculate a unique identifier for the seat
        if digit % 10 == 0 or digit % 10 == 3:  # Check if the seat is a window seat
            c[a][b] = 'W'  # Reset the seat to 'W' (window)
            self.Seats = c  # Update the seat arrangement
            print(self.Seats)  # Print the updated seat arrangement (inconsistent behavior)
            return "the seat has been canceled"  # Return success message
        c[a][b] = 'M'  # Reset the seat to 'M' (middle)
        self.Seats = c  # Update the seat arrangement
        return "the seat has been canceled"  # Return success message
    
    def SeatPositions(self):  # Method to return the current seat arrangement
        return self.Seats  # Return the 2D list of seats