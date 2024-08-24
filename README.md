### Pandas Revision Notes

#### 1. **Introduction**
Pandas is a powerful library for data manipulation and analysis. It's commonly used in data science and machine learning workflows due to its simplicity and integration with other tools.

#### 2. **Data Types in Pandas**

**a. Series**
- **1-dimensional array-like data structure.**
- **Creating Series:**
  ```python
  import pandas as pd

  # Using a list
  my_list = [1, 2, 3, "roht", True, 34.66]
  my_series = pd.Series(my_list)
  print(my_series)
  ```

  **Output:**
  ```
  0        1
  1        2
  2        3
  3     roht
  4     True
  5    34.66
  dtype: object
  ```

  ```python
  # Using a dictionary
  calories = {"day1": 420, "day2": 380, "day3": 390}
  myvar = pd.Series(calories)
  print(myvar)
  ```

  **Output:**
  ```
  day1    420
  day2    380
  day3    390
  dtype: int64
  ```

- **Accessing Elements:**
  ```python
  print(my_series[0])  # Access by index
  ```

  **Output:**
  ```
  1
  ```

  ```python
  # Access using a loop
  for item in my_series:
      print(item)
  ```

**b. DataFrame**
- **2-dimensional data structure (table format).**
- **Creating DataFrames:**

  ```python
  # Using a dictionary of Series
  cars = ["BMW", "Ferrari", "Audi"]
  colors = ["Black", "Red", "Dark Blue"]

  cars_series = pd.Series(cars)
  color_series = pd.Series(colors)

  cars_dict = {"Cars Model": cars_series, "Colors": color_series}
  cars_data = pd.DataFrame(cars_dict)
  print(cars_data)
  ```

  **Output:**
  ```
    Cars Model     Colors
  0        BMW      Black
  1    Ferrari        Red
  2       Audi  Dark Blue
  ```

  ```python
  # Directly from dictionary
  cars_data = pd.DataFrame({"Cars Model": cars_series, "Colors": color_series})
  print(cars_data)
  ```

**c. Accessing DataFrames:**
- **Access columns:**
  ```python
  print(cars_data["Cars Model"])
  ```

- **Access rows by index:**
  ```python
  print(cars_data.iloc[0])  # Access by row index
  ```

#### 3. **Reading and Writing Data**

**a. Reading from CSV:**
- **Code to read a CSV file:**
  ```python
  import pandas as pd

  data_file = pd.read_csv("data.csv")
  print(data_file.to_string())
  ```

- **Tips:**
  - Use `to_string()` to print the entire DataFrame.
  - `pd.options.display.max_rows` shows the number of rows to display.

**b. Writing to CSV:**
- **Export DataFrame to CSV:**
  ```python
  data_file.to_csv("exported-data.csv", index=False)  # Avoid overwriting by renaming the file
  ```

**c. Re-importing CSV:**
- **Code to read an exported CSV file:**
  ```python
  reimport = pd.read_csv("exported-data.csv")
  print(reimport)
  ```

  **Note:** If `index=False` was used while exporting, the index column will not be included in the CSV file.

**d. Reading from JSON:**
- **JSON files can be read as DataFrames:**
  ```python
  import pandas as pd

  data = {
    "Duration": {"0": 60, "1": 60, "2": 60, "3": 45, "4": 45, "5": 60},
    "Pulse": {"0": 110, "1": 117, "2": 103, "3": 109, "4": 117, "5": 102},
    "Maxpulse": {"0": 130, "1": 145, "2": 135, "3": 175, "4": 148, "5": 127},
    "Calories": {"0": 409.1, "1": 479.0, "2": 340.0, "3": 282.4, "4": 406.0, "5": 300.5}
  }

  df = pd.DataFrame(data)
  print(df)
  ```

#### 4. **Key Points**
- **Series**: Use for 1-dimensional data, can be created from lists, dictionaries, or scalars.
- **DataFrame**: Use for 2-dimensional data, can be created from dictionaries of Series or directly from data structures like lists or arrays.
- **File Operations**: Use `pd.read_csv()` to read CSV files and `to_csv()` to write them. Use `pd.read_json()` to read JSON data.

Reading Data from a CSV File
python
Copy code
file = pd.read_csv("data.csv")
print("reading completed!")
This code reads data from a CSV file named data.csv into a DataFrame called file and prints a confirmation message. The pd.read_csv() function is used to load the data.

Viewing the Data: Head and Tail
Head
python
Copy code
print(file.head(10))
The head() method returns the first 10 rows of the DataFrame file. By default, head() returns the first 5 rows. This method is useful for getting a quick overview of the data.

Tail
python
Copy code
print(file.tail(10))
Similarly, the tail() method returns the last 10 rows of the DataFrame file. By default, tail() returns the last 5 rows, providing insight into the end of the data.

