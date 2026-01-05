from flask import Flask, request, jsonify
from flask_cors import CORS
from food_ai import check_food_quality
import random

app = Flask(__name__)
CORS(app)

# In-memory demo storage
food_requests = []

@app.route("/donate", methods=["POST"])
def donate_food():
    data = request.json

    quality = check_food_quality(data["food_type"], data["hours"])

    food_requests.append({
        "id": len(food_requests) + 1,
        "location": data["location"],
        "food_type": data["food_type"],
        "meals": data["meals"],
        "quality": quality
    })

    return jsonify({"status": "Donation added", "quality": quality})

@app.route("/volunteer", methods=["GET"])
def volunteer_view():
    return jsonify(food_requests)

@app.route("/stats", methods=["GET"])
def stats():
    total_meals = sum(item["meals"] for item in food_requests)
    return jsonify({
        "meals_saved": total_meals,
        "co2_saved": total_meals * 2.5
    })

if __name__ == "__main__":
    app.run(debug=True)
