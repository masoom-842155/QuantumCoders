from flask import Flask, render_template, request, jsonify
import random
import string

app = Flask(__name__)

# Function to generate a random password with customizable options
def generate_password(length, use_lowercase, use_uppercase, use_numbers, use_symbols, exclude_similar, exclude_ambiguous):
    similar_chars = "il1Lo0O"
    ambiguous_chars = "{}[]()/\'\"`~,;:.<>"
    
    characters = ""
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    if exclude_similar:
        characters = ''.join([c for c in characters if c not in similar_chars])
    if exclude_ambiguous:
        characters = ''.join([c for c in characters if c not in ambiguous_chars])

    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    password = generate_password(
        length=int(data.get('length', 12)),
        use_lowercase=data.get('use_lowercase', True),
        use_uppercase=data.get('use_uppercase', True),
        use_numbers=data.get('use_numbers', True),
        use_symbols=data.get('use_symbols', True),
        exclude_similar=data.get('exclude_similar', False),
        exclude_ambiguous=data.get('exclude_ambiguous', False)
    )
    return jsonify(password=password)

if __name__ == '__main__':
    app.run(debug=True)