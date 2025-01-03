# -*- coding: utf-8 -*-
"""Linear.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1k4ScF-xvFUWXpFucA3NJ5g_Iz2lr8IXG

Linear approach
"""

import pandas as pd
import time

student_fees = pd.read_csv('student_fees.csv')
students = pd.read_csv('students.csv')

start_time_linear = time.time()

merged_data = pd.merge(student_fees, students, on="Student ID")

most_frequent_dates = merged_data.groupby('Student ID')['Payment Date'].apply(
    lambda dates: dates.mode().iloc[0] if not dates.mode().empty else None
).reset_index()

end_time_linear = time.time()
execution_time_linear = end_time_linear - start_time_linear

most_frequent_dates.to_csv('linear_results.csv', index=False)
print(f"Execution Time (Linear): {execution_time_linear} seconds")

