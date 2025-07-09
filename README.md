## Set up

* Install `retrying` at `1.3.4` and `1.3.6` in the `.venv-1.3.4` and 
`.venv-1.3.6` virtual environments respectively.

```bash
. setup.bash
```

## Run the benchmark for both versions

```bash 
./benchmark.sh
```

## Running the demo directly

Ensure you have activated the appropriate virtual environment before running 
the example script.

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

BENCHMARK RESULTS: Duration(2.002s) Total Calls(2,302) Calls/sec(1149.95)
BENCHMARK RESULTS: Duration(2.003s) Total Calls(2,489) Calls/sec(1242.45)
BENCHMARK RESULTS: Duration(2.007s) Total Calls(2,309) Calls/sec(1150.65)
BENCHMARK RESULTS: Duration(2.001s) Total Calls(2,441) Calls/sec(1219.99)
BENCHMARK RESULTS: Duration(2.005s) Total Calls(2,527) Calls/sec(1260.34)
BENCHMARK RESULTS: Duration(2.001s) Total Calls(2,389) Calls/sec(1193.98)
BENCHMARK RESULTS: Duration(2.001s) Total Calls(2,452) Calls/sec(1225.49)
BENCHMARK RESULTS: Duration(2.003s) Total Calls(2,340) Calls/sec(1168.34)
BENCHMARK RESULTS: Duration(2.001s) Total Calls(2,311) Calls/sec(1154.97)
BENCHMARK RESULTS: Duration(2.005s) Total Calls(2,414) Calls/sec(1204.23)

--- Testing with retrying 1.3.6 ---
Starting ten 2-second-duration benchmarks of retry...
Press Ctrl+C to stop early if needed

BENCHMARK RESULTS: Duration(2.001s) Total Calls(2,158) Calls/sec(1078.33)
BENCHMARK RESULTS: Duration(2.002s) Total Calls(1,798) Calls/sec(897.91)
BENCHMARK RESULTS: Duration(2.006s) Total Calls(1,952) Calls/sec(973.04)
BENCHMARK RESULTS: Duration(2.008s) Total Calls(1,591) Calls/sec(792.29)
BENCHMARK RESULTS: Duration(2.001s) Total Calls(1,520) Calls/sec(759.58)
BENCHMARK RESULTS: Duration(2.004s) Total Calls(1,389) Calls/sec(693.20)
BENCHMARK RESULTS: Duration(2.008s) Total Calls(1,356) Calls/sec(675.38)
BENCHMARK RESULTS: Duration(2.001s) Total Calls(1,287) Calls/sec(643.25)
BENCHMARK RESULTS: Duration(2.016s) Total Calls(1,289) Calls/sec(639.45)
BENCHMARK RESULTS: Duration(2.003s) Total Calls(1,284) Calls/sec(641.04)
```

Note that the calls/sec of `retrying 1.3.6` is lower and decreases over time, 
while `retrying 1.3.4` maintains a more consistent rate.
There seems to be some action that gets slower with each retry. The benchmark 
runs the ten tests in one process. If you modify the benchmark to run more
tests, the performance just gets worse.

## Other Analysis

* During my investigation, I found that the `self._logger.addHandler()` call
\([introduced here][0]\)
in `retrying 1.3.6` is increasingly slow with each retry, which is likely 
causing the performance degradation.
* In addition to this, though I don't have evidence that this is significant, 
if not given a `logger` argument, it will create a new logger each time, which 
also adds overhead.

[0]: https://github.com/groodt/retrying/pull/6/files#diff-5d48e947cb75f0a64ea964638aee51b9473f649b6fe9de4bd3455aa7b0dae095R118