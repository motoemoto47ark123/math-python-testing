from flask import Flask, request, render_template_string

# Initialize Flask application
app = Flask(__name__)

# HTML form for user input
HTML_FORM = """
<!DOCTYPE html>
<html>
<head>
    <title>Update LaTeX Formula</title>
    <style>
        body {
            background-color: #000;
            color: #FF0000;
            font-family: Arial, sans-serif;
        }
        input[type=text], textarea {
            background-color: #333;
            color: #FF0000;
            border: 1px solid #FF0000;
            border-radius: 5px;
            padding: 10px;
            margin: 10px 0;
            width: 95%;
        }
        input[type=submit] {
            background-color: #FF0000;
            color: #000;
            padding: 15px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: transform 0.3s ease;
        }
        input[type=submit]:hover {
            transform: scale(1.1);
        }
        label {
            margin-top: 20px;
        }
        form {
            max-width: 600px;
            margin: auto;
        }
        .error {
            color: #FFA500;
            margin: 20px 0;
        }
    </style>
</head>
<body>
    <h2>Enter LaTeX Formula and Coordinates</h2>
    <form method="post">
        <label for="old_formula">Enter the existing LaTeX formula:</label><br>
        <input type="text" id="old_formula" name="old_formula"><br>
        <label for="x1">Enter x1:</label><br>
        <input type="text" id="x1" name="x1"><br>
        <label for="y1">Enter y1:</label><br>
        <input type="text" id="y1" name="y1"><br>
        <label for="x2">Enter x2:</label><br>
        <input type="text" id="x2" name="x2"><br>
        <label for="y2">Enter y2:</label><br>
        <input type="text" id="y2" name="y2"><br><br>
        <input type="submit" value="Get Updated Formula">
    </form>
    {% if updated_formula %}
        <h3>Updated LaTeX Formula:</h3>
        <textarea rows="4" cols="50">{{ updated_formula }}</textarea>
    {% elif error %}
        <div class="error">{{ error }}</div>
    {% endif %}
</body>
</html>
"""

# Function to update LaTeX formula based on user input
def update_formula(old_formula, x1, y1, x2, y2):
    # Validate input fields are not empty
    if not old_formula or not x1 or not y1 or not x2 or not y2:
        return None, "Please fill in all fields."
    # Convert coordinates to integers
    try:
        x1, y1, x2, y2 = map(int, [x1, y1, x2, y2])
    except ValueError:
        return None, "Coordinates must be integers."
    
    # Update formula based on specific keywords
    if "sqrt" in old_formula:
        new_formula = f"\\sqrt{{({x2}-{x1})^{{2}}+({y2}-{y1})^{{2}}}}"
    elif "frac" in old_formula:
        new_formula = f"\\left( \\frac{{{x1} + {x2}}}{{2}}, \\frac{{{y1} + {y2}}}{{2}} \\right)"
    else:
        return None, "Invalid formula."
    return new_formula, None

# Define route for handling requests
@app.route("/", methods=["GET", "POST"])
def main():
    updated_formula = None
    error = None
    # Process form data on POST request
    if request.method == "POST":
        old_formula = request.form.get("old_formula", "").strip()
        x1 = request.form.get("x1", "").strip()
        y1 = request.form.get("y1", "").strip()
        x2 = request.form.get("x2", "").strip()
        y2 = request.form.get("y2", "").strip()
        updated_formula, error = update_formula(old_formula, x1, y1, x2, y2)
    # Render HTML form with updated formula or error message
    return render_template_string(HTML_FORM, updated_formula=updated_formula, error=error)

# Run Flask application if script is executed directly
if __name__ == "__main__":
    app.run(debug=True)
