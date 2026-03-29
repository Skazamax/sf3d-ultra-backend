from fastapi import FastAPI, UploadFile
import uuid

app = FastAPI()

tasks = {}

@app.post("/generate")
async def generate_model(file: UploadFile):
    task_id = str(uuid.uuid4())
    tasks[task_id] = {"status": "processing", "result": None}

    # Tu później dodamy wywołanie modelu 3D na RunPod GPU
    # Na razie tylko symulacja
    tasks[task_id]["status"] = "done"
    tasks[task_id]["result"] = "model.glb"

    return {"task_id": task_id}

@app.get("/status/{task_id}")
async def get_status(task_id: str):
    return tasks.get(task_id, {"error": "task not found"})

@app.get("/result/{task_id}")
async def get_result(task_id: str):
    task = tasks.get(task_id)
    if not task:
        return {"error": "task not found"}
    return {"result": task["result"]}
