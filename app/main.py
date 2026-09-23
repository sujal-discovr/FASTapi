from fastapi import FastAPI
from app.models import AskRequest

app = FastAPI(title="Grounded Knowledge API")

@app.get("/health")
def health() -> dict:
    return {"status": "ok"}

@app.post("/ask")
def ask(request: AskRequest) -> dict:
    # TODO: Implement the task described in README.md.
    # Hint: import retrieve_documents from app.retriever.
    raise NotImplementedError("Implement POST /ask")
