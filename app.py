from flask import Flask, render_template, request

app = Flask(__name__)

def flames_game(name1, name2):
    # Function to perform the FLAMES game logic
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")
    letters = "flames"
    
    # Create a list of letters in the remaining order
    remaining_letters = list(letters)
    
    # Create a copy of remaining_letters to avoid modifying the original list
    remaining_letters_copy = remaining_letters[:]
    
    # Iterate through the letters in the names
    for letter in name1:
        try:
            # Attempt to remove common letters from the copy
            remaining_letters_copy.remove(letter)
        except ValueError:
            # If the letter is not in the list, ignore the error
            pass
    
    # Count the remaining letters
    result_index = len(name2) % len(remaining_letters_copy)
    result_letter = remaining_letters_copy[result_index]
    
    # Map the result letter to the full relationship description
    relationships = {
        "f": "Friends",
        "l": "Lovers",
        "a": "Affectionate",
        "m": "Marriage",
        "e": "Enemies",
        "s": "Siblings"
    }
    
    result = relationships.get(result_letter, "Unknown")
    
    return result


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        name1 = request.form.get("name1", "")
        name2 = request.form.get("name2", "")
        result = flames_game(name1, name2)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
