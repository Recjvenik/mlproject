from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requrements(file_path:str) -> List[str]:

    requirements = []

    with open(file_path, 'rb') as file_obj:
        content = file_obj.read()

    # Try decoding with common encodings until one works
    for encoding in ['utf-8', 'utf-16', 'utf-16-le', 'utf-16-be', 'latin-1']:
        try:
            requirements = content.decode(encoding).splitlines()
            break  # Exit the loop once decoding is successful
        except UnicodeDecodeError:
            continue

    # Remove the '-e .' entry if it exists
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name = "mlproject",
    version = "0.0.1",
    author = "Himanshu",
    author_email = "himiitd96@gmail.com",
    packages = find_packages(),
    install_requires = get_requrements('requirements.txt')
)