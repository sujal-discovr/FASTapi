## Candidate task
Implement `POST /ask` in `app/main.py`.

The endpoint must:
1. Accept JSON: `{ "question": "..." }`.
2. Validate that the question is not blank.
3. Use `retrieve_documents(question)` from `app/retriever.py`.
4. Return JSON with exactly these fields:
   - `answer`: a concise answer grounded only in retrieved material.
   - `sources`: a list of zero or more source objects, each with `id`, `title`, and `excerpt`.
   - `confidence`: a float from 0 to 1.
5. If the best retrieval score is below `0.45`, return this exact answer: `I don't have enough evidence to answer that.` with `sources: []`.
6. Never use information from a document whose score is below `0.45`.
7. Add or complete tests for successful retrieval, insufficient evidence, blank input, and a missing JSON field.
8. Keep the implementation local: no external API, no LLM key, and no new database.

## Timebox
45 minutes. You may use Claude Code and documentation. Please narrate major choices, run the tests, and review the final Git diff.

## Run
```bash
python -m venv .venv
# macOS/Linux: source .venv/bin/activate
# Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
pytest -q
```

## Example request
```bash
curl -X POST http://127.0.0.1:8000/ask \
  -H 'Content-Type: application/json' \
  -d '{"question":"How long are support tickets retained?"}'
```

## Interviewer-only follow-up
After the candidate has a working solution, say:

> A user reports a confident answer supported by an irrelevant source. Explain how you would debug whether the fault is in retrieval or answer generation, then implement one small improvement without adding external services.

Do not share this section before the initial task is done.
