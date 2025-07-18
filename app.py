from flask import Flask, render_template, request  # Import necessary Flask modules

from train import Train  # Import the Train class

app = Flask(__name__)  # Initialize the Flask application
a = Train()  # Create an instance of the Train class

# Dropdown options for seat type
dropdown_options = [
    {'value': 'W', 'text': 'Window'},  # Window seat option
    {'value': 'M', 'text': 'Middle'}  # Middle seat option
]

# Dropdown options for row selection
dropdown_options2 = [
    {'value': 0, 'text': '0'},  # Row 0
    {'value': 1, 'text': '1'},  # Row 1
    {'value': 2, 'text': '2'},  # Row 2
    {'value': 3, 'text': '3'}   # Row 3
]

# Dropdown options for column selection
dropdown_options3 = [
    {'value': 0, 'text': '0'},  # Column 0
    {'value': 1, 'text': '1'},  # Column 1
    {'value': 2, 'text': '2'},  # Column 2
    {'value': 3, 'text': '3'},  # Column 3
    {'value': 4, 'text': '4'}   # Column 4
]

@app.route('/')  # Base URL route
def index():
    # Render the index.html template with dropdown options
    return render_template('index.html', Options=dropdown_options, Pos1=dropdown_options2, Pos2=dropdown_options3)

@app.route('/Awailable', methods=['POST'])  # Route to check available seats
def AwailableSeateCount():
    # Render the index.html template with available seats information
    return render_template('index.html', seates=a.SeatsAwailable())

@app.route('/Awailable/position', methods=['POST'])  # Route to check seat positions
def AwailableSeatePos():
    # Render the index.html template with seat positions and dropdown options
    return render_template('index.html', position=a.SeatPositions(), Options=dropdown_options, Pos1=dropdown_options2, Pos2=dropdown_options3)

@app.route('/BookSeat', methods=['POST'])  # Route to book a seat
def Bookseat():
    text = request.form.get('BookSeat')  # Get the seat booking input from the form
    # Render the index.html template with booking message and dropdown options
    return render_template('index.html', message1=a.BookSeat(text), Options=dropdown_options, Pos1=dropdown_options2, Pos2=dropdown_options3)

@app.route('/CancelSeat', methods=['POST'])  # Route to cancel a seat
def Cancelseat():
    text1 = request.form.get('CancelSeatRow')  # Get the row input for seat cancellation
    text2 = request.form.get('CancelSeatCol')  # Get the column input for seat cancellation
    m = [int(text1), int(text2)]  # Convert inputs to integers and store as a list
    # Render the index.html template with cancellation message and dropdown options
    return render_template('index.html', message2=a.CancelSeat(m), Options=dropdown_options, Pos1=dropdown_options2, Pos2=dropdown_options3)

if __name__ == '__main__':  # Entry point of the application
    app.run()  # Run the Flask application