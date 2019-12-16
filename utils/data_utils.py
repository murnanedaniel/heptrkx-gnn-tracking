"""
This file contains some common helper code for the analysis notebooks.
"""

# System
import os
import yaml
import pickle
from collections import namedtuple

# Externals
import numpy as np
import pandas as pd
import torch
from torch.utils.data import Subset, DataLoader

# Locals
import datasets.hitgraphs
from torch_geometric.data import Batch
from datasets.hitgraphs_sparse import HitGraphDataset

#------------------------------------------------------------------------------

def get_output_dir(config):
    return os.path.expandvars(config['output_dir'])

def get_input_dir(config):
    return os.path.expandvars(config['data']['input_dir'])

def load_config_dir(result_dir):
    """Load pickled config saved in a result directory"""
    config_file = os.path.join(result_dir, 'config.pkl')
    with open(config_file, 'rb') as f:
        return pickle.load(f)
    
def load_summaries(config):
    summary_file = os.path.join(get_output_dir(config), 'summaries_0.csv')
    return pd.read_csv(summary_file)

def get_dataset(config):
    return HitGraphDataset(get_input_dir(config))

def get_data_loader(config, n_tasks, task):
    # Take the test set from the back
    full_dataset = get_dataset(config)
    full_indices = torch.arange(len(full_dataset))
    sub_indices = np.array_split(full_indices,n_tasks)[task]
    sub_dataset = Subset(full_dataset, sub_indices)
    return DataLoader(sub_dataset, batch_size=1, collate_fn=Batch.from_data_list), sub_indices.numpy()