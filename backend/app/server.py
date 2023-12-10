from fastapi import FastAPI
from fastapi.responses import RedirectResponse, JSONResponse
from langchain.chat_models import AzureChatOpenAI, BedrockChat
from langserve import add_routes

AzureGpt35 = AzureChatOpenAI(
    openai_api_version="2023-05-15",
    azure_deployment="gpt-35-turbo",
)

AzureGpt4 = AzureChatOpenAI(
    openai_api_version="2023-05-15",
    azure_deployment="gpt-4",
)

BedrockClaude = BedrockChat(
    credentials_profile_name='genai',
    model_id='anthropic.claude-v2',
    streaming=True,
)

BedrockLlama = BedrockChat(
    credentials_profile_name='genai',
    model_id='meta.llama2-70b-chat-v1',
    streaming=True,
)

app = FastAPI()

@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")

@app.get("/health")
async def health():
    return JSONResponse({"status": "ok"})

add_routes(app, AzureGpt35, path="/azure_gpt35")
add_routes(app, AzureGpt4, path="/azure_gpt4")
add_routes(app, BedrockClaude, path="/bedrock_claude")
add_routes(app, BedrockLlama, path="/bedrock_llama")
