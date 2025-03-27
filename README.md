### Date created

March 28, 2025

### Project Title

Explore US Bikeshare Data

### Description

In this project, you will make use of Python to explore data related to bike share systems for three major cities in the United States—Chicago, New York City, and Washington. You will write code to import the data and answer interesting questions about it by computing descriptive statistics. You will also write a script that takes in raw input to create an interactive experience in the terminal to present these statistics.

###List of what software, firmware and hardware you may require.

- You should have Python 3, NumPy, and pandas installed using Anaconda
- A text editor, like Sublime or Atom.
- A terminal application (Terminal on Mac and Linux or Cygwin on Windows).

### Files used

1. The following file contains necessary code:
   - bikeshare.py
2. The following files are not uploaded to remote repo by using **.gitignore** because the files are too big:
   - chicago.csv
   - new_york_city.csv
   - washington.csv

### Credits

- The original repo of this is forked from can be found here: [link](https://github.com/udacity/pdsnd_github.git "Git")
- [www.stackoverflow.com](www.stackoverflow.com)
- [Pandas documentation is very usefull](https://pandas.pydata.org/docs/)
- [Python documentation for controlflow](https://docs.python.org/3/tutorial/controlflow.html)

## 🔍 Data Validation

### Input Constraints

| Parameter | Valid Values                       | Case Handling    |
| --------- | ---------------------------------- | ---------------- |
| City      | Chicago, New York City, Washington | Case-insensitive |
| Month     | January-June or 'all'              | Case-insensitive |
| Day       | Monday-Sunday or 'all'             | Case-insensitive |

### Data Quality Checks

- Automatic type conversion for datetime columns
- Missing values handled by Pandas automatically
- Washington dataset warnings for missing gender/birth year:
  ```bash
  [INFO] Washington data: Gender/Birth Year columns not available
  ```
