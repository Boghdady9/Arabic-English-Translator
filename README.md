# Arabic-English-Translator
 in this project we will build a translator that can translate from Arabic to English and vice versa using the transformer model.
 the translator is based on Helsinki NLP's MarianMT model. the data used to train the model is from [**ymoslem/UN-Arabic-English-Filtered**](https://huggingface.co/datasets/ymoslem/UN-Arabic-English-Filtered)

## Data
[Data used for training the model](https://huggingface.co/datasets/BoghdadyJR/ar-en_cleaned)

## Preprocessing

the data was preprocessed by removing the special characters and the non-arabic numbers are replaced.

[**tnkeeh**](https://github.com/ARBML/tnkeeh) was used to preprocess the arabic text.

## Requirements
`
- gradio
- transformers==4.42.3
- torch==2.2.1
- datasets==2.20.0
- tokenizers==0.19.1
- sentencepiece


## Usage
to use the translator you can open the following link: [Arabic-English-Translator](https://huggingface.co/spaces/BoghdadyJR/Arabic_English_translator)


