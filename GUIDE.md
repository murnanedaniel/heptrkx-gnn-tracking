# Experiment Guide

This is a listing of the training and classification experiments run in this directory. We divide these by doublet classification and triplet classification.

## Doublet Training

| Size | Number of Graphs  | Training time  | Dataset dir  | Result dir  |  Notes |
|------|---|---|---|---|---|
|  Large    | 32,768  |  6h13m | /doublet_data/hitgraphs_high_000  | /doublet_results/checkpoints_high/agnn001 |    |
|  Large    | 32,768  |  ??? | /doublet_data/hitgraphs_high_001  | /doublet_results/checkpoints_high/agnn002 |  This dataset contains the features (r, phi, eta)  |
|  Medium    | 2,000  |  31m | /doublet_data/hitgraphs_med_000  |  /doublet_results/agnn03 |  This dataset contains the features (r, phi, z)  |
|  Medium    | 2,000  |   | /doublet_data/hitgraphs_med_001  | /doublet_results/agnn04  |  This dataset contains the features (r, phi, eta) - with a poor eta feature scale  |
|  Medium    | 2,000  |   | /doublet_data/hitgraphs_med_002  | /doublet_results/agnn05  |  This dataset contains the features (r, phi, eta)  |
|  Medium    | 4,000  |   | /doublet_data/hitgraphs_med_002  | /doublet_results/agnn06  |  This dataset contains the features (r, phi, eta)  |
|  Medium    | 3,600  |   | /doublet_data/hitgraphs_med_000  | /doublet_results/agnn07  |    |
|      |   |   |   |   |    |
|      |   |   |   |   |    |


## Triplet Training

| Size | Number of Graphs  | Training time  | Dataset dir  | Result dir  |  Doublet dir |  Notes |
|------|---|---|---|---|---|
|  Large    | 32,768  |  ? | /triplet_data/hitgraphs_high_000  | /triplet_results/checkpoints_med/agnn01 | /doublet_results/checkpoints_high/agnn01  |
|  Medium    | 1,920  |  54m | /triplet_data/hitgraphs_med  | /triplet_results/checkpoints_med/agnn01 |   |
|      | 1,920  |  1h12m | /triplet_data/hitgraphs_med  |  /triplet_results/checkpoints_med/agnn02 |   |
|  Medium    | 3,600  |   | /triplet_data/hitgraphs_med_000  | /triplet_results/checkpoints_med/agnn04 |   |
|      |   |   |   |   |    |
|      |   |   |   |   |    |
|      |   |   |   |   |    |


For future training: There is a strong link between the doublet trained results and the triplet trained results. Therefore the two sets should be closely linked by ID#. 
