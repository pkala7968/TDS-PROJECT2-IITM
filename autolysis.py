import os
import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set up AI Proxy token
api_token = os.getenv("AIPROXY_TOKEN")  # Ensure the environment variable is set
if not api_token:
    raise ValueError("AIPROXY_TOKEN environment variable is not set.")

# Define the AI Proxy API URL (replace this with the correct endpoint)
api_url = "https://aiproxy.sanand.workers.dev/openai/chat/completions"  # Updated to AI Proxy URL

# Function to send data to AI Proxy for analysis
def analyze_with_proxy(data_summary):
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "gpt-4o-mini",  # Specify the model as required by the AI Proxy
        "messages": [
            {
                "role": "system",
                "content": "You are an assistant that analyzes and provides insights from data summaries."
            },
            {
                "role": "user",
                "content": f"Please analyze the following data summary and provide insights:\n{data_summary}"
            }
        ]
    }

    response = requests.post(api_url, headers=headers, json=payload)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to communicate with AI Proxy: {response.text}")

# Load dataset
def load_data(filename):
    try:
        data = pd.read_csv(filename, encoding="latin-1")  # Fallback to latin-1 encoding if UTF-8 fails
        print(f"Dataset loaded successfully with {data.shape[0]} rows and {data.shape[1]} columns.")
        return data
    except Exception as e:
        print(f"Error loading dataset: {e}")
        raise

# Perform basic analysis on the dataset
def analyze_data(data):
    analysis = {}
    
    # General statistics
    analysis["summary_statistics"] = data.describe().to_dict()
    
    # Count missing values
    analysis["missing_values"] = data.isnull().sum().to_dict()
    
    # Correlation matrix (only for numeric columns)
    numeric_data = data.select_dtypes(include=['number'])
    if not numeric_data.empty:
        analysis["correlation_matrix"] = numeric_data.corr().to_dict()
    else:
        analysis["correlation_matrix"] = "No numeric data available for correlation."
    
    return analysis

# Generate charts based on analysis
def generate_charts(data):
    charts = []
    
    # Correlation heatmap (only for numeric columns)
    numeric_data = data.select_dtypes(include=['number'])
    if not numeric_data.empty:
        plt.figure(figsize=(10, 8))
        sns.heatmap(numeric_data.corr(), annot=True, cmap="coolwarm")
        heatmap_path = "correlation_heatmap.png"  # Save directly in the current directory
        plt.savefig(heatmap_path)
        plt.close()  # Close the plot to avoid it being displayed
        charts.append(heatmap_path)
        print("Correlation heatmap saved as correlation_heatmap.png.")
    else:
        print("No numeric columns available for correlation heatmap.")
    
    # Boxplot for outlier detection
    if not numeric_data.empty:
        plt.figure(figsize=(10, 6))
        sns.boxplot(data=numeric_data)
        boxplot_path = "outlier_detection.png"
        plt.savefig(boxplot_path)
        plt.close()
        charts.append(boxplot_path)
        print("Outlier detection chart saved as outlier_detection.png.")
    else:
        print("No numeric columns available for outlier detection.")

    # Histogram of key numeric columns (if available)
    for column in numeric_data.columns:
        plt.figure(figsize=(8, 6))
        sns.histplot(numeric_data[column], kde=True, bins=30)
        hist_path = f"histogram_{column}.png"
        plt.savefig(hist_path)
        plt.close()
        charts.append(hist_path)
        print(f"Histogram for {column} saved as {hist_path}.")
    
    return charts

# Create README.md file with analysis results
def generate_narrative(analysis, charts, data):
    readme_path = "README.md"
    
    with open(readme_path, "w") as file:
        file.write("# Data Analysis Report\n\n")
        
        # Data description
        file.write("## Dataset Overview\n")
        file.write(f"The dataset contains {data.shape[0]} rows and {data.shape[1]} columns. Here is a brief overview of the data:\n")
        file.write(str(data.head()) + "\n\n")
        
        # Write summary statistics
        file.write("## Summary Statistics\n")
        file.write(str(analysis["summary_statistics"]))
        file.write("\n\n")
        
        # Write missing values analysis
        file.write("## Missing Values\n")
        file.write(str(analysis["missing_values"]))
        file.write("\n\n")
        
        # Write correlation matrix
        file.write("## Correlation Matrix\n")
        file.write(str(analysis["correlation_matrix"]))
        file.write("\n\n")
        
        # Write data visualizations
        file.write("## Data Visualizations\n")
        for chart in charts:
            file.write(f"![{chart}]({chart})\n")
        
        # Request narrative from AI Proxy
        data_summary = {
            "summary_statistics": analysis["summary_statistics"],
            "missing_values": analysis["missing_values"],
            "correlation_matrix": analysis["correlation_matrix"]
        }
        
        try:
            narrative = analyze_with_proxy(data_summary)
            file.write("\n\n## Insights and Recommendations\n")
            file.write(narrative.get("choices", [{"message": {"content": "No insights returned."}}])[0]["message"]["content"])
        except Exception as e:
            file.write(f"Error getting insights: {str(e)}")
    
    print(f"README.md file generated successfully at {readme_path}.")

def main():
    # Assume dataset filename is passed as the first argument
    import sys
    if len(sys.argv) != 2:
        print("Usage: python autolysis.py <dataset.csv>")
        sys.exit(1)
    
    filename = sys.argv[1]
    
    # Load data
    data = load_data(filename)
    
    # Analyze data
    analysis = analyze_data(data)
    
    # Generate charts
    charts = generate_charts(data)
    
    # Generate narrative and save the results
    generate_narrative(analysis, charts, data)

if __name__ == "__main__":
    main()
