"""Test classes and methods in the object-oriented EHR analysis approach."""

from ehr_utils_Vicky import Lab, Patient, parse_data


def test_age() -> None:
    """Test if calculated age is equal to the actual age."""
    patient1 = Patient(
        "FB2ABB23-C9D0-4D09-8464-49BF0B982F0F",
        "Male",
        "1947-12-28 02:45:40.547",
        "Unknown",
    )
    patient2 = Patient(
        "64182B95-EB72-4E2B-BE77-8050B71498CE",
        "Male",
        "1952-01-18 19:51:12.917",
        "African American",
    )
    assert patient1.age == 76
    assert patient2.age == 72


def test_patient_is_sick() -> None:
    """Test patient_is_sick to correctly identify sick patients."""
    patient = Patient(
        "FB2ABB23-C9D0-4D09-8464-49BF0B982F0F",
        "Male",
        "1947-12-28 02:45:40.547",
        "Unknown",
    )
    lab1 = Lab(
        "URINALYSIS: RED BLOOD CELLS",
        3.1,
        "rbc/hpf",
        "1968-10-07 14:41:30.843",
    )
    patient.labs.append(lab1)

    assert patient.is_sick("URINALYSIS: RED BLOOD CELLS", ">", 2.0)
    assert not patient.is_sick("URINALYSIS: RED BLOOD CELLS", "<", 2.0)


def test_patient_age_at_first_lab() -> None:
    """Test the calculation of a patient's age at their first recorded lab."""
    patient = Patient(
        "FB2ABB23-C9D0-4D09-8464-49BF0B982F0F",
        "Male",
        "1947-12-28 02:45:40.547",
        "Unknown",
    )
    lab1 = Lab(
        "URINALYSIS: RED BLOOD CELLS",
        3.1,
        "rbc/hpf",
        "1968-10-07 14:41:30.843",
    )
    patient.labs.append(lab1)
    assert patient.age_at_first_lab() == 20


def test_parse_data_from_files() -> None:
    """Test parse_data."""
    patient_file_path = "tests/fake_patient_data.tsv"
    lab_file_path = "tests/fake_lab_data.tsv"

    actual_records = parse_data(patient_file_path, lab_file_path)

    expected_lab1 = Lab(
        "URINALYSIS: RED BLOOD CELLS",
        3.1,
        "rbc/hpf",
        "1968-10-07 14:41:30.843",
    )
    expected_lab2 = Lab(
        "METABOLIC: ALT/SGPT",
        57.1,
        "U/L",
        "1968-10-07 15:40:30.880",
    )
    expected_lab3 = Lab(
        "METABOLIC: CALCIUM",
        9.2,
        "mg/dL",
        "1974-06-13 02:57:29.433",
    )
    expected_lab4 = Lab(
        "METABOLIC: CALCIUM",
        9.3,
        "mg/dL",
        "1976-08-02 19:56:17.130",
    )
    expected_lab5 = Lab(
        "CBC: MCHC",
        38.1,
        "g/dl",
        "1976-08-02 02:31:35.373",
    )

    expected_patient1 = Patient(
        "FB2ABB23-C9D0-4D09-8464-49BF0B982F0F",
        "Male",
        "1947-12-28 02:45:40.547",
        "Unknown",
    )

    expected_patient1.labs.extend(
        [expected_lab1, expected_lab2, expected_lab3]
    )

    expected_patient2 = Patient(
        "64182B95-EB72-4E2B-BE77-8050B71498CE",
        "Male",
        "1952-01-18 19:51:12.917",
        "African American",
    )
    expected_patient2.labs.extend([expected_lab4, expected_lab5])

    expected_records = {
        "FB2ABB23-C9D0-4D09-8464-49BF0B982F0F": expected_patient1,
        "64182B95-EB72-4E2B-BE77-8050B71498CE": expected_patient2,
    }

    assert (
        actual_records == expected_records
    ), "Parsed records do not match the expected records."
