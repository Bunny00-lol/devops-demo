from fastapi import FastAPI

app = FastAPI(title="DevOps Demo App")


@app.get("/")
def home():
    return {
        "message": "DevOps Demo App is running!",
        "status": "success"
    }


@app.get("/tasks")
def get_tasks():
    return {
        "tasks": [
            "Learn Git",
            "Learn Docker",
            "Learn Kubernetes"
        ]
    }