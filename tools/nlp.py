import transformers
import warnings


def preprocess(content):
    classifier = transformers.pipeline("sentiment-analysis",
                          model="IDEA-CCNL/Erlangshen-Roberta-110M-Sentiment")
    return classifier(content)
print(preprocess("我很棒"))