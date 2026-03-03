require('vstudio')

-- This property is used to copy the C++ runtime DLLs to the project's output directory after compilation.
premake.api.register {
    name = "copyruntime",
    scope = "config",
    kind = "boolean"
}

premake.override(premake.vstudio.vc2010.elements, "configurationProperties", function(base, cfg)
    local elements = base(cfg)

    table.insert(elements, function()
        if cfg.copyruntime then
            premake.vstudio.vc2010.element("CopyCppRuntimeToOutputDir", nil, "true")
        end
    end)

    return elements
end)
