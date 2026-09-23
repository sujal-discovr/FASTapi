from dataclasses import dataclass

@dataclass(frozen=True)
class RetrievedDocument:
    id: str
    title: str
    text: str
    score: float

DOCUMENTS = [
    RetrievedDocument(
        id="support-retention",
        title="Support Data Retention Policy",
        text="Customer support tickets are retained for 90 days after they are closed.",
        score=0.0,
    ),
    RetrievedDocument(
        id="security-access",
        title="Access Control Standard",
        text="Production access requires approval from the on-call engineering manager.",
        score=0.0,
    ),
    RetrievedDocument(
        id="remote-work",
        title="Remote Work Guide",
        text="Employees may work remotely up to three days each week with manager approval.",
        score=0.0,
    ),
]

def retrieve_documents(question: str) -> list[RetrievedDocument]:
    """A deliberately small, deterministic retriever for this exercise."""
    q = question.lower()
    results = []
    for document in DOCUMENTS:
        keywords = set((document.title + " " + document.text).lower().replace(".", "").split())
        overlap = len(set(q.replace("?", "").split()) & keywords)
        score = min(0.95, overlap / 3)
        results.append(RetrievedDocument(document.id, document.title, document.text, score))
    return sorted(results, key=lambda doc: doc.score, reverse=True)
