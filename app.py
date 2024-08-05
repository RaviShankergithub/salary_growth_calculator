from flask import Flask, render_template, request
from salary_growth.salary_calculator import SalaryCalculator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    past_salary = float(request.form['past_salary'])
    current_salary = float(request.form['current_salary'])
    cagr_years = int(request.form['cagr_years'])
    future_years = int(request.form['future_years'])

    # Create an instance of SalaryCalculator
    salary_calculator = SalaryCalculator(past_salary, current_salary, cagr_years, future_years)

    # Calculate CAGR percentage
    cagr_percentage = salary_calculator.calculate_cagr()

    # Predict future salary
    future_salary = salary_calculator.predict_future_salary(cagr_percentage)

    return render_template('result.html', cagr_percentage=cagr_percentage, future_salary=future_salary)

if __name__ == '__main__':
    app.run(debug=True)
