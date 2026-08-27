# 🐼 Learning Pandas in Python

A beginner-friendly repository documenting my journey of learning **Pandas in Python** through hands-on examples, practice programs, and real datasets.

This repository contains Python programs covering the fundamentals of Pandas, along with a Jupyter Notebook and Pokémon datasets used for practicing data manipulation and analysis.

---

## 📌 About This Project

This project was created while learning the **Pandas library in Python** and focuses on understanding how Pandas can be used to work with structured data.

The repository progresses from basic Pandas concepts to more practical operations such as:

* Creating Series and DataFrames
* Selecting rows and columns
* Reading CSV and JSON files
* Filtering data
* Performing statistical operations
* Grouping and aggregating data
* Handling missing values
* Removing duplicates
* Converting data types
* Working with real datasets

The goal is to build a strong foundation in Pandas before moving toward more advanced **Data Analysis, Data Science, and Machine Learning** projects.

---

## 📂 Repository Structure

```text
Learning_Pandas/
│
├── 📁 Programs/
│   ├── 01_hello_world.py
│   ├── 02_check_pandas_version.py
│   ├── 03_series_basic.py
│   ├── ...
│   └── 71_drop_duplicates.py
│
├── 📓 Learning_Pandas.ipynb
├── 📊 Pokemon.csv
├── 📄 Pokemon2.json
└── 📖 README.md
```

---

## 📚 Topics Covered

### 1. Pandas Series

Learned how to:

* Create Pandas Series
* Work with Series indexes
* Create Series with custom indexes
* Create Series from dictionaries
* Select data using `.loc`

### 2. DataFrames

Learned how to:

* Create DataFrames
* Create DataFrames from dictionaries
* Work with rows and columns
* Select individual columns
* Select multiple columns
* Use custom indexes

### 3. Reading Data

Practiced loading data from different file formats:

```python
pd.read_csv()
pd.read_json()
```

Datasets included in this project:

* `Pokemon.csv`
* `Pokemon2.json`

### 4. Data Selection & Filtering

Practiced selecting and filtering data based on conditions.

Examples include:

* Selecting Pokémon by height
* Finding Legendary Pokémon
* Filtering Water-type Pokémon
* Filtering Fire-type Pokémon

### 5. Statistical Operations

Practiced common Pandas operations such as:

```python
.mean()
.sum()
.min()
.max()
.count()
```

These operations were applied to columns and datasets to understand basic data analysis.

### 6. GroupBy & Aggregation

Learned how to group data and perform calculations using:

```python
.groupby()
```

Examples include grouping Pokémon by their types and calculating:

* Mean values
* Sum values
* Counts

### 7. Cleaning Data

Practiced basic data-cleaning techniques including:

```python
.drop()
.dropna()
.fillna()
.drop_duplicates()
```

These operations are important when preparing datasets for analysis and machine learning.

### 8. Data Type Conversion

Learned how to convert columns between different data types using:

```python
.astype()
```

### 9. String/Data Transformation

Practiced modifying column values, including converting text to:

```python
.upper()
.lower()
```

---

## 🧪 Learning Approach

The repository follows a **step-by-step learning approach**.

Each Python file focuses on a specific Pandas concept, making it easier to:

1. Understand one concept at a time
2. Run the example
3. Experiment with the code
4. Modify it
5. Observe the output
6. Move on to the next concept

The `Learning_Pandas.ipynb` notebook provides an interactive environment for experimenting with the concepts learned.

---

## 🛠️ Technologies Used

* 🐍 **Python**
* 🐼 **Pandas**
* 📓 **Jupyter Notebook**
* 📊 **CSV**
* 📄 **JSON**
* 💻 **Git & GitHub**

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Soutikkk/Learning_Pandas.git
```

### 2. Navigate to the project

```bash
cd Learning_Pandas
```

### 3. Install Pandas

```bash
pip install pandas
```

### 4. Run a program

For example:

```bash
python Programs/22_read_csv_file.py
```

You can also open:

```text
Learning_Pandas.ipynb
```

using Jupyter Notebook or JupyterLab.

---

## 📊 Dataset

The project uses a **Pokémon dataset** for practicing Pandas operations.

The dataset makes it easier to understand data manipulation using familiar attributes such as:

* Pokémon Name
* Type
* Height
* Weight
* Legendary status
* Other Pokémon statistics

The CSV and JSON files are used to practice loading and working with structured data.

---

## 🎯 Learning Goals

Through this project, I aim to build a strong foundation in:

* Data manipulation
* Data cleaning
* Exploratory data analysis
* Working with structured datasets
* Python data analysis libraries
* Preparing data for Machine Learning

This repository will also serve as a reference for future **Data Science and Machine Learning projects**.

---

## 📈 Progress

* [x] Python basics required for Pandas
* [x] Pandas Series
* [x] Pandas DataFrames
* [x] Row and column selection
* [x] CSV files
* [x] JSON files
* [x] Data filtering
* [x] Statistical operations
* [x] GroupBy
* [x] Missing data handling
* [x] Duplicate handling
* [x] Data type conversion
* [x] Basic data transformation

---

## 🙏 Credits & Learning Resource

A major reference for learning the concepts in this repository was the **Bro Code** Pandas tutorial on YouTube.

**Creator:** Bro Code
**Platform:** YouTube
**Topic:** Pandas in Python

The examples and explanations from the tutorial were used as a learning reference while building and practicing the programs in this repository.

> This repository is a personal learning project created for educational purposes.

---

## 👨‍💻 Author

**Soutikkk**

Learning Python → Pandas → Data Analysis → Machine Learning 🚀

---

## ⭐ Support

If you find this repository useful for learning Pandas, feel free to **⭐ star the repository** and explore the programs.

Happy Learning! 🐼📊🐍
