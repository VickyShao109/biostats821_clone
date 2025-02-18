"""Functions object-orientated."""

from datetime import datetime


class Lab:
    """Represents a laboratory test result."""

    def __init__(
        self, lab_name: str, lab_value: float, lab_units: str, lab_date: str
    ):
        """Initialize a lab result."""
        self.name = lab_name
        self.value = lab_value
        self.units = lab_units
        self.date = datetime.strptime(lab_date, "%Y-%m-%d %H:%M:%S.%f")

    def __eq__(self, other: object) -> bool:
        """Check equality of two Lab instances."""
        if not isinstance(other, Lab):
            return NotImplemented
        return (
            self.name == other.name
            and self.value == other.value
            and self.units == other.units
            and self.date == other.date
        )

    def __str__(self) -> str:
        """Return a string representation of the lab result."""
        return f"{self.name}: {self.value} {self.units} on {self.date}"


class Patient:
    """Represents a patient with personal information and lab results."""

    def __init__(self, patient_id: str, gender: str, dob: str, race: str):
        """Initialize a patient with ID, DOB, gender, race.

        and an optional list of Lab objects.
        """
        self.patient_id = patient_id
        self.gender = gender
        self.dob = datetime.strptime(dob, "%Y-%m-%d %H:%M:%S.%f")
        self.race = race
        self.labs: list[Lab] = []

    def add_lab(self, lab: Lab) -> None:
        """Add lab to patient."""
        self.labs.append(lab)

    def __eq__(self, other: object) -> bool:
        """Check equality of two Patient instances."""
        if not isinstance(other, Patient):
            return NotImplemented
        return (
            self.patient_id == other.patient_id
            and self.gender == other.gender
            and self.dob == other.dob
            and self.race == other.race
            and self.labs == other.labs
        )

    def __str__(self) -> str:
        """Return a string representation of the patient."""
        return (
            f"Patient ID: {self.patient_id}, "
            f"Age: {self.age}, "
            f"Gender: {self.gender}, "
            f"Race: {self.race}"
        )

    @property
    def age(self) -> int:
        """Calculate and return the patient's current age."""
        today = datetime.today()
        return (
            today.year
            - self.dob.year
            - ((today.month, today.day) < (self.dob.month, self.dob.day))
        )

    def is_sick(self, lab_name: str, operator: str, value: float) -> bool:
        """Determine if the patient is sick based on a lab result."""
        for lab in self.labs:
            if (
                lab.name == lab_name
                and (operator == ">" and lab.value > value)
                or (operator == "<" and lab.value < value)
            ):
                return True
        return False

    def age_at_first_lab(self) -> int:
        """Calculate the patient's age at their first recorded lab."""
        if not self.labs:
            # Handle the case where no labs are recorded
            raise ValueError("No lab records available for this patient.")

        earliest_lab_date = min(lab.date for lab in self.labs)
        return (
            earliest_lab_date.year
            - self.dob.year
            - (
                (earliest_lab_date.month, earliest_lab_date.day)
                < (self.dob.month, self.dob.day)
            )
        )


def parse_data(patient_filename: str, lab_filename: str) -> dict[str, Patient]:
    """Parses patient and lab data from TSV files.

    Into a dictionary of Patient objects with embedded Lab data.
    """
    records: dict[str, Patient] = {}

    with open(patient_filename) as pf:
        headers = pf.readline().strip().split("\t")
        for line in pf:
            values = line.strip().split("\t")
            patient_data = dict(zip(headers, values))
            patient_id = patient_data.pop("PatientID")
            records[patient_id] = Patient(
                patient_id,
                patient_data["PatientGender"],
                patient_data["PatientDateOfBirth"],
                patient_data["PatientRace"],
            )

    with open(lab_filename) as lf:
        headers = lf.readline().strip().split("\t")
        for line in lf:
            values = line.strip().split("\t")
            lab_data = dict(zip(headers, values))
            lab = Lab(
                lab_data["LabName"],
                float(lab_data["LabValue"]),
                lab_data["LabUnits"],
                lab_data["LabDateTime"],
            )
            records[lab_data["PatientID"]].add_lab(lab)

    return records
