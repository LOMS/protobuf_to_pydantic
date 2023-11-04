import os
import sys

from protobuf_to_pydantic.__version__ import __version__


def p2p_cli() -> None:
    if not len(sys.argv) > 1:
        return
    if "-V" in sys.argv or "--version" in sys.argv:
        # Overwrite the version information of mypy-protobuf
        print("protobuf-to-pydantic " + __version__)
    if "-I" in sys.argv or "--info" in sys.argv:
        try:
            from pydantic import VERSION as pydantic_version
        except ImportError:
            pydantic_version = "Not Install"
        try:
            from grpc import __version__ as grpc_version
        except ImportError:
            grpc_version = "Not Install"
        try:
            from mypy_protobuf.main import __version__ as mypy_protobuf_version
        except ImportError:
            mypy_protobuf_version = "Not Install"
        try:
            from lark import __version__ as lark_version
        except ImportError:
            lark_version = "Not Install"
        try:
            from toml import __version__ as toml_version  # type: ignore
        except ImportError:
            toml_version = "Not Install"

        try:
            from black import __version__ as black_version
        except ImportError:
            black_version = "Not Install"
        try:
            from isort import __version__ as isort_version
        except ImportError:
            isort_version = "Not Install"
        try:
            from autoflake import __version__ as autoflake_version
        except ImportError:
            autoflake_version = "Not Install"

        print()
        print()
        print("current working directory: " + os.getcwd())
        print("sys path: " + "\n    -".join([""] + sys.path))
        print("executable: " + str(sys.executable))
        print("python version: " + str(sys.version_info))
        print()
        print("############# dependencies ############## ")
        print("    grpc:            " + grpc_version)
        print("    pydantic:        " + pydantic_version)
        print()
        print("########## Expand dependencies ########## ")
        print("    mypy-protobuf:   " + mypy_protobuf_version)
        print("    lark:            " + lark_version)
        print("    toml:            " + toml_version)
        print()
        print("########## Format dependencies ########## ")
        print("    autoflake:       " + autoflake_version)
        print("    black:           " + black_version)
        print("    isort:           " + isort_version)
        print()
    if "--toml-info" in sys.argv:
        print("######### pyproject.toml Content ######### ")
        try:
            from protobuf_to_pydantic.util import get_pyproject_content

            print(get_pyproject_content(""))
        except Exception:
            print("    Not Load pyproject.toml")
        print()

    sys.exit(0)
