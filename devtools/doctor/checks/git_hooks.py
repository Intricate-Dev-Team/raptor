from devtools.core.validation import ValidationResult
from devtools.doctor.checks.check import Check
import devtools.setup.hooks as hooks


class GitHooksCheck(Check):
    type_id = "GitHooksCheck"
    name = "Git Hooks"
    description = "Validates the installed Git Hooks."

    def validate(self) -> ValidationResult:
        return hooks.validate()

    def fix(self) -> bool:
        return hooks.install()
