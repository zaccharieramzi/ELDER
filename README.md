# ELDER experiments

The original readme can still be read [here](original_readme.md).

## Requirements
In order to run this code you need a Python installation with version at least 3.9.
You can then install the requirements using the following command:

```
pip install .
```

## Reproducing Fig. G.4 of the paper
In order to reproduce Fig. G.4 of the paper you will need to download the [model weights](https://drive.google.com/drive/folders/1Q1DTyWffT6dGEaLMO3qa2l4U5QVaNVeG?usp=sharing) for each of the experiments.
These weights come from the original work that introduced ELDER.

Once downloaded, place them into `./ckpts`.

Then you can run the following command to reproduce the results for ELDER:

```
python elder/tune.py data_fidality=sr_test_x3 regularization=elder exp.output_every_step=False 'exp.paths.data_path=miscs/CBSD68' 'exp.restore.max_iter=range(20, 200, 20)'
```

And this one for DEQ:
```
python elder/tune.py data_fidality=sr_test_x3 regularization=deq exp.output_every_step=False 'exp.paths.data_path=miscs/CBSD68' 'exp.restore.max_iter=range(20, 200, 20)'
```

To generate the figure use the [`results_n_iter`](common_experiments/results_n_iter.ipynb) notebook.
