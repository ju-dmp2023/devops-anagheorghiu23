import requests

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