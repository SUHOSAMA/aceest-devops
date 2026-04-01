from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample program data (based on your existing logic)
programs = {
    "Fat Loss": {
        "workout": "Cardio + HIIT + Strength",
        "calorie_factor": 22
    },
    "Muscle Gain": {
        "workout": "Strength + Hypertrophy",
        "calorie_factor": 35
    },
    "Beginner": {
        "workout": "Basic full body training",
        "calorie_factor": 26
    }
}

# Home route
@app.route("/")
def home():
    return jsonify({"message": "ACEest Fitness API is running"})

# Get all programs
@app.route("/programs", methods=["GET"])
def get_programs():
    return jsonify(programs)

# Calculate calories
@app.route("/calories", methods=["POST"])
def calculate_calories():
    data = request.get_json()

    weight = data.get("weight")
    program = data.get("program")

    if not weight or not program:
        return jsonify({"error": "Weight and program are required"}), 400

    if program not in programs:
        return jsonify({"error": "Invalid program"}), 400

    factor = programs[program]["calorie_factor"]
    calories = weight * factor

    return jsonify({
        "program": program,
        "weight": weight,
        "calories": calories
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)