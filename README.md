# FastAPI Task

Implement `POST /ask` in `app/main.py`.

## Requirements

- Accept:

  ```json
  { "question": "..." }
  ```

- Reject blank or missing questions.
- Use `retrieve_documents(question)` from `app/retriever.py`.
- Return:

  ```json
  {
    "answer": "Concise answer based only on retrieved documents",
    "sources": [
      {
        "id": "document-id",
        "title": "Document title",
        "excerpt": "Supporting text"
      }
    ],
    "confidence": 0.0
  }
  ```

- If the best document score is below `0.45`, return:

  ```json
  {
    "answer": "I don't have enough evidence to answer that.",
    "sources": [],
    "confidence": 0.0
  }
  ```

- Do not use documents with a score below `0.45`.
- Add tests for:
  - Successful retrieval
  - Insufficient evidence
  - Blank question
  - Missing question

## Run

```bash
pip install -r requirements.txt
pytest -q
uvicorn app.main:app --reload
```

You may use Claude Code and documentation. Please run the tests and review your final Git diff before finishing.
