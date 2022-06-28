Import('env')
# print(env.Dump())
# env.Append(
#     CPPDEFINES=["HELLO=WORLD", "TAG=1.2.3", "DEBUG"],
#     CPPPATH=["inc", "inc/devices"]
# )

global_env = DefaultEnvironment()
global_env.Append(
    CPPDEFINES=[
        ("ARDUINO", 100),
    ]
)