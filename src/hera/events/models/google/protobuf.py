# generated by datamodel-codegen:
#   filename:  https://raw.githubusercontent.com/argoproj/argo-workflows/v3.4.4/api/openapi-spec/swagger.json

from __future__ import annotations

from typing import Optional

from hera.shared._base_model import BaseModel


class Any(BaseModel):
    type_url: Optional[str] = None
    value: Optional[str] = None
