require('vstudio')

-- Implement the solutionitems command for solution-scope files
premake.api.register
{
    name = "solutionitems",
    scope = "workspace",
    kind = "list:string",
}

premake.override(premake.vstudio.sln2026, "projects", function(base, wks)
    if wks.solutionitems and #wks.solutionitems > 0 then
        premake.push("<Folder Name=\"/Solution Items/\">")
        for _, path in ipairs(wks.solutionitems) do
            premake.w("<File Path=\"%s\" />", path)
        end

        premake.pop("</Folder>")
    end
    base(wks)
end)
