from typing import TypedDict, List, Literal, Optional

class State(TypedDict):
    url: str
    main_page_text: str
    company_description: Optional[str]
    queries: List[str]
    targets: List[str]
    search_answers: List[dict]
    answers: List[str]