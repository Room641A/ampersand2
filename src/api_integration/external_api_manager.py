from fastapi import FastAPI, Request, Response

app = FastAPI()

@app.post("/api/messages")
async def handle_message(request: Request):
    # Process the incoming request
    # Generate a response
    response_body = {
        "type": "message",
        "text": "Hello from FastAPI!"
    }
    return Response(content=response_body, media_type="application/json")
