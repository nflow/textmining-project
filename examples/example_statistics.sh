#!/bin/sh
mkdir tmp
echo "Creating sentence list from Manifesto example ..."
python3 ../data_io.py -m data/manifestos/cdu_2002.csv --output-file-manifesto tmp/cdu_2002.json
echo "Gather facts from Manifesto ..."
python3 ../statistics.py -m tmp/cdu_2002.json
