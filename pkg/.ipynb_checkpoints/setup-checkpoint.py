"""A package for bibtex utilities."""

from setuptools import setup

setup(
    name="s23oa",
    version="0.0.1",
    description="OpenAlex utilities",
    maintainer="Kareem Abdelmaqsoud",
    maintainer_email="kabdelma@andrew.cmu.edu",
    license="MIT",
    packages=["s23oa"],
    scripts=[],
    entry_points={'console_scripts': ['s23oa = s23oa.main:main']},
    long_description="""A set of OpenAlex utilities""",
)
