from flask import Flask, render_template, request  # Importing Flask for web application and render_template for rendering HTML templates

from train import Train  # Importing the Train class from the train module

app = Flask(__name__)  # Initializing the Flask application
a = Train()  # Creating an instance of the Train class
dropdown_options = [  # Dropdown options for seat type
    {'value': 'W', 'text': 'Window'},
    {'value': 'M', 'text': 'Middle'}
]
dropdown_options2 = [  # Dropdown options for position 1
    {'value': 0, 'text': '0'},
    {'value': 1, 'text': '1'},
    {'value': 2, 'text': '2'},
    {'value': 3, 'text': '3'}
]
dropdown_options3 = [  # Dropdown options for position 2
    {'value': 0, 'text': '0'},
    {'value': 1, 'text': '1'},
    {'value': 2, 'text': '2'},
    {'value': 3, 'text': '3'},
    {'value': 4, 'text': '4'}
]

@app.route('/')  # Base URL route
def index():
    # Rendering the index.html template with dropdown options
    return render_template('index.html', Options=dropdown_options, Pos1=dropdown_options2, Pos2=dropdown_options3)

@app.route('/Awailable', methods=['POST'])  # Route to check available seats
def AwailableSeateCount():
    # Rendering the index.html template with available seats data
    return render_template('index.html', seates=a.SeatsAwailable())

@app.route('/Awailable/position', methods=['POST'])  # Route to check available seat positions
def AwailableSeatePos():
    # Rendering the index.html template with seat positions and dropdown options
    return render_template('index.html', position=a.SeatPositions(), Options=dropdown_options, Pos1=dropdown_options2, Pos2=dropdown_options3)

@app.route('/BookSeat', methods=['POST'])  # Route to book a seat
def Bookseat():
    text = request.form.get('BookSeat')  # Getting the seat booking input from the form
    # Rendering the index.html template with booking message and dropdown options
    return render_template('index.html', message1=a.BookSeat(text), Options=dropdown_options, Pos1=dropdown_options2, Pos2=dropdown_options3)

@app.route('/CancelSeat', methods=['POST'])  # Route to cancel a seat
def Cancelseat():
    text1 = request.form.get('CancelSeatRow')  # Getting the row input for seat cancellation
    text2 = request.form.get('CancelSeatCol')  # Getting the column input for seat cancellation
    m = [int(text1), int(text2)]  # Creating a list with row and column as integers
    # Rendering the index.html template with cancellation message and dropdown options
    return render_template('index.html', message2=a.CancelSeat(m), Options=dropdown_options, Pos1=dropdown_options2, Pos2=dropdown_options3)

if __name__ == '__main__':  # Entry point for running the Flask application
    app.run()  # Running the Flask application