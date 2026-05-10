#!/bin/bash
echo "Generating NEUROPIA results..."
python3 bin/benchmark.py > results/latest_benchmark.txt 2>/dev/null
echo "Results saved to results/latest_benchmark.txt"
