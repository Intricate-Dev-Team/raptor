from devtools.config.loader import CONFIG
from devtools.core.log import error
from devtools.doctor.checks.check import Check
from devtools.doctor.checks.git import GitCheck
from devtools.doctor.checks.git_hooks import GitHooksCheck
from devtools.doctor.checks.intricate import IntricateCheck
from devtools.doctor.checks.doxygen import DoxygenCheck
from devtools.doctor.checks.vulkan import VulkanCheck
from devtools.doctor.checks.vulkan_driver import VulkanDriverCheck
from devtools.doctor.checks.dotnet import DotNetCheck
from devtools.doctor.checks.visualstudio import VisualStudioCheck
from devtools.doctor.checks.windows import WindowsCheck
from devtools.doctor.checks.cpp23 import Cpp23Check


def get_checks() -> list[Check]:
    _CHECK_NAME_MAP: dict[str, type[Check]] = {
        "cpp23": Cpp23Check,
        "dotnet": DotNetCheck,
        "doxygen": DoxygenCheck,
        "git": GitCheck,
        "git-hooks": GitHooksCheck,
        "intricate": IntricateCheck,
        "vulkan": VulkanCheck,
        "vulkan-driver": VulkanDriverCheck,
        "visualstudio": VisualStudioCheck,
        "windows": WindowsCheck
    }

    checks: list[Check] = []
    for check in CONFIG.doctor.checks:
        if not check.enabled:
            continue

        check_cls = _CHECK_NAME_MAP.get(check.name)
        if not check_cls:
            error(f"Unknown doctor check '{check.name}'!")
            continue

        checks.append(check_cls())

    return checks

def type_id_to_check(type_id: str) -> Check | None:
    _CHECK_TYPE_MAP: dict[str, type[Check]] = {
        GitCheck().type_id: GitCheck,
        IntricateCheck().type_id: IntricateCheck,
        GitHooksCheck().type_id: GitHooksCheck,
        DoxygenCheck().type_id: DoxygenCheck,
        VulkanCheck().type_id: VulkanCheck,
        VulkanDriverCheck().type_id: VulkanDriverCheck,
        DotNetCheck().type_id: DotNetCheck,
        VisualStudioCheck().type_id: VisualStudioCheck,
        WindowsCheck().type_id: WindowsCheck,
        Cpp23Check().type_id: Cpp23Check
    }

    if type_id not in _CHECK_TYPE_MAP:
        return None

    return _CHECK_TYPE_MAP[type_id]()
