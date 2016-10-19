#!/bin/sh
mkdir tmp
echo "Creating BOW from Spiege example ..."
python3 ../create_bow.py -s data/spiegel/2000_example.xml > tmp/spiegel_bow.json
echo "Creating BOW from Manifesto example ..."
python3 ../create_bow.py -m data/manifestos/afd_2013.csv -m data/manifestos/cdu_2002.csv > tmp/manifesto_bow.json
echo "Create tf json file from Manifesto ..."
python3 ../tf_idf.py tf -m tmp/manifesto_bow.json -o tmp/tf_manifesto.json
echo "Create tf json file from Spiegel ..."
python3 ../tf_idf.py tf -s tmp/spiegel_bow.json -o tmp/tf_spiegel.json
echo "Create token-mapping ..."
python3 ../tf_idf.py token-mapping -m tmp/manifesto_bow.json -s tmp/spiegel_bow.json -o tmp/token_mapping.json
echo "Create idf json file from all documents ..."
python3 ../tf_idf.py idf --token-mapping tmp/token_mapping.json -o tmp/idf_all.json
echo "Calculate tf-idf and create json file for Manifesto ..."
python3 ../tf_idf.py tfidf --tf-manifesto=tmp/tf_manifesto.json --idf tmp/idf_all.json -o tmp/manifesto_tfidf.json
echo "Calculate tf-idf and create json file for Spiegel ..."
python3 ../tf_idf.py tfidf --tf-spiegel=tmp/tf_spiegel.json --idf tmp/idf_all.json -o tmp/spiegel_tfidf.json
echo "Calculate Cosine similarity between Spiegel and Manifesto file ..."
python3 ../cosine_sim.py -s tmp/spiegel_tfidf.json -m tmp/manifesto_tfidf.json --tfidf
echo "Calculate Cosine similarity between Manifesto and Manifesto file ..."
python3 ../cosine_sim.py -m tmp/manifesto_tfidf.json --tfidf
