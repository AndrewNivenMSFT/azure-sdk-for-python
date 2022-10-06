# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import Baseline
from ._models_py3 import BaselineAdjustedResult
from ._models_py3 import BenchmarkReference
from ._models_py3 import CloudErrorBody
from ._models_py3 import ErrorAdditionalInfo
from ._models_py3 import QueryCheck
from ._models_py3 import Remediation
from ._models_py3 import Resource
from ._models_py3 import RuleResults
from ._models_py3 import RuleResultsInput
from ._models_py3 import RuleResultsProperties
from ._models_py3 import RulesResults
from ._models_py3 import RulesResultsInput
from ._models_py3 import Scan
from ._models_py3 import ScanProperties
from ._models_py3 import ScanResult
from ._models_py3 import ScanResultProperties
from ._models_py3 import ScanResults
from ._models_py3 import Scans
from ._models_py3 import VaRule

from ._security_center_enums import RuleSeverity
from ._security_center_enums import RuleStatus
from ._security_center_enums import RuleType
from ._security_center_enums import ScanState
from ._security_center_enums import ScanTriggerType
from ._patch import __all__ as _patch_all
from ._patch import *  # type: ignore # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "Baseline",
    "BaselineAdjustedResult",
    "BenchmarkReference",
    "CloudErrorBody",
    "ErrorAdditionalInfo",
    "QueryCheck",
    "Remediation",
    "Resource",
    "RuleResults",
    "RuleResultsInput",
    "RuleResultsProperties",
    "RulesResults",
    "RulesResultsInput",
    "Scan",
    "ScanProperties",
    "ScanResult",
    "ScanResultProperties",
    "ScanResults",
    "Scans",
    "VaRule",
    "RuleSeverity",
    "RuleStatus",
    "RuleType",
    "ScanState",
    "ScanTriggerType",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()