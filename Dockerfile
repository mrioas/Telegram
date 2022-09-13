FROM python:3.9
ADD setup.py .
# RUN python setup.py build
# RUN python setup.py install
RUN pip install --editable .
RUN mbot
