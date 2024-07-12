curl -X POST https://api.example.com/verify_telegram \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your_api_token" \
  -d '{
        "telegram_id": "your_telegram_id",
        "code": "your_verification_code"
      }'
