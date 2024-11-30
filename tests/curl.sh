# Load environment variables from .env file
source .env

### health check
curl http://127.0.0.1:8000/health

### GET personal loan by id
curl -u $BASIC_AUTH_USERNAME:$BASIC_AUTH_PASSWORD "http://127.0.0.1:8000/loans/personal/1"

### POST personal loan
curl -X POST "http://127.0.0.1:8000/loans/personal" \
     -u $BASIC_AUTH_USERNAME:$BASIC_AUTH_PASSWORD \
     -H "Content-Type: application/json" \
     -d '{"amount": 500000, "interest_rate": 5.5, "term_months": 360, "purpose": "car"}'

### PUT personal loan
curl -X PUT "http://127.0.0.1:8000/loans/personal/1" \
     -u $BASIC_AUTH_USERNAME:$BASIC_AUTH_PASSWORD \
     -H "Content-Type: application/json" \
     -d '{"amount": 100000, "interest_rate": 6.5, "term_months": 400, "purpose": "car"}'

### DELETE personal loan
curl -X DELETE "http://127.0.0.1:8000/loans/personal/1" -u $BASIC_AUTH_USERNAME:$BASIC_AUTH_PASSWORD

### GET mortgage loan by id
curl -u $BASIC_AUTH_USERNAME:$BASIC_AUTH_PASSWORD "http://127.0.0.1:8000/loans/mortgage/1"

### POST mortgage loan
curl -X POST "http://127.0.0.1:8000/loans/mortgage" \
     -u $BASIC_AUTH_USERNAME:$BASIC_AUTH_PASSWORD \
     -H "Content-Type: application/json" \
     -d '{"amount": 1000000, "interest_rate": 3.5, "term_months": 240, "address": "123 Main St"}'

### PUT mortgage loan
curl -X PUT "http://127.0.0.1:8000/loans/mortgage/1" \
     -u $BASIC_AUTH_USERNAME:$BASIC_AUTH_PASSWORD \
     -H "Content-Type: application/json" \
     -d '{"amount": 1200000, "interest_rate": 4.0, "term_months": 300, "address": "123 Main St"}'

### DELETE mortgage loan
curl -X DELETE "http://127.0.0.1:8000/loans/mortgage/1" -u $BASIC_AUTH_USERNAME:$BASIC_AUTH_PASSWORD