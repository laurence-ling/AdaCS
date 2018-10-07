from torch.utils.data import Dataset


class CodeSearchDataset(Dataset):

    def __init__(self, original_data):
        self.core_term_size = 0
        self.query_max_size = 0
        self.samples = []
        pass

    def __len__(self):
        return len(self.items)

    def __getitem__(self, idx):
        return self.items[idx]
