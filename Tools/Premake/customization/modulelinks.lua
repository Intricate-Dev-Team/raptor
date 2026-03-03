-- This extension does what its supposed to but Visual Studio is weird and even with the module added here, we still can't link against it

require "vstudio"

premake.api.register {
    name = "modulelinks",
    scope = "config",
    kind = "list:string"
}

premake.override(premake.vstudio.vc2010.elements, "clCompile", function(base, cfg)
    local elements = base(cfg)

    if cfg.modulelinks and (#cfg.modulelinks > 0) then
        local final_dirs = {}
        for _, dir in ipairs(cfg.modulelinks) do
            -- Premake string expansion
            local expanded_path = premake.detoken.expand(dir, cfg.environ)
            table.insert(final_dirs, expanded_path)
        end

        table.insert(elements, function()
            premake.vstudio.vc2010.element("AdditionalModuleDependencies", nil, (table.concat(final_dirs, ";") .. ";%%(AdditionalModuleDependencies)"))
        end)
    end

    return elements
end)
