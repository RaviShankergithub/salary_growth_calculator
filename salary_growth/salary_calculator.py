# salary_growth/salary_calculator.py

class SalaryCalculator:
    def __init__(self, past_salary, current_salary, cagr_years, future_years):
        self.past_salary = past_salary
        self.current_salary = current_salary
        self.cagr_years = cagr_years
        self.future_years = future_years

    def calculate_cagr(self):
        """
        Calculate the Compound Annual Growth Rate (CAGR).
        Returns:
        float: CAGR in percentage
        """
        # Calculate CAGR
        CAGR = (self.current_salary / self.past_salary) ** (1 / self.cagr_years) - 1

        # Convert to percentage
        CAGR_percentage = CAGR * 100
        return CAGR_percentage

    def predict_future_salary(self, cagr_percentage):
        """
        Predict future salary based on the CAGR percentage.
        Parameters:
        cagr_percentage (float): CAGR in percentage
        Returns:
        float: Predicted future salary
        """
        # Convert percentage to a decimal
        CAGR_decimal = cagr_percentage / 100

        # Calculate future salary
        future_salary = self.current_salary * (1 + CAGR_decimal) ** self.future_years
        return future_salary
