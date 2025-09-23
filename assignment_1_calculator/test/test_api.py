import requests

class TestCalculatorAPI():
    def test_add_api(self):
        url="http://localhost:5001/#/actions/calculate"
        payload={
             "operation": "add",
             "operand1": 0,
             "operand2": 0   
        }
        requests.post(url, json=payload)
     
