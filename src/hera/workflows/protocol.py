from typing import Any, Union

from typing_extensions import Protocol, runtime_checkable

from hera.workflows.models import (
    ContainerSetTemplate,
    DAGTemplate,
    ResourceTemplate,
    ScriptTemplate,
    SuspendTemplate,
    Template,
)

TTemplate = Union[
    ContainerSetTemplate,
    DAGTemplate,
    ResourceTemplate,
    ScriptTemplate,
    SuspendTemplate,
    Template,
]


@runtime_checkable
class Templatable(Protocol):
    def _build_template(self) -> TTemplate:
        ...


@runtime_checkable
class Subbable(Protocol):
    def _add_sub(self, node: Any) -> Any:
        ...


@runtime_checkable
class Steppable(Protocol):
    def _build_step(self) -> Any:
        ...