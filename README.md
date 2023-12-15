# Group14-NLP-Final-Project
## Winston Yin, Pranav Kanchi, Jonathan Simonson, Kim Young
This our (Group 14)'s final project for Professor Meyer's Natural Language Processing Class
Our project looks to take the textual content of drop-shipped and authentic product listings and apply NLP-based classification algorithms to distinguish between the two types. \

Please find our research paper in the "Research Paper" directory. 

## Dependencies
Our code relies on a number of open-source libraries: `Numpy, Pandas, Scikit-Learn, NLTK, bs4, Scapy, Json, Time, Re, sentencepiece, jaxlib, pytorch, Gensim, etc`. It also requires a number of BERT based models and related libraries.\
Most plugins should come preinstalled, but if not, please use `pip install` to install all of them on your personal machine. 

## Running the Program

Please make sure that all directories references in the "Classification Models" directory point to the correct sources in the "Data Scraping" Folder. 

### Logistic Regression and Word Embeddings/Vectorization:
To run the Logistic Regression Classifiers, open `Logistic Regression_JS.ipynb` and run the notebook. There also sections labeled for our TF-IDF + Logistic Regression approach, as well as our Word2Vec + Logistic Regression approach. 
All results should be output as print statements to the console. 

### BERT-based models
To run the BERT-based models, open `NLP_Final_CoLab_Doc.ipynb` and run the notebook. The notebook should run in order, to allow for data processing. Further, if there are errors with finding the dataset, please change the filepath in the first cell.
All results should be output as print statements to the console. 
