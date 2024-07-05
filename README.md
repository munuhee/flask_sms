# Flask App with Africa's Talking Integration

Demonstration of a simple Flask application that integrates with Africa's Talking API to send SMS messages.

## Prerequisites

- Python
- Africa's Talking account with API key

## Example Request

Send a POST request to `/send_sms` endpoint with JSON data:

```json
{
    "phone_number": "+254712345678",
    "message": "Hello"
}
```

## Example Response

Successful response from Africa's Talking API:

```json
{
    "response": {
        "SMSMessageData": {
            "Message": "Sent to 1/1 Total Cost: KES 0.8000 Message parts: 1",
            "Recipients": [
                {
                    "cost": "KES 0.8000",
                    "messageId": "ATXid_b2b536b6e5ef4de2132f7c85f66b796f",
                    "number": "+254712345678",
                    "status": "Success",
                    "statusCode": 101
                }
            ]
        }
    }
}
```
