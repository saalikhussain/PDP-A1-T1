# -*- coding: utf-8 -*-
"""paralle.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1x3UpFuINfCDwP99vHFSokTDT_UaRzsi_
"""

import pandas as pd
import time
from multiprocessing import Pool, cpu_count

student_fees = pd.read_csv('student_fees.csv')
students = pd.read_csv('students.csv')

merged_data = pd.merge(student_fees, students, on="Student ID")

def calculate_mode(group):
    return group.mode().iloc[0] if not group.mode().empty else None

start_time_parallel = time.time()

grouped_data = merged_data.groupby('Student ID')['Payment Date']

with Pool(cpu_count()) as pool:
    modes = pool.map(calculate_mode, [group for _, group in grouped_data])

most_frequent_dates_parallel = pd.DataFrame({
    'Student ID': grouped_data.groups.keys(),
    'Most Frequent Payment Date': modes
})

end_time_parallel = time.time()
execution_time_parallel = end_time_parallel - start_time_parallel

most_frequent_dates_parallel.to_csv('parallel_results.csv', index=False)
print(f"Execution Time (Parallel): {execution_time_parallel} seconds")
