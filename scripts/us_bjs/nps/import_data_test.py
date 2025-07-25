# Copyright 2020 Google LLC
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

import os
import unittest
import pandas as pd
import sys

_SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(_SCRIPT_PATH, '../nps'))
from .import_data import save_csv
from .preprocess_data import preprocess_df


class TestPreprocess(unittest.TestCase):

    def test_preprocess(self):
        module_dir = os.path.dirname(os.path.realpath(__file__))
        input_path = os.path.join(module_dir, "test/test_data.tsv")
        output_path = os.path.join(module_dir, "test/test_data_processed")
        expected_path = os.path.join(module_dir, "test/expected_data.csv")

        input_df = pd.read_csv(input_path, delimiter='\t')
        save_csv(preprocess_df(input_df), output_path)

        # Get the content from the processed file.
        with open(output_path + ".csv", 'r+') as actual_f:
            actual: str = actual_f.read()

        # Get the content of the expected output.
        with open(expected_path, 'r+') as expected_f:
            expected: str = expected_f.read()

        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
