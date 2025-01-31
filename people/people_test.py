def test():
    from omnigibson import lazy
    # lazy.omni.isaac.core.utils.extensions.disable_extension("omni.anim.people")
    # lazy.omni.isaac.core.utils.extensions.enable_extension("omni.anim.people")
    lazy.omni.anim.people.ui_components.CommandTextWidget.textbox_commands = """Spawn Tom 5 0 0 0
    Tom GoTo  0 10 0 _"""
    c = lazy.omni.anim.people.ui_components.CharacterSetupWidget(None)
    c._load_characters_on_clicked()
    c._setup_characters_on_clicked()
    setting = lazy.carb.settings.get_settings()
    setting.set(
        lazy.omni.anim.people.settings.PeopleSettings.NAVMESH_ENABLED, False)

