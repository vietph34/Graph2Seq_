# Graph2Seq_
This is a re-implementation of [Graph2Seq](https://arxiv.org/pdf/1804.00823.pdf)

The data is for the Shortest Path Task whose goal is to find the shortest directed path between two nodes in a graph.

| Model      | Results |
| ----------- | ----------- |
| Paper      | 100%   ??    |
| Author's checkpoint   | 97.7% ??       |
|This version |37.6%|

There are some problems with the producability of the [original code](https://github.com/IBM/Graph2Seq), as the author say that it may because the difference of Python version and TF. 

I even use their model checkpoint but got only **1.9%** accuracy on testset.
