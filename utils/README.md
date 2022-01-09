## Example

![Example Image](graphs/week3.png)

![Example Image](graphs/week4.png)

## Requirements

For installing in existing conda environment.
```
conda install python-igraph pycairo
pip install distinctipy
```

For creating a new conda environment.
```
conda create -n <env_name> python=3.9 python-igraph pycairo
conda activate <env_name>
pip install distinctipy
```


## Usage

After configuring environemnt, run the following command inside `graphs/` with result PNG file as a flag. Then the corresponding file will be created within `utils/graphs/`.

```python
python main.py -n week3
```

From the above example the output file will be in `./utils/graphs/week3.png`.
