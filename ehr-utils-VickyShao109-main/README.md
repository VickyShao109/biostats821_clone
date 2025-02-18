# EHR Utils Library (Object-Oriented)

The EHR Utils Library designed using an object-oriented approach, streamlines the processing and analysis of Electronic Health Records (EHR) data. It introduces classes for patient and laboratory test records, enabling more intuitive and effective data management and analysis. The library facilitates parsing EHR data from files, calculating patient age, evaluating health conditions through lab tests, and determining the age at the first recorded lab, among other features.

## For End Users

### Setup/Installation Instructions

Before using the EHR Utils Library, ensure Python 3.8 or higher is installed on your system. Follow the steps below to set up the library:

```sh
git clone https://github.com/biostat821-2024/ehr-utils-VickyShao109
cd ehr-utils-VickyShao109
```

### Expected Input File Formats

- **Patient Data File (`patients.tsv`):** Should include columns for `PatientID`, `Gender`, `PatientDateOfBirth`, `Race`, and possibly other demographic details.

- **Lab Data File (`labs.tsv`):** Should comprise columns for `PatientID`, `LabName`, `LabValue`, `LabUnits`, and `LabDateTime`.

### Key Classes and Methods

- `Patient`: A class representing patients, encapsulating personal and demographic information along with a list of associated `Lab` objects.
- `Lab`: A class representing individual laboratory test results.
- `parse_data`: A function for parsing patient and lab data from files, returning a dictionary of `Patient` instances keyed by patient IDs.

### Examples

**Parsing Data and Accessing Patient Information:**

```python
from ehr_utils_Vicky import parse_data

# Load patient and lab data from files
record = parse_data(
    "path/to/patients.tsv",
    "path/to/labs.tsv"
)

# Example of accessing a specific patient's information
patient_id = "FB2ABB23-C9D0-4D09-8464-49BF0B982F0F"
if patient_id in record:
    patient = record[patient_id]
    print(patient)

```

**Calculating Age:**

```python
print(patient.age)
```

**Checking Health Conditions:**

```python
condition = patient.is_sick("URINALYSIS: RED BLOOD CELLS", ">", 2.0)
print(condition)
```

**Calculating Age at First Lab:**

```python
age_first_lab = patient.age_at_first_lab()
print(age_first_lab)
```

## For Contributors

The EHR Utils Library is designed with testability in mind, allowing for comprehensive validation of its functionalities. Below are examples of tests that can be run to ensure the library's classes and methods behave as expected.

### Running Tests

Tests are written using pytest. To run the tests, ensure pytest is installed in your environment, then execute the following command in the terminal:

```sh
pytest tests/test_ehr_utils_Vicky.py 
```

### Test Examples

Our test suite covers various aspects of the library, including calculating patient age, identifying sick patients based on lab results, and verifying the parsing of patient and lab data. Here's a brief overview of the tests:

**Test Patient Age Calculation:**

Verifies that the `Patient` class correctly calculates ages based on the date of birth.

**Test Health Condition Checks:**

Confirms the ability of the `is_sick` method to accurately determine a patient's health condition based on lab results.

**Test Age Calculation at First Lab:**

Ensures that the library can correctly calculate a patient's age at the time of their first recorded lab.

**Test Data Parsing:**

Demonstrates how to test the `parse_data` parsing patient and lab data from TSV files.