# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Geo utility that maps the names of reporting areas in NNDSS to Data Commons
place nodes.
"""

_PLACE_MAP = {
    'Ala.': 'geoId/01',
    'Alabama': 'geoId/01',
    'Alaska': 'geoId/02',
    'Amer. Samoa': 'geoId/60',
    'American Samoa': 'geoId/60',
    'Ariz.': 'geoId/04',
    'Arizona': 'geoId/04',
    'Ark.': 'geoId/05',
    'Arkansas': 'geoId/05',
    'C.N.M.I.': 'geoId/69',
    'Calif.': 'geoId/06',
    'California': 'geoId/06',
    'Colo.': 'geoId/08',
    'Colorado': 'geoId/08',
    'Commonwealth of Northern Mariana Islands': 'geoId/69',
    'Commonwealth of the Northern Mariana Islands': 'geoId/69',
    'Conn.': 'geoId/09',
    'Connecticut': 'geoId/09',
    'D.C.': 'geoId/11',
    'Del.': 'geoId/10',
    'Delaware': 'geoId/10',
    'District of Columbia': 'geoId/11',
    'E.N. CENTRAL': 'usc/EastNorthCentralDivision',
    'E.S. CENTRAL': 'usc/EastSouthCentralDivision',
    'East North Central': 'usc/EastNorthCentralDivision',
    'East South Central': 'usc/EastSouthCentralDivision',
    'Fla.': 'geoId/12',
    'Florida': 'geoId/12',
    'Ga.': 'geoId/13',
    'Georgia': 'geoId/13',
    'Guam': 'geoId/66',
    'Hawaii': 'geoId/15',
    'Idaho': 'geoId/16',
    'Ill.': 'geoId/17',
    'Illinois': 'geoId/17',
    'Ind.': 'geoId/18',
    'Indiana': 'geoId/18',
    'Iowa': 'geoId/19',
    'Kans.': 'geoId/20',
    'Kansas': 'geoId/20',
    'Kentucky': 'geoId/21',
    'Ky.': 'geoId/21',
    'La.': 'geoId/22',
    'Louisiana': 'geoId/22',
    'MID. ATLANTIC': 'usc/MiddleAtlanticDivision',
    'MOUNTAIN': 'usc/MountainDivision',
    'Maine': 'geoId/23',
    'Maryland': 'geoId/24',
    'Mass.': 'geoId/25',
    'Massachusetts': 'geoId/25',
    'Md.': 'geoId/24',
    'Mich.': 'geoId/26',
    'Michigan': 'geoId/26',
    'Middle Atlantic': 'usc/MiddleAtlanticDivision',
    'Minn.': 'geoId/27',
    'Minnesota': 'geoId/27',
    'Miss.': 'geoId/28',
    'Mississippi': 'geoId/28',
    'Missouri': 'geoId/29',
    'Mo.': 'geoId/29',
    'Mont.': 'geoId/30',
    'Montana': 'geoId/30',
    'Mountain': 'usc/MountainDivision',
    'N. Dak.': 'geoId/38',
    'N. Mex.': 'geoId/35',
    'N.C.': 'geoId/37',
    'N.H.': 'geoId/33',
    'N.J.': 'geoId/34',
    #NOTE: It is unclear if Upstate NY is same as geoId/36, hence unresolved
    'N.Y. (Upstate)': '',
    #NOTE: N.Y. City is not resolved to geoId/3651000 since the admin boundaries is unclear
    'N.Y. City': '',
    'NEW ENGLAND': 'usc/NewEnglandDivision',
    'Nebr.': 'geoId/31',
    'Nebraska': 'geoId/31',
    'Nev.': 'geoId/32',
    'Nevada': 'geoId/32',
    'New England': 'usc/NewEnglandDivision',
    'New Hampshire': 'geoId/33',
    'New Jersey': 'geoId/34',
    'New Mexico': 'geoId/35',
    'New York': 'geoId/36',
    #NOTE: This is unresolved since there is no equivalent place within geoId/36
    'New York (excluding New York City)': '',
    #NOTE: N.Y. City is not resolved to geoId/3651000 since the admin boundaries is unclear
    'New York City': '',
    'Non-U.S. Residents': 'country/USA',
    'North Carolina': 'geoId/37',
    'North Dakota': 'geoId/38',
    'Ohio': 'geoId/39',
    'Okla.': 'geoId/40',
    'Oklahoma': 'geoId/40',
    'Oreg.': 'geoId/41',
    'Oregon': 'geoId/41',
    'P.R.': 'geoId/72',
    'PACIFIC': 'usc/PacificDivision',
    'Pa.': 'geoId/42',
    'Pacific': 'usc/PacificDivision',
    'Pennsylvania': 'geoId/42',
    'Puerto Rico': 'geoId/72',
    'R.I.': 'geoId/44',
    'Republic of Palau': 'country/PLW',
    'Republic of the Marshall Islands': 'country/MHL',
    'Rhode Island': 'geoId/44',
    'S. ATLANTIC': 'usc/SouthAtlanticDivision',
    'S. Dak.': 'geoId/46',
    'S.C.': 'geoId/45',
    'South Atlantic': 'usc/SouthAtlanticDivision',
    'South Carolina': 'geoId/45',
    'South Dakota': 'geoId/46',
    'Tenn.': 'geoId/47',
    'Tennessee': 'geoId/47',
    'Tex.': 'geoId/48',
    'Texas': 'geoId/48',
    'U.S. Residents': 'country/USA',
    'U.S. Residents, excluding U.S. Territories': 'country/USA',
    'U.S. Territories': '',
    'U.S. Virgin Islands': 'geoId/78',
    'UNITED STATES': 'country/USA',
    'US Virgin Islands': 'geoId/78',
    'United States': 'country/USA',
    'Utah': 'geoId/49',
    'V.I.': 'geoId/78',
    'Va.': 'geoId/51',
    'Vermont': 'geoId/50',
    'Virginia': 'geoId/51',
    'Vt.': 'geoId/50',
    'W. Va.': 'geoId/54',
    'W.N. CENTRAL': 'usc/WestNorthCentralDivision',
    'W.S. CENTRAL': 'usc/WestSouthCentralDivision',
    'Wash.': 'geoId/53',
    'Washington': 'geoId/53',
    'Washington DC': 'geoId/11001',
    'West North Central': 'usc/WestNorthCentralDivision',
    'West South Central': 'usc/WestSouthCentralDivision',
    'West Virginia': 'geoId/54',
    'Wis.': 'geoId/55',
    'Wisconsin': 'geoId/55',
    'Wyo.': 'geoId/56',
    'Wyoming': 'geoId/56'
}


def get_place_dcid(place_name: str) -> str:
    """
  Utility wrapper that returns the place dcid given a name
  """
    return _PLACE_MAP.get(place_name, '')
