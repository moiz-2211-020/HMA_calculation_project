Overview
The HMA indicator provides a smoother moving average that reduces lag and enhances trend analysis for better responsiveness. This project reads data from a CSV file, performs
calculations for each row, and outputs the calculated values.

Features:
Calculates the Hull Moving Average (HMA)
Includes columns for:
Change: Measures the difference between current and previous values
Gain and Loss: Derived from Change values
Avg Gain and Avg Loss: Rolling averages of Gain and Loss values
HM (Hull Moving Average Ratio) and 14-day HMA


Outputs results in a formatted CSV


Requirements
Python 3.x
pandas for data manipulation
numpy for numerical calculations

Installation
Clone this repository:
bash
Copy code
git clone <repository-url>
cd <repository-folder>

Install dependencies:
bash
Copy code
pip install -r requirements.txt

Usage
Place your input data in a CSV file named hma_input.csv.
Run the script:
bash
Copy code
python Calculation_of_Hull_Moving_Average(HMA).py
The output will be saved as hma_output.csv with all calculated columns.
File Structure
Calculation_of_Hull_Moving_Average(HMA).py - Main script containing calculation logic
hma.xlsx - Input file containing initial data
hma_output.csv - Output file with calculated columns


API Endpoints
This project includes API endpoints to facilitate data upload and URL testing functionalities. These endpoints are built using FastAPI, providing a seamless interface for handling data uploads and verifying URL structures.

1. Upload Endpoint
Endpoint: /upload
Method: POST
Description: Accepts excel files to populate data for HMA calculations.

Running the API Server
Start the FastAPI server:
bash
uvicorn main:app --reload


Notes on Rounding
For some columns, rounding to two decimal places (using Python’s round function) is applied to ensure consistent results.

Known Issues
HM Calculation Rounding: When rounding Avg Gain and Avg Loss to two decimals, slight discrepancies in HM values may occur.
Output Structure: The Unnamed columns in the output file can sometimes reflect an index misalignment; removing them is recommended if not needed.
