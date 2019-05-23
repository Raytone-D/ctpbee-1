import platform
from setuptools import Extension, setup, find_packages


if platform.uname().system == "Windows":
    compiler_flags = [
        "/MP", "/std:c++17",  # standard
        "/O2", "/Ob2", "/Oi", "/Ot", "/Oy", "/GL",  # Optimization
        "/wd4819"  # 936 code page
    ]
    extra_link_args = []
else:
    compiler_flags = [
        "-std=c++17",  # standard
        "-O3",  # Optimization
        "-Wno-delete-incomplete", "-Wno-sign-compare",
    ]
    extra_link_args = ["-lstdc++"]

vnctpmd = Extension(
    "ctpbee.api.ctp.vnctpmd",
    [
        "ctpbee/api/ctp/vnctp/vnctpmd/vnctpmd.cpp",
    ],
    include_dirs=[
        "ctpbee/api/ctp/include",
        "ctpbee/api/ctp/vnctp",
                  ],
    language="c++",
    define_macros=[],
    undef_macros=[],
    library_dirs=["ctpbee/api/ctp/libs", "ctpbee/api/ctp"],
    libraries=["thostmduserapi_se", "thosttraderapi_se", ],
    extra_compile_args=compiler_flags,
    extra_link_args=extra_link_args,
    depends=[],
    runtime_library_dirs=["$ORIGIN"],
)
vnctptd = Extension(
    "ctpbee.api.ctp.vnctptd",
    [
        "ctpbee/api/ctp/vnctp/vnctptd/vnctptd.cpp",
    ],
    include_dirs=[
        "ctpbee/api/ctp/include",
        "ctpbee/api/ctp/vnctp",
                  ],
    define_macros=[],
    undef_macros=[],
    library_dirs=["ctpbee/api/ctp/libs",
                  "ctpbee/api/ctp",
                  ],
    libraries=["thostmduserapi_se", "thosttraderapi_se", ],
    extra_compile_args=compiler_flags,
    extra_link_args=extra_link_args,
    runtime_library_dirs=["$ORIGIN"],
    depends=[],
    language="c++",
)

if platform.system() == "Windows":
    # use pre-built pyd for windows ( support python 3.7 only )
    ext_modules = []
elif platform.system() == "Darwin":
    ext_modules = []
else:
    ext_modules = [vnctptd, vnctpmd]

pkgs = ['ctpbee', 'ctpbee.api', 'ctpbee.context', 'ctpbee.exceptions', 'ctpbee.data_handle', 'ctpbee.ctp', 'ctpbee.event_engine']

print(pkgs)


install_requires = ['flask']
setup(
    name='ctpbee',
    version='0.15',
    description="easy ctp trade and market support",
    author='somewheve',
    author_email='somewheve@gmail.com',
    url='https://github.com/somewheve/ctpbee',
    license="MIT",
    packages=pkgs,
    install_requires=install_requires,
    platforms=["Windows", "Linux", "Mac OS-X"],
    package_dir = {'ctpbee': 'ctpbee'},
    package_data={'ctpbee': ['api/ctp/*',]},
    ext_modules=ext_modules,
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
            ]
      )