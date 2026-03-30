from main import generate_model
import asyncio

def handler(event):
    # RunPod przekazuje dane w event["input"]
    file = event["input"].get("file")

    # Symulacja — normalnie tu byłby upload pliku
    # i wywołanie modelu 3D
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(generate_model(file))

    return {"task_id": result["task_id"]}
