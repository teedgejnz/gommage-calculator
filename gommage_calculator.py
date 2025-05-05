from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def gommage_calculator():
    print("Received a request!")  # Debugging print statement
    result = None  

    if request.method == "POST":
        try:
            current_gommage = int(request.form["current_gommage"])
            your_age = int(request.form["your_age"])

            print(f"User input - Monolith: {current_gommage}, Age: {your_age}")  # Debugging

            while current_gommage > your_age:
                current_gommage -= 1
                your_age += 1

            result = f"Your Gommage will occur when you are {your_age}."
            print(f"Calculated result: {result}")  # Debugging
        except ValueError:
            result = "Please enter valid numbers."
            print("Error: Invalid number input")  # Debugging

    return render_template("index.html", result=result)

if __name__ == "__main__":
    print("Starting Flask server...")  # Debugging
    app.run(debug=True, port=5001)