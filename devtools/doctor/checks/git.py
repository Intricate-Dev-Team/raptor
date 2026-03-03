from devtools.core.validation import ValidationResult
from devtools.doctor.checks.check import Check
import devtools.setup.git as git


class GitCheck(Check):
    type_id = "GitCheck"
    name = "Git for Windows"
    description = "Validates the Git for Windows installation."

    def validate(self) -> ValidationResult:
        return git.validate()

    def fix(self) -> bool:
        return git.install()
