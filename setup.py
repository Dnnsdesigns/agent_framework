from setuptools import setup, find_packages

setup(
    name='agent_framework',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'asyncio',
        'apscheduler',
        'pytest',
        'sqlite3',
    ],
    entry_points={
        'console_scripts': [
            'agent-framework=agent_framework:main',
        ],
    },
)
