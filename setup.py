import setuptools


# Function to load requirements from requirements.txt
def load_requirements(filename="requirements.txt"):
    with open(filename, "r") as file:
        requirements = file.readlines()
        requirements = [
            req.strip()
            for req in requirements
            if req.strip() and not req.startswith("#")
        ]
        return requirements


setuptools.setup(
    name="professional_secure_ai_bot",
    version="1.0",
    author="Paul Zenker (NSIDE ATTACK LOGIC GmbH) <pzenker@nsideattacklogic.de>",
    description="A demo application that showcases LLM vulnerabilities.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    package_dir={"": "src"},  # Directory where setuptools will look for Python files
    packages=setuptools.find_packages(
        where="src"
    ),  # Automatically find all packages in 'src'
    include_package_data=True,  # Include non-code files specified in MANIFEST.in
    install_requires=load_requirements(),  # Load requirements from requirements.txt
    entry_points={
        "console_scripts": ["secure_ai_bot=professional_secure_ai_bot.main:main"],
    },
    python_requires=">=3.11",
)
