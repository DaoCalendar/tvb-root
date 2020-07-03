# -*- coding: utf-8 -*-
#
#
#  TheVirtualBrain-Contributors Package. This package holds simulator extensions.
#  See also http://www.thevirtualbrain.org
#
# (c) 2012-2020, Baycrest Centre for Geriatric Care ("Baycrest") and others
#
# This program is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software Foundation,
# either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE.  See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this
# program.  If not, see <http://www.gnu.org/licenses/>.
#
#
#   CITATION:
# When using The Virtual Brain for scientific publications, please cite it as follows:
#
#   Paula Sanz Leon, Stuart A. Knock, M. Marmaduke Woodman, Lia Domide,
#   Jochen Mersmann, Anthony R. McIntosh, Viktor Jirsa (2013)
#       The Virtual Brain: a simulator of primate brain network dynamics.
#   Frontiers in Neuroinformatics (7:10. doi: 10.3389/fninf.2013.00010)
#
#

"""
.. moduleauthor:: Dionysios Perdikis <Denis@tvb.invalid>
"""

from tvb.contrib.scripts.datatypes.base import BaseModel
from tvb.datatypes.region_mapping import RegionMapping as TVBRegionMapping
from tvb.datatypes.region_mapping import RegionVolumeMapping as TVBRegionVolumeMapping


class RegionMapping(TVBRegionMapping, BaseModel):

    def to_tvb_instance(self, datatype=TVBRegionMapping, **kwargs):
        return super(RegionMapping, self).to_tvb_instance(datatype, **kwargs)


class CorticalRegionMapping(RegionMapping):
    pass


class SubcorticalRegionMapping(RegionMapping):
    pass


class RegionVolumeMapping(TVBRegionVolumeMapping, BaseModel):

    def to_tvb_instance(self, **kwargs):
        return super(RegionVolumeMapping, self).to_tvb_instance(TVBRegionVolumeMapping, **kwargs)