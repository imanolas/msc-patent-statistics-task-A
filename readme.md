# Part 1 of Assignment 1 - IR_MSc_Web_Intelligence - 2020[cite: 3]

## Author
* **Ioannis Manolas** (132020)[cite: 3]

---

## Assignment Specification

Using the collection of patent documents in XML format (using the data from the main assignment), perform the following tasks[cite: 3]:

**A)** Create an algorithm that takes as input a collection of patents in XML format and writes the following statistics to a text file. The patents are located in subfolders rather than a single directory[cite: 3].

### Required Output Metrics:
* Number of all patent-documents:[cite: 3]
* Number of all patents:[cite: 3]
* Average number of ipc codes per patents:[cite: 3]
* Number of patents containing section:[cite: 3]
* Distribution of all the different sections:[cite: 3]
* Average number of sections per patents:[cite: 3]
* Number of patents containing class:[cite: 3]
* Distribution of all the different classes:[cite: 3]
* Average number of classes per patents:[cite: 3]
* Number of patents containing subclass:[cite: 3]
* Distribution of all the different subclasses:[cite: 3]
* Average number of subclasses per patents:[cite: 3]
* Number of patents containing group:[cite: 3]
* Average number of groups per patents:[cite: 3]
* Number of patents containing subgroup:[cite: 3]
* Average number of subgroups per patents:[cite: 3]
* Number of patents not containing title:[cite: 3]
* Number of patents not containing ipc-codes:[cite: 3]
* Number of patents containing abstract:[cite: 3]
* Number of patents containing description:[cite: 3]
* Number of patents containing contain claims:[cite: 3]
* Number of patents containing all previous:[cite: 3]
* Number of patents containing abstract and claims:[cite: 3]
* Number of patents containing description and claims:[cite: 3]
* Number of patents containing abstract and description:[cite: 3]
* Number of patents containing abstract in more than 1 language:[cite: 3]
* Number of patents containing description in more than 1 language:[cite: 3]
* Number of patents containing claims in more than 1 language:[cite: 3]
* Number of patents where main language is English:[cite: 3]
* Number of patents where main language is German:[cite: 3]
* Number of patents where main language is French:[cite: 3]
* Number of English patents containing abstract in non-English:[cite: 3]
* Number of English patents containing description in non-English:[cite: 3]
* Number of English patents containing claims in non-English:[cite: 3]
* Number of non-english patents containing abstract in English:[cite: 3]
* Number of non-english patents containing description in English:[cite: 3]
* Number of non-english patents containing claims in English:[cite: 3]
* Min number of words in abstract:[cite: 3]
* Max number of words in abstract:[cite: 3]
* Average number of words in abstract:[cite: 3]
* Min number of words in description:[cite: 3]
* Max number of words in description:[cite: 3]
* Average number of words in description:[cite: 3]
* Min number of words in claims:[cite: 3]
* Max number of words in claims:[cite: 3]
* Average number of words in claims:[cite: 3]

---

## Solution Overview

For the solution of the 1st part, we used the Python programming language to create a script that iterates through all existing patent files to calculate the statistics[cite: 3].

### Python Libraries Used:
* **numpy**: For data storage[cite: 3].
* **pandas**: For data storage and processing[cite: 3].
* **os**: For opening and writing to external files[cite: 3].
* **re**: For finding and processing data using regular expressions[cite: 3].
* **statistics**: For calculating metrics like the mean and variance[cite: 3].
* **nltk**: For data cleaning and text processing[cite: 3].
* **BeautifulSoup**: For extracting data from `.xml` format files with specific tags[cite: 3].

The final script was executed across all data (106,087 patent document files)[cite: 1, 3].

---

## Important Note

For the correct execution of the script, the specific code block containing the path to the documents must be updated to match the user's local directory[cite: 3]:
```python
dir = 'patents/'