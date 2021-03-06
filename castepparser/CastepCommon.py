# Copyright 2015-2018 Martina Stella, Massimo Riello, Fawzi Mohamed, Ankit Kariryaa
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import numpy as np
from nomadcore.local_meta_info import loadJsonFile, InfoKindEl
from nomadcore.unit_conversion.unit_conversion import convert_unit
import json, os, re

############################################################
# This file contains functions that are needed
# by more than one parser.
############################################################

def get_metaInfo(filePath):
    """Loads metadata.

    Args:
        filePath: Location of metadata.

    Returns:
        metadata which is an object of the class InfoKindEnv in nomadcore.local_meta_info.py.
    """
    metaInfoEnv, warnings = loadJsonFile(filePath = filePath, dependencyLoader = None, extraArgsHandling = InfoKindEl.ADD_EXTRA_ARGS, uri = None)
    return metaInfoEnv