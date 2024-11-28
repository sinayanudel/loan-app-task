curl -X POST "http://<load_balancer_dns>/loans/" -H "Content-Type: application/json" -d '{
  "amount": 100000,
  "interest_rate": 5.5,
  "term_months": 360
}'