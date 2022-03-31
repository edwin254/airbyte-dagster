import setuptools

setuptools.setup(
    name="app",
    packages=setuptools.find_packages(exclude=["app_tests"]),
    install_requires=[
        "dagster==0.14.6",
        "dagit==0.14.6",
        "pytest",
    ],
)