Information About the DataFrame
python
Copy code
info = file.info()
print(info)
The info() method provides a summary of the DataFrame, including the number of entries, column names, non-null counts, and data types. It helps in understanding the structure and completeness of the data.

Handling Null Values
The info() method also shows that there are 5 missing values in the "Calories" column. Handling null values is crucial for accurate data analysis. Strategies include removing or imputing missing values.

Data Attributes and Metadata
Data Types
python
Copy code
print(file.dtypes)
The dtypes attribute provides the data type of each column in the DataFrame. This helps in understanding what kind of data is stored in each column (e.g., int64, float64, object).

Columns
python
Copy code
print(file.columns)
The columns attribute returns the names of all columns in the DataFrame. This is useful for understanding the structure of the DataFrame.

Adding and Deleting Columns
Adding a Column
python
Copy code
data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Height': [5.1, 6.2, 5.1, 5.2],
        'Qualification': ['Msc', 'MA', 'Msc', 'Msc']}
df = pd.DataFrame(data)
address = ['Delhi', 'Bangalore', 'Chennai', 'Patna']
df['Address'] = address
print(df)
Here, a new column named Address is added to the DataFrame df. This demonstrates how to insert additional columns into an existing DataFrame.

Deleting a Column
python
Copy code
df.drop(["Qualification"], axis=1, inplace=True)
print(df)
The drop() method is used to remove the Qualification column from the DataFrame df. The axis=1 argument specifies that a column is being dropped. The inplace=True argument modifies the DataFrame in place.

Adding and Deleting Rows
Adding a Row
python
Copy code
new_row = pd.DataFrame({'Name': 'Geeks', 'Team': 'Boston', 'Number': 3, 'Position': 'PG', 'Age': 33, 'Height': '6-2', 'Weight': 189, 'College': 'MIT', 'Salary': 99999}, index=[0])
df = pd.concat([new_row, df]).reset_index(drop=True)
print(df)
A new row is added to the DataFrame using pd.concat(). This method concatenates the new row with the existing DataFrame df, and reset_index(drop=True) reindexes the DataFrame.

Deleting a Row
python
Copy code
df.drop([0], inplace=True) # Example of dropping a row by index
print(df)
The drop() method with index [0] is used to remove a specific row from the DataFrame. The inplace=True argument ensures that the DataFrame is modified directly.

Index and Descriptive Statistics
Index
python
Copy code
print(file.index)
The index attribute returns the index of the DataFrame, showing the range and step of the row indices.

Descriptive Statistics
python
Copy code
file_describe = file.describe()
print(file_describe)
The describe() method provides statistical summaries for numerical columns, such as count, mean, standard deviation, min, max, and quartiles.

Mathematical Operations
Mean
python
Copy code
print(file.mean())
The mean() method calculates the mean (average) for each numerical column in the DataFrame.

Median
python
Copy code
print(file.median())
The median() method calculates the median value for each numerical column, which represents the middle value when the data is sorted.

Size
python
Copy code
print(file.size)
The size attribute returns the total number of elements in the DataFrame, which is the product of the number of rows and columns.

Label-Based Indexing and Slicing
Creating a DataFrame
python
Copy code
names = ["Abhi", "Bholu", "Anand", "Chandan"]
roll_no = [1, 34, 23, 60]
CGPA = [7.5, 8.9, 9.5, 7.0]
class_data = pd.DataFrame({"Names": names, "Roll no": roll_no, "CGPA": CGPA})
print(class_data)
This code creates a DataFrame class_data with columns for student names, roll numbers, and CGPA.

Label-Based Indexing
python
Copy code
a = pd.Series(class_data["CGPA"], index=[1, 2, 3, 3])
print(a.loc[3])
The loc method returns all values that correspond to the index value 3 in the Series a. It includes duplicate index values.

Positional Indexing
python
Copy code
print(a.iloc[3])
The iloc method returns the value at the positional index 3, which is the fourth element of the Series.

Conditional Printing
python
Copy code
print(class_data[class_data["CGPA"] > 8.0])
This code filters and prints rows from class_data where the CGPA is greater than 8.0.

CrossTabulation
python
Copy code
pd.crosstab(file["Pulse"], file["Duration"])
The crosstab() function creates a cross-tabulation (contingency table) between the Pulse and Duration columns, showing the frequency of each combination.

Plotting Data
python
Copy code
import matplotlib.pyplot as plt

file["Maxpulse"].plot()
plt.show()

file["Calories"].hist()
plt.show()
Here, plot() creates a line plot for the Maxpulse column, and hist() creates a histogram for the Calories column.

Handling Currency Data
python
Copy code
import regex

data = {'Amount': ['$1,234.56', '$2,345.67', '$3,456.78']}
df = pd.DataFrame(data)
df['Amount'] = df['Amount'].replace('[\$\,\.]', '', regex=True).astype(int)
print(df)
This code removes dollar signs, commas, and periods from the Amount column and converts the values to integers.
