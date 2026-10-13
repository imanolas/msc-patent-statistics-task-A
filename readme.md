# Assignment 1

## Author
* **Ioannis Manolas**

---

## Assignment Specification

Using the collection of patent documents in XML format (using the data from the main assignment), perform the following tasks:

**A)** Create an algorithm that takes as input a collection of patents in XML format and writes the following statistics to a text file. The patents are located in subfolders rather than a single directory.

### Required Output Metrics:
* Number of all patent-documents:
* Number of all patents:
* Average number of ipc codes per patents:
* Number of patents containing section:
* Distribution of all the different sections:
* Average number of sections per patents:
* Number of patents containing class:
* Distribution of all the different classes:
* Average number of classes per patents:
* Number of patents containing subclass:
* Distribution of all the different subclasses:
* Average number of subclasses per patents:
* Number of patents containing group:
* Average number of groups per patents:
* Number of patents containing subgroup:
* Average number of subgroups per patents:
* Number of patents not containing title:
* Number of patents not containing ipc-codes:
* Number of patents containing abstract:
* Number of patents containing description:
* Number of patents containing contain claims:
* Number of patents containing all previous:
* Number of patents containing abstract and claims:
* Number of patents containing description and claims:
* Number of patents containing abstract and description:
* Number of patents containing abstract in more than 1 language:
* Number of patents containing description in more than 1 language:
* Number of patents containing claims in more than 1 language:
* Number of patents where main language is English:
* Number of patents where main language is German:
* Number of patents where main language is French:
* Number of English patents containing abstract in non-English:
* Number of English patents containing description in non-English:
* Number of English patents containing claims in non-English:
* Number of non-english patents containing abstract in English:
* Number of non-english patents containing description in English:
* Number of non-english patents containing claims in English:
* Min number of words in abstract:
* Max number of words in abstract:
* Average number of words in abstract:
* Min number of words in description:
* Max number of words in description:
* Average number of words in description:
* Min number of words in claims:
* Max number of words in claims:
* Average number of words in claims:

---

## Solution Overview

For the solution of the 1st part, we used the Python programming language to create a script that iterates through all existing patent files to calculate the statistics.

### Python Libraries Used:
* **numpy**: For data storage.
* **pandas**: For data storage and processing.
* **os**: For opening and writing to external files.
* **re**: For finding and processing data using regular expressions.
* **statistics**: For calculating metrics like the mean and variance.
* **nltk**: For data cleaning and text processing.
* **BeautifulSoup**: For extracting data from `.xml` format files with specific tags.

The final script was executed across all data (106,087 patent document files).

---

## Important Note

For the correct execution of the script, the specific code block containing the path to the documents must be updated to match the user's local directory:
```python
dir = 'patents/'
