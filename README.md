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
  1. 1.479s
  2. 1.454s
  3. 0.845s
  4. 0.817s
- A short analysis of why the program behaves as it does with an increasing number of threads:
  Probably some overhead related to storage disk read speed causing threads to finish actual
  processing before the next thread can finish the read.
- Any observations or comments you had while doing the assignment:
  This :banana: is a banana.

- Output from the cpuInfoDump.sh program:
  ```
  model name: Intel(R) Core(TM) i5-2520M CPU @ 2.50GHz
  4 36 216
  ```

# MPI Report

- What problems you encountered completing the assignment and how you overcame them:
  Outlined below.

- Any problems you weren't able to overcome or any bugs still left in the program:
  Same with floyd-warshall, some form of index miscalculation I haven't the time to solve.
  I feel confident my understanding of using MPI's specifics is solid, and my understanding
  of how this aids parallel programming is extremely strong. I just don't seem to understand
  some semantics specific to MPI itself, even if I understand the problem its solving and the
  abstractions underpinning it.

- About how long it took you to complete the assignment:
  About an hour.

- Performance measurements (given in seconds) for 1, 2, 4, and 8 threads:
  Never got it working, so no metrics.

- A short analysis of why the program behaves as it does with an increasing number of threads:
  :shrug:
- Any observations or comments you had while doing the assignment:
  I think the network-based approach is cool, definitely like it more than using a
  python context with autolooping utility functions as it feels like it removes the
  dilemma behind locking. It also feels closer to pythons own multiprocessing library,
  and seems to solve the issue of GIL.
