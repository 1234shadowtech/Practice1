from flask import Flask, render_template, request  # Import necessary Flask modules

from train import Train, speak  # Import Train class and speak function from train module

app = Flask(__name__)  # Initialize Flask app
a = Train()  # Create an instance of the Train class

# Dropdown options for seat types
dropdown_options = [
    {'value': 'W', 'text': 'Window'},  # Window seat option
    {'value': 'M', 'text': 'Middle'}  # Middle seat option
]

# Dropdown options for row positions
dropdown_options2 = [
    {'value': 0, 'text': '0'},  # Row 0
    {'value': 1, 'text': '1'},  # Row 1
    {'value': 2, 'text': '2'},  # Row 2
    {'value': 3, 'text': '3'}   # Row 3
]

# Dropdown options for column positions
dropdown_options3 = [
    {'value': 0, 'text': '0'},  # Column 0
    {'value': 1, 'text': '1'},  # Column 1
    {'value': 2, 'text': '2'},  # Column 2
    {'value': 3, 'text': '3'},  # Column 3
    {'value': 4, 'text': '4'}   # Column 4
]

@app.route('/')  # Base URL route
def index():
    speak()  # Call the speak function (purpose unclear)
    return render_template('index.html', Options=dropdown_options, Pos1=dropdown_options2, Pos2=dropdown_options3)  # Render index.html with dropdown options

@app.route('/Awailable', methods=['POST'])  # Route to check available seats
def AwailableSeateCount():
    return render_template('index.html', seates=a.SeatsAwailable())  # Render index.html with available seats data

@app.route('/Awailable/position', methods=['POST'])  # Route to check seat positions
def AwailableSeatePos():
    return render_template('index.html', position=a.SeatPositions(), Options=dropdown_options, Pos1=dropdown_options2, Pos2=dropdown_options3)  # Render index.html with seat positions and dropdown options

@app.route('/BookSeat', methods=['POST'])  # Route to book a seat
def Bookseat():
    text = request.form.get('BookSeat')  # Get seat booking input from form
    return render_template('index.html', message1=a.BookSeat(text), Options=dropdown_options, Pos1=dropdown_options2, Pos2=dropdown_options3)  # Render index.html with booking message and dropdown options

@app.route('/CancelSeat', methods=['POST'])  # Route to cancel a seat
def Cancelseat():
    text1 = request.form.get('CancelSeatRow')  # Get row input for seat cancellation
    text2 = request.form.get('CancelSeatCol')  # Get column input for seat cancellation
    m = [int(text1), int(text2)]  # Convert inputs to integers and store in a list
    return render_template('index.html', message2=a.CancelSeat(m), Options=dropdown_options, Pos1=dropdown_options2, Pos2=dropdown_options3)  # Render index.html with cancellation message and dropdown options

if __name__ == '__main__':
    app.run()  # Run the Flask app