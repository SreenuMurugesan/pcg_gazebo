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

from ..types import XMLBase
from .point import Point
from .height import Height


class Polyline(XMLBase):
    _NAME = 'polyline'
    _TYPE = 'sdf'

    _CHILDREN_CREATORS = dict(
        point=dict(creator=Point, n_elems='+', optional=True),
        height=dict(creator=Height, default=[1])
    )

    def __init__(self):
        super(Polyline, self).__init__()
        self.reset()

    @property
    def height(self):
        return self._get_child_element('height')

    @height.setter
    def height(self, value):
        self._add_child_element('height', value)

    @property
    def points(self):
        return self._get_child_element('point')

    def add_point(self, name=None, point=None):
        if point is None:
            point = Point()
        self._add_child_element('point', point)
