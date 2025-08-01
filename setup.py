import platform
from pathlib import Path

# Available at setup time due to pyproject.toml
from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup

_DIR = Path(__file__).parent
_ESPEAK_DIR = _DIR / "piper_phonemize"

__version__ = "1.2.0"

ext_modules = [
    Pybind11Extension(
        "piper_phonemize_cpp",
        [
            "src/python.cpp",
            "src/phonemize.cpp",
            "src/phoneme_ids.cpp",
            "src/tashkeel.cpp",
        ],
        define_macros=[("VERSION_INFO", __version__)],
        include_dirs=[str(_ESPEAK_DIR / "include")],
        library_dirs=[str(_ESPEAK_DIR / "lib")],
        libraries=["espeak-ng", "onnxruntime"],
        extra_link_args=[
            "-Wl,-rpath,$ORIGIN/piper_phonemize/lib"
        ]
    ),
]

setup(
    name="piper_phonemize",
    version=__version__,
    author="Michael Hansen",
    author_email="mike@rhasspy.org",
    url="https://github.com/rhasspy/piper-phonemize",
    description="Phonemization libary used by Piper text to speech system",
    long_description="",
    packages=["piper_phonemize"],
    package_data={
        "piper_phonemize": [
            str(p) for p in (_ESPEAK_DIR / "share" / "espeak-ng-data").rglob("*")
        ]
        + [str(_DIR / "etc" / "libtashkeel_model.ort")]
        + [str(_ESPEAK_DIR / "lib" / "libespeak-ng.so.1")]
        + [str(_ESPEAK_DIR / "lib" / "libonnxruntime.so.1.14.1")]
    },
    include_package_data=True,
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
    python_requires=">=3.7",
)
