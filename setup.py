from setuptools import find_packages, setup

setup(
    name="rkv",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "lmcache.token_drop_algorithms": [
            "rkv=rkv:build_r1kv_serving_algorithm",
        ],
    },
)
