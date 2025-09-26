import requests
from calculator_client_generated.calculator_client import Client

from calculator_client_generated.calculator_client.api.actions.calculate import sync
from calculator_client_generated.calculator_client.models.calculation import Calculation
from calculator_client_generated.calculator_client.api.actions import calculate
from calculator_client_generated.calculator_client.models.opertions import Opertions
from calculator_client_generated.calculator_client.models import ResultResponse
import pytest
    

class TestCalculatorAPI():
    def test_add_api(self):
        url="http://localhost:5001/calculate"
        payload={
            "operation": "add",
            "operand1": 10,
            "operand2": 10
            } 
        response = requests.post(url, json=payload)
        
        assert response.status_code == 200
        result = response.json()
        assert result["result"] == 20
   
   
    def test_generated_code(self):
        client = Client(base_url="http://localhost:5001")
        response=calculate.sync(client=client,body=Calculation(Opertions.SUBTRACT,operand1 = 10,operand2 = 2))
        assert isinstance (response, ResultResponse)
        assert response.result == 8