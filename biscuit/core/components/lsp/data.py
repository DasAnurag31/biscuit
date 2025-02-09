from __future__ import annotations

import dataclasses
from typing import List, Optional, Union

import tarts as lsp

# Requests

@dataclasses.dataclass
class CompletionRequest:
    id: int
    cursor: str

@dataclasses.dataclass
class JumpRequest:
    file_path: str
    location: str


# Responses

@dataclasses.dataclass
class Underline:
    start: str
    end: str
    tooltip_text: str
    color: Optional[str] = None

    def __repr__(self) -> str:
        return self.start
    
@dataclasses.dataclass
class Underlines:
    id: str
    underline_list: List[Underline]

@dataclasses.dataclass
class Completion:
    kind: int
    display_text: str
    replace_start: str
    replace_end: str
    replace_text: str
    filter_text: str
    documentation: str
    
    def __repr__(self) -> str:
        return self.replace_text

@dataclasses.dataclass
class Completions:
    id: int
    completions: List[Completion]

@dataclasses.dataclass
class HoverResponse:
    location: str
    text: Optional[list[str, str]]
    docs: Optional[str] = None

    def __repr__(self) -> str:
        return self.text

@dataclasses.dataclass
class JumpLocationRange:
    file_path: str
    start: str
    end: str

    def __repr__(self) -> str:
        return self.file_path

@dataclasses.dataclass
class Jump:
    pos: str
    locations: List[JumpLocationRange]


@dataclasses.dataclass
class TextEdit:
    start: str
    end: str
    new_text: str

    def __repr__(self) -> str:
        return self.file_path

@dataclasses.dataclass
class WorkspaceEdit:
    file_path: str
    edits: list[TextEdit]

    def __repr__(self) -> str:
        return self.file_path

@dataclasses.dataclass
class WorkspaceEdits:
    edits: List[WorkspaceEdit]

