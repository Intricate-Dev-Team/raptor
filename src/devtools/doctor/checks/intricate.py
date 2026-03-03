from devtools.core.fs import tools_dir
from devtools.core.git import repo_root
from devtools.core.process import run
from devtools.core.validation import ValidationResult, Severity
from devtools.doctor.checks.check import Check


class IntricateCheck(Check):
    type_id = "IntricateCheck"
    name = "Intricate-DevTools"
    description = "Validates this installation of Intricate-DevTools."

    def validate(self) -> ValidationResult:
        root = repo_root()
        devtools_dir = str(tools_dir() / "DevTools").replace('\\', '/')

        installed_ver = run(["intricate", "--version"], cwd = root, capture = True)
        repo_ver = run(["python", "-c",
                        f"import sys; sys.path.insert(0, '{devtools_dir}'); import devtools; print(devtools.__version__)"],
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
