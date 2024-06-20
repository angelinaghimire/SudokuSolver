from flask import Flask, render_template, session, redirect, url_for
from sudoku import generate
from solver import solve
import numpy as np
import time

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session management

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze')
def analyze():
    return render_template('analyze.html')
    

@app.route('/generate-sudoku', methods=['GET', 'POST'])
def generate_sudoku():
    size = 9  # Default size
    sudoku_matrix = generate(size)
    while not solve(np.copy(sudoku_matrix)):  # Check if the generated Sudoku is solvable
        sudoku_matrix = generate(size)  # Generate a new one if not solvable
    session['sudoku_matrix'] = sudoku_matrix.tolist()  # Store in session as list
    return render_template('sudoku.html', sudoku_matrix=sudoku_matrix)

@app.route('/solve-sudoku', methods=['GET', 'POST'])
def solve_sudoku_route():
    sudoku_matrix = session.get('sudoku_matrix')
    if sudoku_matrix is None:
        return redirect(url_for('generate_sudoku'))  # Redirect to generate if no sudoku found

    sudoku_matrix = np.array(sudoku_matrix)  # Convert back to numpy array
    solved_matrix = np.copy(sudoku_matrix)  # Create a copy to solve

    start_time = time.time()
    if solve(solved_matrix):
        end_time = time.time()
        time_taken = end_time - start_time
        return render_template('solver.html', sudoku_matrix=solved_matrix, time_taken=time_taken)
    else:
        return "No solution exists for this Sudoku puzzle."

if __name__ == '__main__':
    app.run(debug=True)
