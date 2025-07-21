class Train:
    def __init__(self):
        self.__TotalSeats = 20  # Total number of seats in the train (currently unused)
        self.Seats = [  # 2D list representing seat layout; 'W' for window, 'M' for middle
            ['W', 'M', 'M', 'W'],
            ['W', 'M', 'M', 'W'],
            ['W', 'M', 'M', 'W'],
            ['W', 'M', 'M', 'W'],
            ['W', 'M', 'M', 'W']
        ]
        
    def SeatsAwailable(self):  # Method to count available seats
        count = 0
        for i in self.Seats:  # Iterate through each row
            for a in i:  # Iterate through each seat in the row
                if a != 'B':  # Check if the seat is not booked
                    count += 1
        return count  # Return the total count of available seats
    
    def BookSeat(self, Option):  # Method to book a seat based on the given option ('W' or 'M')
        a = self.Seats
        for i in range(0, len(a)):  # Iterate through rows
            for j in range(0, len(a[0])):  # Iterate through seats in the row
                if a[i][j] == Option and a[i][j] != 'B':  # Check if the seat matches the option and is not booked
                    a[i][j] = 'B'  # Mark the seat as booked
                    self.Seats = a  # Update the Seats attribute (unnecessary reassignment)
                    return [i, j]  # Return the position of the booked seat
        return "No Seates are awailable for your selected option"  # Return message if no seat is available
    
    def CancelSeat(self, SeatID):  # Method to cancel a booked seat
        a, b = SeatID  # Unpack the seat ID into row and column indices
        c = self.Seats
        if c[a][b] != 'B':  # Check if the seat is not booked
            return "Entered Wrong SeatID"  # Return error message for invalid SeatID
        digit = a * 10 + b  # Calculate a unique number for the seat (used to determine seat type)
        if digit % 10 == 0 or digit % 10 == 3:  # Check if the seat is a window seat
            c[a][b] = 'W'  # Reset the seat to 'W' (window)
            self.Seats = c  # Update the Seats attribute (unnecessary reassignment)
            print(self.Seats)  # Print the updated seat layout
            return "the seat has been canceled"  # Return success message
        
        c[a][b] = 'M'  # Reset the seat to 'M' (middle)
        self.Seats = c  # Update the Seats attribute (unnecessary reassignment)
        return "the seat has been canceled"  # Return success message
    
    def SeatPositions(self):  # Method to return the current seat layout
        return self.Seats  # Return the Seats attribute