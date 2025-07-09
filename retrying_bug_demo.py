import random
import time

import retrying

foo = "bar"  # static data to reduce noise in results

# Global counter for benchmarking
total_calls = 0

@retrying.retry(
    retry_on_result=lambda result: result is None,
    stop_max_attempt_number=30000,  # Don't raise an exception
    wait_fixed=1
)
def fetch_user_data():
    """
    Example using retry_on_result instead of retry_on_exception
    Retries when the result is None
    """
    global total_calls
    total_calls += 1

    # Simulate sometimes returning None (triggering retry)
    if random.random() < 0.4:
        return foo
    else:
        return None

def benchmark_retries(duration_seconds=5):
    """
    Benchmark retry throughput for specified duration

    Args:
        duration_seconds: How long to run the benchmark
    """
    global total_calls

    # Reset counters
    total_calls = 0

    start_time = time.time()
    end_time = start_time + duration_seconds

    try:
        while time.time() < end_time:
            _ = fetch_user_data()
    except KeyboardInterrupt:
        print("\nBenchmark interrupted by user")

    actual_duration = time.time() - start_time

    # Calculate metrics
    calls_per_second = total_calls / actual_duration

    # Display results
    print(f"BENCHMARK RESULTS: Duration({actual_duration:.3f}s) Total Calls({total_calls:,}) Calls/sec({calls_per_second:.2f})")

def main():
    print(f"Starting ten 2-second-duration benchmarks of retry...")
    print("Press Ctrl+C to stop early if needed\n")

    for i in range(10):
        benchmark_retries(duration_seconds=2)

if __name__ == "__main__":
    main()
