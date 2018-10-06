from torch.utils.data import Dataset


class CodeSearchDataset(Dataset):

    def __init__(self, original_data):
        pass

    def __len(self):
        return len(self.items)

    def __getitem__(self, idx):
        return self.items[idx]
