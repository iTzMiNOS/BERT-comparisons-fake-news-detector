# BERT Comparisons for Fake News Detection

This project compares the performance of three BERT variants — **DistilBERT**, **MobileBERT**, and **TinyBERT** — for detecting fake news. Each model has been fine-tuned on a custom dataset containing approximately 50% fake and 50% reliable news articles.

## Table of Contents
- [Installation](#installation)
- [Dataset](#dataset)
- [Models](#models)
- [Results](#results)
- [Usage](#usage)
- [Demo](#demo)
- [License](#license)

## Installation

To run this project locally, clone the repository and install the required dependencies:
```
git clone https://github.com/yourusername/BERT-comparisons-fake-news-detector.git
cd BERT-comparisons-fake-news-detector
pip install -r requirements.txt
```

Ensure you have Python 3.7+ installed, as well as any necessary dependencies for Streamlit and the Hugging Face transformers library.

## Dataset

The dataset used in this project consists of news articles labeled as either fake or reliable. The dataset contains approximately 50% fake news articles and 50% reliable news articles.

- Fake News: 50% of the dataset.
- Reliable News: 50% of the dataset.

Each article was preprocessed to clean the text before being used to train the models.

## Models

This project leverages three BERT variants, each fine-tuned on the dataset:

- **DistilBERT**: A smaller, faster variant of BERT, offering a good trade-off between speed and performance.
- **MobileBERT**: A mobile-optimized version of BERT, designed to run efficiently on mobile devices with limited computational resources.
- **TinyBERT**: An even more compact version of BERT, tailored for latency-sensitive applications with minimal resources.

The models are trained to classify news articles as either fake or reliable.

## Demo

You can try out the demo of this project by visiting the following link:

[Fake News Detection](#)

The demo allows you to input news articles and see how the models classify them as either fake or reliable.

## License

This project is licensed under the MIT License — see the LICENSE file for details.
