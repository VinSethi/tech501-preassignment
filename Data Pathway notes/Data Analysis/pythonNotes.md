# Python Notes

## Object and Variables
* A variable is used to store data within a variable to recall later
* Objects are Pythons abstracts of data- For example '1' is the object and the object type would be an 'int'

## Numbers
* Int: Int is a whole number
* Floating number: It is a number that has a decimal point
* Arithmetic Operations and Functions: You can set a variable to a number and then call them and add them e.g. x+y+z setting each one to a number would give you a result
* Modulo: Using the percent sign between two numbers will give you an answer of the remainder between the two. E.g. 10%3 = 1 as 3 goes into 10 3 times with a remainder of 1

## String indexing and Slicing:
* String indexing: Lets say `x= This` and you wanted the letter 's' you would do x[3], indexing also works in negatives starting with '-1'
* String slicing: Lets say `x= This is a string` and you wanted the word 'is' you would do x[5:7:1]. So it works as str(start:stop:step)

## String methods and properties
* Lets say `y= 'Red Flag'` and then you did `y.find('Red')` it will give a response of '0' meaning its been found, however if it was something like y.find(red) it will give '-1' meaning not found.
* `Lets say y= 'Red Flag'` and you wanted to replace 'Red' with 'Green' you would do `y.replace('Red', 'Green')`, if you wanted to change it in the whole variable you would have to do the replace in the variable.
* Let's say `x= 'This is a string'`, doing x.split() would split it and the result would be `'This', 'is' , 'a', 'string' `

## Lists
* append(x): Adds an item x to the end of the list.
* extend(iterable): Extends the list by appending elements from the iterable.
* insert(i, x): Inserts an item x at a given position i.
* remove(x): Removes the first occurrence of an item x.
* pop([i]): Removes and returns the item at the given position i. If no index is specified, it removes and returns the last item.

## Dictionaries
* Store data in key value pairs, these key value pairs are written as key:value
* E.g. `dict_1 = {'brand': 'ford' , 'cost': 25000}`
* To update you would just do dict_1['brand'] = 'Audi'
* `.items()` method returns all the key value pairs in the dictionary object
* `.keys()` returns all the keys in the dictionary
* `.values()` returns all the values

## Numpy
```
numpy.array()
➜ What it does:
Creates a NumPy array from a list or tuple.

➜ When to use it:
Use it whenever you need to work with numerical data efficiently instead of using
```
```
numpy.linspace()
➜ What it does:
Generates an array of evenly spaced numbers between a given range.

➜ When to use it:
Use it when you need a range of values for plotting or simulations.
```
```
numpy.random.randint()
➜ What it does:
Generates random integers within a given range.

➜ When to use it:
Use it when you need random integers for simulations, testing, or games.
```
```
numpy.reshape()
➜ What it does:
Changes the shape of an array without changing its data.

➜ When to use it:
Use it when you need to change a 1D array to a 2D or 3D format.
```
```
numpy.flatten()
➜ What it does:
Converts a multi-dimensional array into a 1D array.

➜ When to use it:
Use it when you need to process data as a single list.
```
```
numpy.transpose()
➜ What it does:
Swaps the rows and columns of a 2D array (matrix).

➜ When to use it:
Use it when you need to switch axes in a matrix for mathematical operations.
```
```
numpy.add()
➜ What it does:
Element-wise addition of two arrays.

➜ When to use it:
Use it when adding corresponding elements in two arrays.
```
```
numpy.subtract()
➜ What it does:
Element-wise subtraction of two arrays.

➜ When to use it:
Use it when you need to find the difference between two arrays.
```
```
numpy.multiply()
➜ What it does:
Element-wise multiplication of two arrays.

➜ When to use it:
Use it for scalar multiplication or Hadamard product (element-wise).
```
```
numpy.divide()
➜ What it does:
Element-wise division of two arrays.

➜ When to use it:
Use it when performing division between corresponding elements.
```
```
numpy.power()
➜ What it does:
Raises elements of an array to a given power.

➜ When to use it:
Use it when applying exponentiation to an array.
```
```
numpy.mean()
➜ What it does:
Computes the average of an array.

➜ When to use it:
Use it to calculate the mean of a dataset.
```
```
numpy.median()
➜ What it does:
Finds the middle value in a sorted array.

➜ When to use it:
Use it to find the median in statistics.
```
```
numpy.average()
➜ What it does:
Computes the weighted average.

➜ When to use it:
Use it when calculating the mean with different weights.
```
```
numpy.std()
➜ What it does:
Calculates the standard deviation.

➜ When to use it:
Use it to measure data dispersion.
```
```
numpy.var()
➜ What it does:
Computes the variance of an array.

➜ When to use it:
Use it when analyzing data variability.
```
```
numpy.min()
➜ What it does:
Finds the smallest element in an array.

➜ When to use it:
Use it to get the minimum value from a dataset.
```
```
numpy.mod()
➜ What it does:
Computes the remainder of division element-wise.

➜ When to use it:
Use it when working with cycles or periodic calculations.
```
## Pandas 
* Pandas is a powerful data analysis library in Python that provides various functions for data manipulation and analysis. Here are some of the main functions used in Pandas:
1. Creating DataFrames & Series:
   * pd.DataFrame() – Creates a DataFrame from a dictionary, list, NumPy array, etc.
   * pd.Series() – Creates a Pandas Series (1D array with labels).
