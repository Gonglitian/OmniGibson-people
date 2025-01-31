import omnigibson as og
from omnigibson.macros import gm
from omnigibson import lazy
cfg = dict()

cfg["env"]= {
    "device":
    "cpu",
    }
# Define scene
cfg["scene"] = {
    "type": "Scene",
    "floor_plane_visible": True,
}

# Define objects
cfg["objects"] = [
    {
        "type": "USDObject",
        "name": "ghost_stain",
        "usd_path": f"{gm.ASSET_PATH}/models/stain/stain.usd",
        "category": "stain",
        "visual_only": True,
        "scale": [1.0, 1.0, 1.0],
        "position": [1.0, 2.0, 0.001],
        "orientation": [0, 0, 0, 1.0],
    },
    {
        "type": "DatasetObject",
        "name": "delicious_apple",
        "category": "apple",
        "model": "agveuv",
        "position": [0, 0, 1.0],
    },
    {
        "type": "PrimitiveObject",
        "name": "incredible_box",
        "primitive_type": "Cube",
        "rgba": [0, 1.0, 1.0, 1.0],
        "scale": [0.5, 0.5, 0.1],
        "fixed_base": True,
        "position": [-1.0, 0, 1.0],
        "orientation": [0, 0, 0.707, 0.707],
    },
    {
        "type": "LightObject",
        "name": "brilliant_light",
        "light_type": "Sphere",
        "intensity": 50000,
        "radius": 0.1,
        "position": [3.0, 3.0, 4.0],
    },
]

# Define robots
# cfg["robots"] = [
#     {
#         "type": "Fetch",
#         "name": "skynet_robot",
#         "obs_modalities": ["scan", "rgb", "depth"],
#     },
# ]

# Define task
# cfg["task"] = {
#     "type": "DummyTask",
#     "termination_config": dict(),
#     "reward_config": dict(),
# }

# Create the environment
env = og.Environment(cfg)
assert og.sim.is_playing()  # sim should be playing now
og.sim.stop()
assert og.sim.is_stopped()  # sim should be stopped now

# Enable the extensions for people
EXTENSIONS_PEOPLE = [
    'omni.anim.people',
    'omni.anim.navigation.bundle',
    'omni.anim.timeline',
    'omni.anim.graph.bundle',
    'omni.anim.graph.core',
    'omni.anim.graph.ui',
    'omni.anim.retarget.bundle',
    'omni.anim.retarget.core',
    'omni.anim.retarget.ui',
    'omni.kit.scripting',
    'omni.graph.io',
    'omni.anim.curve.core',
]
for ext_people in EXTENSIONS_PEOPLE:
    lazy.omni.isaac.core.utils.extensions.enable_extension(ext_people)

def setup_people_ext():
    import people
    people.test()
    

for _ in range(3000): # wait for people extension to setup using python code
    # only run setup_people_ext once in loop
    if _ == 0:
        setup_people_ext() # initialize people, bind script etc.
    og.sim.render()


og.sim.play()
assert og.sim.is_playing()  # sim should be playing now
# og.sim.scenes.reset()  # this should reset the scene to its initial state.



# def setup_people_ext():
#     from people_ext.ui_components import CharacterSetupWidget
#     cmd_lines = ["Spawn Tom", "Spawn Jerry 10 10 0 0", "Tom GoTo 10 10 0 _", "Jerry GoTo 0 0 0 _"]
#     c = CharacterSetupWidget()
#     c._load_characters_on_clicked(cmd_lines)
#     # wait for setup
#     finish_setup = False
#     while not finish_setup:
#         finish_setup = c._setup_characters_on_clicked()

# def setup_people_ext():
#     from pegasus.simulator.logic.people.person import Person
#     people_assets_list = Person.get_character_asset_list()
#     for person in people_assets_list:
#         print(person)

#     p = Person("person", "original_female_adult_business_02",
#                 init_pos=[2.0, 0.0, 0.0])
#     p.update_target_position([10.0, 0.0, 0.0], 1.0)




# og.sim.play()

# Allow camera teleoperation
og.sim.enable_viewer_camera_teleoperation()

# # Step!
while True:
    # obs, rew, terminated, truncated, info = env.step(env.action_space.sample())
    og.sim.step()

og.shutdown()