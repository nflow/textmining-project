#!/bin/sh
mkdir tmp
echo "Creating BOW from Spiege example ..."
python3 ../create_bow.py -s data/spiegel/2000_example.xml > tmp/spiegel_bow.json
echo "Creating BOW from Manifesto example ..."
python3 ../create_bow.py -m data/manifestos/afd_2013.csv -m data/manifestos/cdu_2002.csv > tmp/manifesto_bow.json
echo "Calculate Cosine similarity between Spiegel and Manifesto file ..."
python3 ../cosine_sim.py -s tmp/spiegel_bow.json -m tmp/manifesto_bow.json
echo "Calculate Cosine similarity between Manifesto and Manifesto file ..."
python3 ../cosine_sim.py -m tmp/manifesto_bow.json
