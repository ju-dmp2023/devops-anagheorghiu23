FROM python:3.12-alpine
COPY . .
RUN pip install -r requirements.txt
# COPY calculator_helper.py /
# COPY calculator_rest_service.py /
#CMD python calculator.py
ENTRYPOINT [ "python", "calculator.py" ]