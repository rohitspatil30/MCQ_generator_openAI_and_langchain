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

---

### **Reading and Viewing Data**

- **Reading Data:**
  ```python
  file = pd.read_csv("data.csv")
  ```

- **Viewing the First and Last Rows:**
  ```python
  print(file.head(10))  # First 10 rows
  print(file.tail(10))  # Last 10 rows
  ```

- **Basic Information:**
  ```python
  print(file.info())  # DataFrame information
  ```

### **DataFrame Attributes and Methods**

- **Data Types:**
  ```python
  print(file.dtypes)
  ```

- **Columns:**
  ```python
  print(file.columns)
  ```

### **DataFrame Operations**

- **Adding a Column:**
  ```python
  df['Address'] = ['Delhi', 'Bangalore', 'Chennai', 'Patna']
  ```

- **Deleting a Column:**
  ```python
  df.drop(["Qualification"], axis=1, inplace=True)
  ```

- **Adding Rows:**
  ```python
  new_row = pd.DataFrame({'Name': 'Geeks', 'Team': 'Boston', 'Number': 3, 'Position': 'PG', 'Age': 33, 'Height': '6-2', 'Weight': 189, 'College': 'MIT', 'Salary': 99999}, index=[0])
  df = pd.concat([new_row, df]).reset_index(drop=True)
  ```

- **Removing Rows:**
  ```python
  df.drop([0, 1], inplace=True)  # Example: Dropping specific indices
  ```

### **Indexing and Selection**

- **Index:**
  ```python
  print(file.index)
  ```

- **Describe:**
  ```python
  print(file.describe())
  ```

- **Math Functions:**
  ```python
  print(file.mean())
  print(file.median())
  ```

- **Conditional Selection:**
  ```python
  print(class_data[class_data["CGPA"] > 8.0])
  ```

### **Advanced Data Analysis**

- **CrossTab:**
  ```python
  pd.crosstab(file["Pulse"], file["Duration"])
  ```

- **Group By:**
  ```python
  print(file.groupby(["Pulse"]).mean())
  ```

### **Data Visualization**

- **Plotting:**
  ```python
  import matplotlib.pyplot as plt
  file["Maxpulse"].plot()
  file["Calories"].hist()
  ```

### **Data Cleaning**

- **Cleaning Strings and Conversion:**
  ```python
  df['Amount'] = df['Amount'].replace('[\$\,\.]', '', regex=True).astype(int)
  ```

### **Additional Tips**

- **Explore `pd.DataFrame` Methods:**
  Use methods like `df.sort_values()`, `df.fillna()`, `df.dropna()` for more data manipulation.
  
- **Visualizations:**
  Customize plots using `plt.title()`, `plt.xlabel()`, `plt.ylabel()`, and other matplotlib features.

- **Documentation:**
  Refer to the [pandas documentation](https://pandas.pydata.org/pandas-docs/stable/) for more in-depth explanations and additional functions.

--- 

### Reassigning Columns
When reassigning columns or filling missing values:
```python
file["Assignments"] = file["Assignments"].fillna(file["Assignments"].mean())
```

### Adding Columns
Adding columns can be done in several ways:
- **From a Series:**
  ```python
  se = pd.Series(range(1, len(file) + 1))
  file["NewColumn"] = se
  ```
- **From a List:**
  ```python
  file["NewListColumn"] = [num for num in range(1, len(file) + 1)]
  ```
- **Using a Condition:**
  ```python
  file["ConditionalColumn"] = [i if i % 2 == 0 else np.nan for i in range(len(file))]
  ```

### Deleting Columns
To remove a column:
```python
file.drop("ColumnName", axis=1, inplace=True)
```

### Shuffling Data
To shuffle rows:
```python
shuffled_file = file.sample(frac=1).reset_index(drop=True)
```

