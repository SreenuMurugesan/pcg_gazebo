# Copyright (c) 2019 - The Procedural Generation for Gazebo authors
# For information on the respective copyright owner see the NOTICE file
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


class Constraint(object):
    """Abstract constraint class.

    > *Attributes*

    * `LABEL` (*type:* `str`): Name of the constraint class.
    """
    _LABEL = None

    def __init__(self):
        """Class constructor."""

    def __eq__(self, other):
        return self._LABEL != other._LABEL

    def __ne__(self, other):
        result = self.__eq__(other)
        return not result

    @property
    def type(self):
        return self._LABEL
