from flask import Flask, render_template, request

app = Flask(__name__)

# Function to calculate the product of numbers in a list
def calculate_product(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form.get("numbers")
        try:
            numbers = [float(num) for num in user_input.split(',')]
            if len(numbers) == 0:
                result = "No numbers entered."
            else:
                result = calculate_product(numbers)
        except ValueError:
            result = "Invalid input. Please enter numbers separated by commas."
        return render_template("index.html", result=result)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
