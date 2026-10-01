"""Conservative UVM/SystemVerilog context extraction."""
from __future__ import annotations
from dataclasses import dataclass
import re
from typing import Iterable

@dataclass(frozen=True)
class UVMSequence:
    name: str
    base_class: str | None = None
    source_file: str | None = None

@dataclass(frozen=True)
class UVMComponent:
    name: str
    kind: str
    base_class: str | None = None
    source_file: str | None = None

@dataclass(frozen=True)
class UVMContext:
    sequences: tuple[UVMSequence, ...] = ()
    components: tuple[UVMComponent, ...] = ()
    tests: tuple[str, ...] = ()
    assertions: tuple[str, ...] = ()
    confidence: str = "low"

class UVMContextExtractor:
    _class = re.compile(r"\bclass\s+(\w+)\s+extends\s+([\w:]+)", re.I)
    _assert = re.compile(r"\b(?:assert\s+property|property)\s+(\w+)", re.I)

    def extract(self, text: str, source_file: str | None = None) -> UVMContext:
        sequences, components, tests = [], [], []
        for name, base in self._class.findall(text):
            b = base.lower()
            if "uvm_test" in b:
                tests.append(name)
            elif "uvm_sequence" in b:
                sequences.append(UVMSequence(name, base, source_file))
            elif "uvm_" in b:
                components.append(UVMComponent(name, self._kind(b), base, source_file))
        assertions = tuple(dict.fromkeys(self._assert.findall(text)))
        confidence = "medium" if sequences or components or tests or assertions else "low"
        return UVMContext(tuple(sequences), tuple(components), tuple(tests), assertions, confidence)

    @staticmethod
    def _kind(base: str) -> str:
        for kind in ("driver","monitor","sequencer","agent","env","scoreboard"):
            if kind in base:
                return kind
        return "component"

    def extract_many(self, sources: Iterable[tuple[str, str]]) -> UVMContext:
        all_ctx = [self.extract(text, path) for path, text in sources]
        return UVMContext(
            tuple(x for c in all_ctx for x in c.sequences),
            tuple(x for c in all_ctx for x in c.components),
            tuple(x for c in all_ctx for x in c.tests),
            tuple(x for c in all_ctx for x in c.assertions),
            "medium" if any(c.confidence == "medium" for c in all_ctx) else "low",
        )
