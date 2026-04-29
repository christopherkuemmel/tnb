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
from torch.utils.data import DataLoader

from tnb.data.cryptodatarequest import CryptoDataRequest
from tnb.data.loader.cryptocandledataset import CryptoCandleDataset


def download_crypto_data():
    cdr = CryptoDataRequest()
    print("Download from FTX")
    cdr.request('BTC/USDT', 'ftx', 1495032490, 1652798890, file_path='ftx.csv')
    print("Download from POLONIEX")
    cdr.request('BTC_USDT',
                'poloniex',
                1495032490,
                1652798890,
                file_path='poloniex.csv')
    print("Done!")


def crypto_candle_dataloader():

    crypto_data = pd.read_csv('data/poloniex.csv')

    loader_params = {
        'batch_size': 1,
        'shuffle': False,
    }
    mapping = ['open', 'high', 'low', 'close', 'amount']
    # define dataset
    ccd = CryptoCandleDataset(crypto_data, 50, mapping)
    train_loader = DataLoader(ccd, **loader_params)

    for step, batch in enumerate(train_loader):
        print(f'Step: {step} - Batch: {batch}')


if __name__ == '__main__':
    # download_crypto_data()
    crypto_candle_dataloader()
