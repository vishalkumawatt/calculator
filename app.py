from flask import Flask, request, jsonify, render_template
import math

app = Flask(__name__)

# Dictionary of safe math functions for eval
safe_dict = {
    'abs': abs,
    'round': round,
    'pow': pow,
    'sqrt': math.sqrt,
    'sin': math.sin,
    'cos': math.cos,
    'tan': math.tan,
    'asin': math.asin,
    'acos': math.acos,
    'atan': math.atan,
    'log': math.log,         # Natural log
    'log10': math.log10,     # Base-10 log
    'pi': math.pi,
    'e': math.e,
    '__builtins__': {}       # Restrict built-in access
}

@app.route('/')
def index():
    return render_template('calculator.html')  # Make sure file is named correctly

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    expression = data.get('expression', '')
    try:
        result = eval(expression, {"__builtins__": None}, safe_dict)
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': f"Error: {str(e)}"}), 400

if __name__ == '__main__':
    app.run(debug=True)
