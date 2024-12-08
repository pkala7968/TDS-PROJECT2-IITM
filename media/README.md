# Data Analysis Report

## Dataset Overview
The dataset contains 2652 rows and 8 columns. Here is a brief overview of the data:
        date language   type        title                             by  overall  quality  repeatability
0  15-Nov-24    Tamil  movie  Meiyazhagan           Arvind Swamy, Karthi        4        5              1
1  10-Nov-24    Tamil  movie    Vettaiyan        Rajnikanth, Fahad Fazil        2        2              1
2  09-Nov-24    Tamil  movie       Amaran  Siva Karthikeyan, Sai Pallavi        4        4              1
3  11-Oct-24   Telugu  movie        Kushi    Vijay Devarakonda, Samantha        3        3              1
4  05-Oct-24    Tamil  movie         GOAT                          Vijay        3        3              1

## Summary Statistics
{'overall': {'count': 2652.0, 'mean': 3.0475113122171944, 'std': 0.7621797580962717, 'min': 1.0, '25%': 3.0, '50%': 3.0, '75%': 3.0, 'max': 5.0}, 'quality': {'count': 2652.0, 'mean': 3.2092760180995477, 'std': 0.7967426636666686, 'min': 1.0, '25%': 3.0, '50%': 3.0, '75%': 4.0, 'max': 5.0}, 'repeatability': {'count': 2652.0, 'mean': 1.4947209653092006, 'std': 0.598289430580212, 'min': 1.0, '25%': 1.0, '50%': 1.0, '75%': 2.0, 'max': 3.0}}

## Missing Values
{'date': 99, 'language': 0, 'type': 0, 'title': 0, 'by': 262, 'overall': 0, 'quality': 0, 'repeatability': 0}

## Correlation Matrix
{'overall': {'overall': 1.0, 'quality': 0.8259352331454309, 'repeatability': 0.5126000083900123}, 'quality': {'overall': 0.8259352331454309, 'quality': 1.0, 'repeatability': 0.31212651153886395}, 'repeatability': {'overall': 0.5126000083900123, 'quality': 0.31212651153886395, 'repeatability': 1.0}}

## Data Visualizations
![correlation_heatmap.png](correlation_heatmap.png)
![outlier_detection.png](outlier_detection.png)
![histogram_overall.png](histogram_overall.png)
![histogram_quality.png](histogram_quality.png)
![histogram_repeatability.png](histogram_repeatability.png)
Error getting insights: Failed to communicate with AI Proxy: {
  "message": "Bearer \"eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjIzZjEwMDIzNzRAZHMuc3R1ZHkuaWl0bS5hYy5pbiJ9.fr2uSx0R42TVL_uChcXUvu3ewJG-Zv2pStwyI_ynD0g\" is invalid: JWSInvalid: JWS Protected Header is invalid"
}