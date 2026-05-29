from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

CHARACTERS = {
    "motivation": {"name": "Sakura", "emoji": "🌸", "color": "#ff85a1"},
    "wisdom":     {"name": "Haru",   "emoji": "🌿", "color": "#52b788"},
    "peace":      {"name": "Yuki",   "emoji": "❄️", "color": "#74b9ff"},
    "courage":    {"name": "Rei",    "emoji": "⚡", "color": "#a29bfe"},
    "friendship": {"name": "Miku",   "emoji": "🎵", "color": "#00b4d8"},
    "love":       {"name": "Nana",   "emoji": "🌹", "color": "#e63946"},
}

QUOTES = {
    "motivation": [
        "Every step forward is a step toward something amazing.",
        "You are stronger than you think, braver than you believe.",
        "Don't give up! The beginning is always the hardest.",
        "Even the smallest star shines in the darkness.",
        "Your potential is limitless — believe it, and you'll prove it.",
        "One day at a time. One step at a time. You've got this.",
        "The only failure is giving up before you've truly tried.",
    ],
    "wisdom": [
        "To know oneself is to understand the universe.",
        "Patience is not waiting — it's how you act while you wait.",
        "The heart knows what the mind cannot understand.",
        "True strength is handling life's hardships with grace.",
        "Knowledge is knowing what to say. Wisdom is knowing when.",
        "Look at the stars — even they had to burn through darkness first.",
        "Sometimes the greatest lessons come wrapped in hardship.",
    ],
    "peace": [
        "The past cannot be changed, but the future is still yours.",
        "In the silence of the world, you'll find your own answers.",
        "Let go of what was. Embrace what is. Trust what will be.",
        "A calm mind is the greatest weapon against life's storms.",
        "Not knowing is not hopeless — it's the start of discovery.",
        "Breathe. You are exactly where you need to be.",
        "Peace is not the absence of chaos — it's your response to it.",
    ],
    "courage": [
        "It's okay not to be okay. Just don't give up.",
        "Fear tells you where your weakness is — face it head-on.",
        "The moment you give up is the moment someone else wins.",
        "Courage is not the absence of fear — it's acting despite it.",
        "Even if I can't be a hero, I'll be the one who tries.",
        "The world belongs to those who refuse to back down.",
        "Stand tall. The storm is just testing how strong you are.",
    ],
    "friendship": [
        "A true friend sees your pain even through your smile.",
        "Friends are the family we choose for ourselves.",
        "Bonds forged in hardship are the ones that never break.",
        "You don't have to face the world alone — that's what we're here for.",
        "A single kind word can change someone's entire day.",
        "Side by side or miles apart, real friends are always close at heart.",
        "The best adventures are the ones shared with someone you trust.",
    ],
    "love": [
        "Love isn't something you find. It's something that finds you.",
        "Even in the darkest night, love is the light that guides us home.",
        "The spaces between your fingers exist so someone else's can fill them.",
        "When you truly love someone, the world becomes a better place.",
        "Love is not about words — it's about what you're willing to do.",
        "To love someone is to see all their stars, even in the dark.",
        "Home is not a place — it's the person who makes you feel safe.",
    ],
}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/quote")
def get_quote():
    category = request.args.get("category", "all")
    if category == "all" or category not in QUOTES:
        category = random.choice(list(QUOTES.keys()))
    quote = random.choice(QUOTES[category])
    return jsonify({
        "quote": quote,
        "category": category,
        "character": CHARACTERS[category],
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
