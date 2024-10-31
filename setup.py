import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("LICENSE", "r", encoding="utf-8") as fh:
    license_content = fh.read()

setuptools.setup(
    name="ceo-alfred",
    version='0.0.1-beta',
    author="vortezwohl",
    author_email="vortez.wohl@gmail.com",
    description="Alfred is an assistant in your shell.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license=license_content,
    url="https://github.com/vortezwohl/CEO-Alfred-TheProcessManager",
    project_urls={
        "Bug Tracker": "https://github.com/vortezwohl/CEO-Alfred-TheProcessManager/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Natural Language :: English",
    ],
    package_dir={"": "."},
    packages=setuptools.find_packages(where="."),
    python_requires=">=3.10",
    install_requires=[
        'langchain-core>=0.3.13',
        'langchain-openai>=0.2.3'
    ],
    entry_points={},
    include_package_data=False
)