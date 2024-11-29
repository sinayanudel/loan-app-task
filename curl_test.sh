curl http://127.0.0.1:8000/health

###

curl "http://127.0.0.1:8000/loans/2" 

###

curl -X POST "http://127.0.0.1:8000/loans/" -H "Content-Type: application/json" -d '{
  "amount": 500000,
  "interest_rate": 5.5,
  "term_months": 360
}'

###

curl -X PUT "http://127.0.0.1:8000/loans/1" -H "Content-Type: application/json" -d '{
  "amount": 100000,
  "interest_rate": 6.5,
  "term_months": 400
}'

###

curl -X DELETE "http://127.0.0.1:8000/loans/1"