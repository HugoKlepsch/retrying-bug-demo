## Set up

* Install `retrying` at `1.3.4` and `1.3.6` in the `.venv-1.3.4` and `.venv-1.3.6` virtual environments respectively.

```bash
. setup.bash
```

## Run the benchmark for both versions

```bash 
./benchmark.sh
```

## Running the Example

Ensure you have activated the appropriate virtual environment before running the example script.

```bash
python retrying_bug_demo.py
```

## Example output

Ran on my M1 MacBook Pro with Python 3.11.6:

```
$ ./benchmark.sh 
=== Retrying Library Benchmark Comparison ===

--- Testing with retrying 1.3.4 ---
Starting ten 2-second-duration benchmarks of retry...
Press Ctrl+C to stop early if needed

BENCHMARK RESULTS: Duration(2.002s) Total Calls(2,242) Calls/sec(1119.77)
BENCHMARK RESULTS: Duration(2.004s) Total Calls(2,429) Calls/sec(1212.00)
BENCHMARK RESULTS: Duration(2.002s) Total Calls(2,390) Calls/sec(1193.56)
BENCHMARK RESULTS: Duration(2.005s) Total Calls(2,454) Calls/sec(1223.86)
BENCHMARK RESULTS: Duration(2.001s) Total Calls(2,441) Calls/sec(1220.00)
BENCHMARK RESULTS: Duration(2.000s) Total Calls(2,405) Calls/sec(1202.41)
BENCHMARK RESULTS: Duration(2.006s) Total Calls(2,297) Calls/sec(1145.28)
BENCHMARK RESULTS: Duration(2.001s) Total Calls(2,441) Calls/sec(1219.65)
BENCHMARK RESULTS: Duration(2.017s) Total Calls(2,306) Calls/sec(1143.45)
BENCHMARK RESULTS: Duration(2.005s) Total Calls(2,464) Calls/sec(1229.18)

--- Testing with retrying 1.3.6 ---
Starting ten 2-second-duration benchmarks of retry...
Press Ctrl+C to stop early if needed

BENCHMARK RESULTS: Duration(2.008s) Total Calls(2,138) Calls/sec(1064.91)
BENCHMARK RESULTS: Duration(2.000s) Total Calls(1,946) Calls/sec(972.94)
BENCHMARK RESULTS: Duration(2.001s) Total Calls(1,659) Calls/sec(829.25)
BENCHMARK RESULTS: Duration(2.010s) Total Calls(1,607) Calls/sec(799.31)
BENCHMARK RESULTS: Duration(2.003s) Total Calls(1,492) Calls/sec(744.75)
BENCHMARK RESULTS: Duration(2.002s) Total Calls(1,406) Calls/sec(702.13)
BENCHMARK RESULTS: Duration(2.002s) Total Calls(1,355) Calls/sec(676.99)
BENCHMARK RESULTS: Duration(2.011s) Total Calls(1,273) Calls/sec(633.02)
BENCHMARK RESULTS: Duration(2.001s) Total Calls(1,268) Calls/sec(633.73)
BENCHMARK RESULTS: Duration(2.003s) Total Calls(1,557) Calls/sec(777.51)
```

Note that the calls/sec of `retrying 1.3.6` is lower and decreases over time, while `retrying 1.3.4` maintains a more consistent rate.