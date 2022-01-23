## Example

![Example Image](graphs/week3.png)

## Requirements

Depends on `conda` and `brew`. Appologies to Windows users.

## Usage

Within the `utils/` folder, build the environment.

```bash
make build-env
```

Test the environment with

```bash
make test-env
```

If the test passes, change the name of `graphs/random-graph.png`.

```bash
mv graphs/random-graph.png graphs/weekX.png
```

After creating the graph, delete the environment with the following command.

```bash
make clean
```

