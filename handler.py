import runpod
from main import generate_model
import asyncio

async def run_job(event):
    # event["input"] zawiera dane wysłane do /run
    file = event["input"].get("file")

    # wywołujemy Twoją funkcję FastAPI (async)
    result = await generate_model(file)

    return result

runpod.serverless.start({"handler": run_job})
