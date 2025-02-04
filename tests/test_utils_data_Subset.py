# Copyright (c) 2023 PaddlePaddle Authors. All Rights Reserved.
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

import textwrap

from apibase import APIBase

obj = APIBase("torch.utils.data.Subset")


def test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torch
        from torch.utils.data import Dataset, Subset
        class MyDataset(Dataset):
            def __init__(self, size=10):
                super(Dataset).__init__()
                self.data = list(range(size))

            def __getitem__(self, idx):
                return self.data[idx]

            def __len__(self):
                return len(self.data)

        dataset = Subset(MyDataset(10),[1, 2, 3, 4, 5, 6])
        result = []
        for d in dataset:
            result.append(d)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_2():
    pytorch_code = textwrap.dedent(
        """
        import torch
        from torch.utils.data import Dataset, Subset
        class MyDataset(Dataset):
            def __init__(self, size=10):
                super(Dataset).__init__()
                self.data = list(range(size))

            def __getitem__(self, idx):
                return self.data[idx]

            def __len__(self):
                return len(self.data)

        dataset = Subset(MyDataset(10),[9, 1])
        result = []
        for d in dataset:
            result.append(d)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_3():
    pytorch_code = textwrap.dedent(
        """
        import torch
        from torch.utils.data import Dataset, Subset
        class MyDataset(Dataset):
            def __init__(self, size=10):
                super(Dataset).__init__()
                self.data = list(range(size))

            def __getitem__(self, idx):
                return self.data[idx]

            def __len__(self):
                return len(self.data)

        dataset = Subset(MyDataset(10),[9, 1, 3])
        result = []
        for d in dataset:
            result.append(d)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_4():
    pytorch_code = textwrap.dedent(
        """
        import torch
        from torch.utils.data import Dataset, Subset
        class MyDataset(Dataset):
            def __init__(self, size=10):
                super(Dataset).__init__()
                self.data = list(range(size))

            def __getitem__(self, idx):
                return self.data[idx]

            def __len__(self):
                return len(self.data)
        data = MyDataset(10)
        indices = [9, 1, 3]
        dataset = Subset(data, indices)
        result = []
        for d in dataset:
            result.append(d)
        """
    )
    obj.run(pytorch_code, ["result"])
