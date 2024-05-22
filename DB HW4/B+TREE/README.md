# B+TREE Test code

You can run the B+Tree code by the following command:
in `B+TREE` directory:

```shell
make
./main path/to/instructions.txt
```

You can test the B+Tree by writing the instructions in a text file.

There are three insturctions:

- `p`: Print tree
- `i <key>`: Insert key
- `r <key>`: Remove key

The first line of the instruction file is the degree of the B+Tree.
Rest of the lines are the instructions.

For example:

```text
3
i 3
i 4
r 5
p
```

This instruction will create a B+Tree with degree 3, insert 3 and 4, remove 5, and print the tree.

Refer to `example1.txt` ~ `example4.txt` for examples.
