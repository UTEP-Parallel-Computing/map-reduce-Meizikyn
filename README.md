# Parallel-Computing-MapReduce

### Usage

```sh
./run
```

### Report

- What problems you encountered completing the assignment and how you overcame them:
  No problems related to the assignment itself. It was fun.

- Any problems you weren't able to overcome or any bugs still left in the program:
  Nope.

- About how long it took you to complete the assignment:
  About 6 hours over 2 days.

- Performance measurements (given in seconds) for 1, 2, 4, and 8 threads:
  Can't get a read on this one. Different executions prompt different usage of threads,
  mostly that one thread has finished before another can even start causing it to be
  reused. 4 thread counts results (usually) in only 3 threads doing work, the first one
  doing the work of the fourth (probably disk-read overhead slowing down consecutive
  threads).

- A short analysis of why the program behaves as it does with an increasing number of threads:
  No speed up, for reason described above.
- Any observations or comments you had while doing the assignment:
  This :banana: is a banana.

- Output from the cpuInfoDump.sh program:
  ```
  model name: Intel(R) Core(TM) i5-2520M CPU @ 2.50GHz
  4 36 216
  ```
