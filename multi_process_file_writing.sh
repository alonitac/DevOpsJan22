#!/bin/bash
for i in $(seq 1000); do
  ./write_to_file_sequentially.sh &
done
