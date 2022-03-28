#!/bin/bash
for i in $(seq 1000); do
  echo "hello world" > overloaded_file
done
