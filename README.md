# TDS-PROJECT2-IITM
## Automated Data Analysis and Reporting Tool
This project provides an automated data analysis and reporting tool, designed to simplify the process of exploring datasets, visualizing key insights, and generating a comprehensive narrative about the analysis. The tool is powered by Python and integrates with AI-powered models to generate insightful reports in the form of a README.md file.

### Features
Automatic Data Analysis: The tool performs an initial analysis of the dataset, including summary statistics, missing values detection, and correlation analysis.
Data Visualizations: It generates a series of useful visualizations such as histograms, correlation heatmaps, and boxplots to better understand the data.
Outlier Detection: Identifies and visualizes outliers that may represent errors or high-impact opportunities.
Narrative Generation: Uses AI-powered models (GPT-4o-Mini) to generate a story-like summary of the analysis, providing insights into the dataset and offering recommendations.
Customizable Output: The generated outputs, including charts and the final README.md file, are saved directly to the current working directory.

### Project Workflow
Input: You provide a CSV file as input to the script.
Data Analysis: The script automatically loads the dataset, performs several analytical steps such as:
Generating summary statistics for each column.
Detecting missing values.
Calculating correlations between numerical features.
Data Visualization: Several plots are generated to visualize key patterns and relationships:
Histograms for individual columns.
Correlation heatmaps.
Boxplots for outlier detection.
Narrative Generation: The tool sends a summary of the dataset and analysis to an AI model (GPT-4o-Mini via AI Proxy) to generate a comprehensive narrative that describes the dataset, the analysis performed, insights discovered, and recommended actions.
Output: The final README.md file is generated, containing:
A brief summary of the dataset.
Descriptions of the analysis and visualizations.
The insights and recommendations provided by the AI model.
Generated charts saved as PNG files.
