name = "llvm"

version = "15.0.7.sse.1.0.0"

description = \
    """
    LLVM compiler
    """

with scope("config") as c:
    # Determine location to release: internal (int) vs external (ext)

    # NOTE: Modify this variable to reflect the current package situation
    release_as = "ext"

    # The `c` variable here is actually rezconfig.py
    # `release_packages_path` is a variable defined inside rezconfig.py

    import os
    if release_as == "int":
        c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_INT"]
    elif release_as == "ext":
        c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_EXT"]

requires = [
]

private_build_requires = [
]

variants = [
    ["platform-linux", "arch-x86_64", "os-centos-7"]
]

uuid = "repository.llvm-project"
build_system = "cmake"


def pre_build_commands():
    # command("source /opt/rh/devtoolset-6/enable")
    command("source /opt/rh/devtoolset-7/enable")


def commands():
    env.LLVM_LOCATION = "{root}"
    env.LLVM_ROOT = "{root}"
    env.LLVM_INCLUDE_DIR = "{root}/include"
    env.LLVM_LIBRARY_DIR = "{root}/lib"
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
    env.PATH.prepend("{root}/bin")
