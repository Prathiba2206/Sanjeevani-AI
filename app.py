from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


# Function to generate chatbot response based on simple rule logic
def chatbot_reply(message):
    lowered = message.lower()

    # Initial greetings and check-ins
    if "start" in lowered or "hello" in lowered or "hi" in lowered:
        return "Hey, I'm SafeBot. Is everything ok? Any problems you want to share?"

    # Risk keywords detection
    risk_keywords = ["suicide", "kill myself", "depressed", "hopeless", "worthless", "alone", "no hope"]
    if any(keyword in lowered for keyword in risk_keywords):
        return ("I’m really sorry you’re feeling this way. "
                "Remember, you don’t have to face this alone. "
                "Would you like me to help you find someone to talk to?")

    # Positive or neutral replies
    if "yes" in lowered or "good" in lowered or "fine" in lowered or "okay" in lowered:
        return ("Glad to hear that! "
                "If you ever feel like talking or need support, I’m here to listen.")

    # Expressions of sadness or stress
    sadness_keywords = ["sad", "stress", "anxious", "tired", "overwhelmed", "lonely"]
    if any(keyword in lowered for keyword in sadness_keywords):
        return ("I'm sorry you're feeling that way. "
                "It's okay to feel down sometimes. "
                "Would you like to tell me more about what's bothering you?")

    # User shares details or seeks encouragement
    if "not good" in lowered or "hard" in lowered or "struggling" in lowered:
        return ("Thanks for sharing that. Remember, challenges can be tough, but "
                "you are stronger than you think. "
                "Would you like some tips on coping or someone to talk to?")

    # Encouraging open communication
    if "talk" in lowered or "help" in lowered or "listen" in lowered:
        return ("I’m here to listen. Tell me whatever you feel comfortable sharing.")

    # Goodbye or end chat signals
    if "bye" in lowered or "thank" in lowered or "exit" in lowered:
        return "Take care of yourself! Remember, SafeBot is always here if you want to talk again."

    # Default fallback for other messages
    return ("Thanks for sharing. Is there anything else on your mind? "
            "You can tell me anything; I’m here to help.")

    

# Route to serve chatbot page (will be created later)
@app.route('/chat')
def chat():
    user_id = request.args.get('user')  # Get user ID from URL param
    return render_template('chat.html', user_id=user_id)

# API route to receive user messages and respond
@app.route('/get_response', methods=['POST'])
def get_response():
    data = request.json
    user_message = data.get('message', '')
    user_id = data.get('user_id', '')
    reply = chatbot_reply(user_message)
    return jsonify({'reply': reply})

if __name__ == "__main__":
    app.run(debug=True)
