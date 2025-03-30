from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operation = request.form["operation"]

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                result = num1 / num2 if num2 != 0 else "Error: Division by zero"

        except ValueError:
            result = "Error: Invalid input. Please enter numbers only."

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
