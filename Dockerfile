FROM python:3.9
WORKDIR /code
# ADD setup.py .
# RUN python setup.py build
# RUN python setup.py install
RUN python -m venv .
COPY . .
RUN pip install --editable .
CMD [ "mbot"]
