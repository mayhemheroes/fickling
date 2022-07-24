FROM python:3.8-bullseye
RUN pip3 install atheris

COPY . /fickling
WORKDIR /fickling
RUN python3 -m pip install . && chmod +x fuzz/fuzz_pickle_decompiler.py