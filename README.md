# PDP-A1-T1
Most Frequent Payment Date Analysis

This repository contains Python scripts to analyze student payment data and identify the most frequent payment dates for each student. The implementation is provided in two ways:

Linear Processing: A straightforward approach that processes data sequentially.

Parallel Processing: A more efficient approach that leverages multi-core processing for concurrent execution.
Features

Merges student data with payment records.
Computes the most frequent payment dates for each student.
Compares execution times between linear and parallel implementations.
Files

linear_processing.py: Script for linear data processing.

parallel_processing.py: Script for parallel data processing using multiprocessing.

student_fees.csv: Sample dataset containing student payment records.

students.csv: Sample dataset containing student information.
How to Use

Clone the repository.

Replace the sample dataset files (student_fees.csv and students.csv) with your data.

Run the scripts in a Python environment:

For linear processing: python linear_processing.py

For parallel processing: python parallel_processing.py

View the results in the generated linear_results.csv and parallel_results.csv.
Performance

The execution times for the provided datasets are as follows:

Linear Processing: 19.83 seconds

Parallel Processing: 20.72 seconds

While parallel processing is typically faster for larger datasets, the slight overhead in managing parallel threads may make it slower for smaller datasets, as seen here.

Requirements

Python 3.7+

Pandas

Multiprocessing
