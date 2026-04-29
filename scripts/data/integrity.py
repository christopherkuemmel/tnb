# -*- coding: utf-8 -*-
# Copyright 2022 Christopher Kümmel
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

import pandas as pd


def main():
    print("FTX")
    crypto_data = pd.read_csv('data/ftx.csv')

    times = crypto_data['time'].to_list()

    for idx, time in enumerate(zip(times, times[1:])):
        if time[1] - time[0] != 300000:
            print(f"IDX: {idx} - wrong offset")
            print(f"Time: {time} - Diff: {time[1] - time[0]}")

    print("POLONIEX")
    crypto_data = pd.read_csv('data/poloniex.csv')

    times = crypto_data['startTime'].to_list()

    for idx, time in enumerate(zip(times, times[1:])):
        if time[1] - time[0] != 300000:
            print(f"IDX: {idx} - wrong offset")
            print(f"Time: {time} - Diff: {time[1] - time[0]}")


if __name__ == "__main__":
    main()
