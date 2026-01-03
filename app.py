from flask import Flask, request, jsonify # pyright: ignore[reportMissingImports]
import random
import re

from flask_cors import CORS # type: ignore

app = Flask(__name__)
CORS(app)


COMMON_NAMES = open("name_list.txt").read().lower().splitlines()

def detect_language(pw):
    if re.search(r"[அ-ஹ]", pw): return "Tamil"
    if re.search(r"[अ-ह]", pw): return "Hindi"
    if re.search(r"[క-హ]", pw): return "Telugu"
    return "English"

def policy_check(pw):
    lower = pw.lower()
    has_name = any(n in lower for n in COMMON_NAMES)

    return {
        "min_12_chars": len(pw) >= 12,
        "uppercase": any(c.isupper() for c in pw),
        "lowercase": any(c.islower() for c in pw),
        "digit": any(c.isdigit() for c in pw),
        "special": bool(re.search(r"[!@#$%^&*]", pw)),
        "no_name": not has_name
    }

def ml_strength_stub(pw):
    if len(pw) < 8: return "weak"
    if len(pw) < 12: return "medium"
    return "strong"

def suggest_passwords():
    base = ["Nova","Secure","Cyber","Shield","Alpha","Zen"]
    return [
        f"{random.choice(base)}-{random.randint(10,99)}@{random.randint(2024,2029)}!"
        for _ in range(3)
    ]

@app.route("/analyze", methods=["POST"])
def analyze():
    pw = request.json.get("password","")

    policy = policy_check(pw)

    return jsonify({
        "ml_strength": ml_strength_stub(pw),
        "language": detect_language(pw),
        "policy": policy,
        "suggestions": suggest_passwords()
    })

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=5000)

