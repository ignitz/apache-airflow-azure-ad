from __future__ import annotations

# [START tutorial]
# [START import_module]
from typing import Any

# The DAG object; we'll need this to instantiate a DAG
from airflow.models.dag import DAG

# [END import_module]

class YuriDAG(DAG):

    def __init__(self, dag_id: str, domain: str, *args: Any, **kwargs: Any):
        print(f"YuriDAG({args}, {kwargs})")
        print(args)

        default_args = kwargs.get("default_args", {})
        default_args["owner"] = domain
        kwargs["default_args"] = default_args
        access_control = {
            domain: {"can_read", "can_edit", "can_delete"},
        }
        kwargs["access_control"] = access_control
        super().__init__(dag_id, *args, **kwargs)