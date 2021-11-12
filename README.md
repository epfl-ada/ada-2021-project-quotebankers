

# Who has a voice in the media? <!-- omit in toc --> 
What kind of people has a voice in the media? What do they need to talk about and how do they need to express themselves? A datastory that aims to draw the typical profile of individuals quoted in the media.

<p align="center">
  <img src="wordcloud-speakers.png" alt="wordcloud" width="650">
  <br>
  <em>Most frequent speakers in 2020 quotations (random sample size: 1'000'0000)</em>
</p>

## Table of Contents <!-- omit in toc -->

- [Abstract](#abstract)
- [Research questions](#research-questions)
- [Additional datasets](#additional-datasets)
- [Methods](#methods)
- [Timeline](#timeline)
- [Milestones](#milestones)
- [Questions for TAs](#questions-for-tas)
  

## Abstract
What a pleasure it is to be listened to… The ability to make your voice heard is a privilege that many cannot afford. Sometimes you can have the feeling that only the loudest are listened to.
Starting from the 2015-2020 Quotebank dataset, which precisely gathers speaker-attributed quotations from various web domains, we will tackle the following question: who has a voice in the media? This project has the ambitious aim to identify key attributes that will make a speech quoted and spread out. First, by gathering insights about speakers, with the use of wikidata: gender, age, occupation, ethnicity, etc. Second, by considering the quotation in itself and extract the subjects tackled, as well as the sentiments associated with the speech. From our datastory, we will be able to understand why an individual is more quoted than another, and anyone will have the keys to maximize its odds to be quoted in a famous english-speaking media.



## Research questions
A list of research questions you would like to address during the project.
- What kind of people has a voice in the media? We will consider socio-economic characteristics such as occupation, gender, age, ethnicity, etc. This question is investigated in the notebook [initial_analysis.ipynb](initial_analysis.ipynb).
- What do they need to talk about (in order to be quoted)? More precisely, investigate the answer to this question as a function of speaker's profile (e.g. quotation topics for different occupation, gender etc.). This part will involve text classification and is tackled in the notebook [what.ipynb](what.ipynb).
- How do they need to say it?
- How does the answer to the previous questions changed over time?

## Additional datasets
- __Language model for text classification and sentiment analysis__: <br> We will be using the following fine-tuned model, appropriate for the task of zero-shot text classification: DistilBERT base model uncased ([see there](https://huggingface.co/typeform/distilbert-base-uncased-mnli)). This model is fine-tuned on Multi-Genre Natural Language Inference (MNLI) dataset for the zero-shot classification task.


## Methods

- __Text classification__ for answering the "what". More precisely, our project requires to be able to automatically find quotations' topics: for example among {politics, U.S., world, economy, business, sport, science, technology, culture}. The approach used is called "zero-shot text classification" and is described in the notebook [what.ipynb](what.ipynb).
- __Sentiment analysis__

## Timeline
- ...
- 12 Nov: homework 2 released
- 26 Nov: homework 2 deadline
- 12 Nov: milestone P2 deadline
- 17 Dec: milestone P3 deadline  

## Milestones
A list of internal milestones up until project Milestone 3.
- ...


## Questions for TAs
Add here any questions you have for us related to the proposed project.
