from devtools.core.validation import ValidationResult
from devtools.doctor.checks.check import Check
import devtools.setup.doxygen as doxygen


class DoxygenCheck(Check):
    type_id = "DoxygenCheck"
    name = "Doxygen"
    description = "Validates the Doxygen installation."

    def validate(self) -> ValidationResult:
        return doxygen.validate()

    def fix(self) -> bool:
        return doxygen.install()
