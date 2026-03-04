from devtools.core.validation import ValidationResult
from devtools.doctor.checks.check import Check
import devtools.setup.dotnet as dotnet


class DotNetCheck(Check):
    type_id = "DotNetCheck"
    name = ".NET SDK"
    description = "Validates the .NET SDK installation."

    def validate(self) -> ValidationResult:
        return dotnet.validate()

    def fix(self) -> bool:
        return dotnet.install()
