# Copyright 2021 Google LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from temporian.implementation.numpy.operators.arithmetic.base import (
    BaseArithmeticNumpyImplementation,
)
from temporian.core.operators.arithmetic import DivisionOperator
from temporian.implementation.numpy import implementation_lib


class DivisionNumpyImplementation(BaseArithmeticNumpyImplementation):
    """Actual numpy implementation to divide first event by the second one"""

    def __init__(self, operator: DivisionOperator) -> None:
        super().__init__(operator)

    def _do_operation(self, event_1_data, event_2_data):
        return (event_1_data / event_2_data).astype(event_1_data.dtype)


implementation_lib.register_operator_implementation(
    DivisionOperator, DivisionNumpyImplementation
)
