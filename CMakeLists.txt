
set(LLVM_ENABLE_PROJECTS "clang" CACHE STRING
    "Semicolon-separated list of projects to build (${LLVM_KNOWN_PROJECTS}), or \"all\".")

add_subdirectory(llvm)
