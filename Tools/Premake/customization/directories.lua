require("vstudio")

premake.api.register {
    name = "directories",
    scope = "project",
    kind = "list:string",
}

-- C# (.csproj) Implementation
local function writeCSharpDirectories(prj)
    local dirs = prj.directories or {}
    if #dirs > 0 then
        premake.push('<ItemGroup>')

        for _, pattern in ipairs(dirs) do
            local path = pattern:gsub("/", "\\")
            local tag = "Compile"

            if path:find("%.xaml$") then
                tag = "Page"
            elseif path:find("%.config$") or path:find("%.settings$") then
                tag = "None"
            end

            premake.w('<%s Include="%s" />', tag, path)
        end

        premake.pop('</ItemGroup>')
    end
end

-- Safely override the C# element list
if premake.vstudio and premake.vstudio.cs2005 then
    premake.override(premake.vstudio.cs2005.elements, "project", function(oldfn, prj)
        local list = oldfn(prj)
        table.insert(list, writeCSharpDirectories)

        return list
    end)
end

-- C++ (.vcxproj) Implementation
local function writeCppDirectories(prj)
    local dirs = prj.directories or {}
    if #dirs > 0 then
        premake.push('<ItemGroup>')

        for _, pattern in ipairs(dirs) do
            local path = pattern:gsub("/", "\\")
            local tag = "None"

            if path:find("%.cpp$") or path:find("%.c$") or path:find("%.cc$") then
                tag = "ClCompile"
            elseif path:find("%.h$") or path:find("%.hpp$") then
                tag = "ClInclude"
            end

            premake.w('<%s Include="%s" />', tag, path)
        end

        premake.pop('</ItemGroup>')
    end
end

-- Safely override the C++ element list
if premake.vstudio and premake.vstudio.vc2010 then
    premake.override(premake.vstudio.vc2010.elements, "project", function(oldfn, prj)
        local list = oldfn(prj)
        table.insert(list, writeCppDirectories)

        return list
    end)
end