2. Reading & Writing Data:
   * pd.read_csv('file.csv') – Reads a CSV file into a DataFrame.
   * df.to_csv('file.csv') – Writes a DataFrame to a CSV file.
   * pd.read_excel('file.xlsx') – Reads an Excel file into a DataFrame.
   * df.to_excel('file.xlsx') – Writes a DataFrame to an Excel file.
3. Exploring Data:
   * df.head(n) – Returns the first n rows of the DataFrame.
   * df.tail(n) – Returns the last n rows.
   * df.info() – Provides info about the DataFrame (columns, data types, non-null values).
   * df.describe() – Gives summary statistics of numeric columns.
   * df.shape – Returns the number of rows and columns.
   * df.columns – Lists all column names.
4. Selecting & Filtering Data:
   * df['column_name'] – Selects a single column as a Series.
   * df[['col1', 'col2']] – Selects multiple columns.
   * df.loc[row_label, col_label] – Selects data by label.
   * df.iloc[row_index, col_index] – Selects data by position.
   * df[df['column'] > value] – Filters rows based on a condition.
5. Data Cleaning:
   * df.dropna() – Removes rows with missing values.
   * df.fillna(value) – Fills missing values with a specified value.
   * df.drop(columns=['col1', 'col2']) – Drops specific columns.
   * df.rename(columns={'old_name': 'new_name'}) – Renames columns.
6. Modifying Data:
   * df['new_col'] = df['col1'] + df['col2'] – Creates a new column.
   * df.apply(function, axis=1 or 0) – Applies a function row-wise or column-wise.
   * df.replace({'old_value': 'new_value'}) – Replaces values in a DataFrame.
7. Grouping & Aggregation:
   * df.groupby('column').sum() – Groups data by a column and applies an aggregate function.
   * df.agg({'col1': 'mean', 'col2': 'sum'}) – Aggregates multiple columns with different functions.
   * df.pivot_table(values='col', index='col1', columns='col2', aggfunc='sum') – Creates a pivot table.
8. Sorting & Ordering:
   * df.sort_values(by='column', ascending=True) – Sorts by a column.
9. Merging & Joining DataFrames:
   * pd.concat([df1, df2]) – Concatenates DataFrames along rows or columns.
   * df1.merge(df2, on='common_column', how='inner') – Merges two DataFrames.
10. Exporting Data:
    * df.to_csv('file.csv', index=False) – Saves DataFrame to CSV.
    * df.to_excel('file.xlsx', index=False) – Saves DataFrame to Excel.