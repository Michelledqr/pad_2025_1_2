from setuptools import setup, find_packages

setup(
    name="edu_pad",
    version="0.0.1",
    author="Michelle Robinson",
    authon_email="michelle.robinson@est.iudigital.edu.co",
    description="Prog para análisis de datos",
    pymodules=["actividad1","actividad2"],
    install_requires=[
        "pandas",
        "openpyxl",
        "requests",
        "beautifulsoup4"
    ]
)