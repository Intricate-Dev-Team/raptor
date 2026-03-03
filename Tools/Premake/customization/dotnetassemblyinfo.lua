require('vstudio')

-- Implement the dotnetassemblyinfo command for project-scope files
premake.api.register {
    name = "dotnetassemblyinfo",
    scope = "project",
    kind = "string", -- Can be "on" or "off"
}

-- Inject the <GenerateAssemblyInfo> element into the C# project
local function generateAssemblyInfo(prj)
    if not prj.dotnetassemblyinfo then
        return
    end

    local value = string.lower(prj.dotnetassemblyinfo)
    if value ~= "on" and value ~= "off" then
        value = "off" -- Default to off if invalid
    end

    _p(2, '<GenerateAssemblyInfo>%s</GenerateAssemblyInfo>', value)
end

premake.override(premake.vstudio.cs2005.elements, "projectProperties", function(base, prj)
    return table.join(base(prj), { generateAssemblyInfo })
end)
