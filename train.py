class Train:
    def __init__(self):
        self.__TotalSeats = 20  # Total number of seats in the train
        self.Seats = [  # 2D list representing seat layout: 'W' (Window), 'M' (Middle), 'B' (Booked)
            ['W', 'M', 'M', 'W'],
            ['W', 'M', 'M', 'W'],
            ['W', 'M', 'M', 'W'],
            ['W', 'M', 'M', 'W'],
            ['W', 'M', 'M', 'W']
        ]
        
    def SeatsAwailable(self):  # Method to count the number of available seats
        count = 0
        for i in self.Seats:  # Iterate through each row
            for a in i:  # Iterate through each seat in the row
                if a != 'B':  # Check if the seat is not booked
                    count += 1
        return count  # Return the total count of available seats
    
    def BookSeat(self, Option):  # Method to book a seat based on the user's preference ('W' or 'M')
        a = self.Seats
        for i in range(0, len(a)):  # Iterate through each row
            for j in range(0, len(a[0])):  # Iterate through each seat in the row
                if a[i][j] == Option and a[i][j] != 'B':  # Check if the seat matches the option and is not booked
                    a[i][j] = 'B'  # Mark the seat as booked
                    self.Seats = a  # Update the seat layout
                    return [i, j]  # Return the position of the booked seat
        return "No Seates are awailable for your selected option"  # Return a message if no seats are available
    
    def CancelSeat(self, SeatID):  # Method to cancel a booked seat
        a, b = SeatID  # Extract row and column indices from SeatID
        c = self.Seats
        if c[a][b] != 'B':  # Check if the seat is not booked
            return "Entered Wrong SeatID"  # Return an error message if the seat is not booked
        digit = a * 10 + b  # Calculate a unique identifier for the seat (unnecessary logic)
        if digit % 10 == 0 or digit % 10 == 3:  # Check if the seat is a window seat
            c[a][b] = 'W'  # Reset the seat to 'W' (Window)
            self.Seats = c  # Update the seat layout
            print(self.Seats)  # Print the updated seat layout (should be removed)
            return "the seat has been canceled"  # Return a success message
        
        c[a][b] = 'M'  # Reset the seat to 'M' (Middle) for non-window seats
        self.Seats = c  # Update the seat layout
        return "the seat has been canceled"  # Return a success message
    
    def SeatPositions(self):  # Method to return the current seat layout
        return self.Seats