from raptor.core.fs import tools_dir
from raptor.core.git import repo_root
from raptor.core.process import run
from raptor.core.validation import ValidationResult, Severity
from raptor.doctor.checks.check import Check


class IntricateCheck(Check):
    type_id = "IntricateCheck"
    name = "Intricate-DevTools"
    description = "Validates this installation of Intricate-raptor."

    def validate(self) -> ValidationResult:
        root = repo_root()
        devtools_dir = str(tools_dir() / "DevTools").replace('\\', '/')

        installed_ver = run(["intricate", "--version"], cwd = root, capture = True)
        repo_ver = run(["python", "-c",
                        f"import sys; sys.path.insert(0, '{devtools_dir}'); import devtools; print(raptor.__version__)"],
                        cwd = root, capture = True)

        if installed_ver != repo_ver:
            return ValidationResult(
                valid = False,
                severity = Severity.ERROR,
                message = "Incorrect Intricate-DevTools version installed!"
            )

        return ValidationResult(
            valid = True,
            severity = Severity.NONE
        )

    def fix(self) -> bool:
        root = repo_root()
        res = run(["python", "-m", "pip", "install", f"\"{tools_dir() / "DevTools"}\"", "--quiet"], cwd = root, capture = True)

        return len(res) != 0
