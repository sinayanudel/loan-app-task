curl http://127.0.0.1:8000/health

###

curl "http://127.0.0.1:8000/loans/personal/1" 

###

curl -X POST "http://127.0.0.1:8000/loans/personal" -H "Content-Type: application/json" -d '{
  "amount": 500000,
  "interest_rate": 5.5,
  "term_months": 360,
  "purpose": "car"
}'

###

curl -X PUT "http://127.0.0.1:8000/loans/personal/1" -H "Content-Type: application/json" -d '{
  "amount": 100000,
  "interest_rate": 6.5,
  "term_months": 400,
  "purpose": "car"
}'

###

curl -X DELETE "http://127.0.0.1:8000/loans/personal/1"