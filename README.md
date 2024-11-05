# LT2326-Project

This project is for the course LT2326  (Gothenburg University).
OpenNMT-py was used for creating a machine translation model with Transformer architecture.
There is a configuration file with the hyperparameters used for training the model.
There is also a file with the data. 
In the sub20_model..txt are the models applied to train,test and validation datasets for the sudword tokenization. Later on the vocabularies where generated. This code can be found on subword.ipynb
For splitting the data run: python3 splitting_train_test_valid.py
There are also two python scripts for counting the enaglish and greek words on each datasets, but also in total.
To run those scripts use: python3 counting_words_en/grc.py   

To use OpenNMT-py (pytorch) first it needs to be installed:   pip install OpenNMT-py

To train the model: onmt_train -config config.yaml
To generate translation: onmt_translate -model path/to/model.pt -src /path/to/test_data.txt -output path/to/translation.txt -gpu 0 -verbose

Here because we use the test data with subword tokenization (because the model is trained with the subworded data), the resulting translation will also be subworded.
Extra step to detokenize the translation:  sed -r 's/(@@ )|(@@ ?$)//g' path/to/generated_transl.txt > path/to/detok_gener_transl.txt

For counting the BLEU score run: python3 compute-bleu.py reference_test.txt generated_transl.txt
For counting the METEOR score run the jupyter notebook Meteor.ipynb