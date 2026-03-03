from devtools.core.validation import ValidationResult
from devtools.doctor.checks.check import Check
import devtools.setup.vulkan as vk


class VulkanCheck(Check):
    type_id = "VulkanCheck"
    name = "Vulkan SDK"
    description = "Validates Vulkan SDK installation."

    def validate(self) -> ValidationResult:
        return vk.validate()

    def fix(self) -> bool:
        return vk.install()
