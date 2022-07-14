<h1> <p align="center">Text classification project for KPMG at Becode Ghent  </p> </h1>
<h3> <p align="center">This is a group project by team Tagsation as part of a collaboration between <a href="https://github.com/becodeorg"><strong>BeCode Ghent </strong></a> and <a href="https://www.linkedin.com/company/kpmg-belgium/?originalSubdomain=be"<strong>KPMG</strong></a>
 </p> </h3>
<h3> <p align="center">Tagsation team members: <a href="https://github.com/bakiguher">  Baki Guher, <a href="https://github.com/lelotok"> Lelo Manou Tokwaulu, <a href="https://github.com/Len-Fid"> Yelena Fidrmuc </a></p> </h3>

<p align = "center">
  <img src="https://becode.org/app/uploads/2021/06/logo-becode.png" alt="Logo" width="200" height="200"/>
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Plus_symbol.svg/1200px-Plus_symbol.svg.png" alt="plus" width="200" height="200"/>
  <img src="https://www.epra.com/application/files/7316/3162/2252/KPMG-logo.png" alt="KPMG" width="200" height="200"/></p>

 
# Project description: 
<img src="https://github.com/lelotok/KPMG_project/blob/Lena/assets/Text-Classification-using-Deep-Learning-1.png" align="right" width="550px"/>
<h4> The tax department at KPMG needs to be up to date with the changes in the law in order to help their customers. They do that by checking all the articles that are published in the <a href="https://www.ejustice.just.fgov.be/cgi/welcome.pl"> Belgian Official Gazette. </a> Going through every article is very time consuming and costly to our client. <br><br>
That is why our team has automated this process. We scrape the articles from the website,pre-process them and then by using the NLP( Natural Processing Language) techniques, our app reads the entire article and extracts the main key points.</h4> <br clear="right"/>
 
 
**Timeline assigned for the project:
 01/06/22 - 15/06/22** <br> 
 
 # How to navigate through the project: 
 *Click on the relevant step to access the Jupyter Notebook with the code*
 * **<a href="https://github.com/lelotok/KPMG_project/blob/main/jupyter/01_scrape.ipynb"> Scrapping the data </a>**   
    * **Beautiful Soup** package for scraping the articles from the <a href="https://www.ejustice.just.fgov.be/cgi/welcome.pl"> Belgian Official Gazette <a>
 * **<a href="https://github.com/lelotok/KPMG_project/blob/main/jupyter/02_summary.ipynb"> Extracting short summaries </a>**
    * <a href="https://huggingface.co/ml6team/mbart-large-cc25-cnn-dailymail-nl-finetune"> A pre-trained NLP model </a> for summarization from **Hugging Face** developed by <a href="https://huggingface.co/ml6team"> ML6 Team </a>
 * **<a href="https://github.com/lelotok/KPMG_project/blob/main/jupyter/03_keywords.ipynb"> Generating the keywords </a>**
    * <a href="https://spacy.io/models/nl#nl_core_news_lg"> A Dutch language NLP model </a> from **Spacy** and ```similarity()``` function for extracting the relevant tax keywords from the summaries of the articles 
 * **<a href="https://github.com/lelotok/KPMG_project/blob/main/jupyter/04_tagging.ipynb"> Tagging the text </a>**
    * Cross-checking the presence of the the keywoords in each summary. Returning the tags with the percentage of how much it corresponds to the assigned keywords 
 * **<a href="https://github.com/lelotok/KPMG_project/blob/main/jupyter/05_forsql.ipynb"> Creating the database </a>**
    * **Pandas** library to put all the created data into a dataframe
 * **<a href="https://github.com/lelotok/KPMG_project/blob/main/jupyter/06_app.ipynb"> Building an app </a>**
    * Preparing the code for the app using **Django**
 
 
 ## <a href="https://github.com/lelotok/KPMG_project/blob/main/btax/requirements.txt"> The requirements: </a>
* beautifulsoup4==4.11.1
* Django==4.0.5
* numpy==1.22.4
* pandas==1.4.2
* requests==2.27.1
* spacy==3.3.0
* transformers==4.17.0
* Unidecode==1.3.4
* <a href="https://github.com/explosion/spacy-models/releases/download/nl_core_news_lg-3.3.0/nl_core_news_lg-3.3.0-py3-none-any.whl">nl-core-news-lg </a>
* torch==1.11.0
* sentence-transformers==2.2.0
* sentencepiece==0.1.96
 
 # Contributors: 
 <a href="https://github.com/bakiguher">  Baki Guher </a> (Developer): 
- Developed the scrapping script
- Used NLP techniques to summarize the text and extract the tags
- Developed the App

<a href="https://github.com/Len-Fid"> Yelena Fidrmuc </a> (Functional analyst):
- Worked as a bridge between the product manager and the developer
- Helped to facilate the workflow researched about the relevant NLP techniques 
- Analysed the scope and help to define a strategy to build the solution
- Wrote the README file

 <a href="https://github.com/lelotok"> Lelo Tokwaulu </a> (Product manager):
- Made sure the solution is build according the scope of the project
- Helped the team to keep the communication flowing
- Wrote a script for the translation
- Designed the presentation slides
 
 # Visuals 
###  *Data source: Belgian Official Gazette/Belgische Staatblad/Moniteur Belge*
 <p align="center"><img src="https://github.com/lelotok/KPMG_project/blob/Lena/assets/National_Gazette.JPG"></a><p>
 
### *Our keywords:*
 The tax keywords we extracted from the data provided by the client
 <p align="center"><img src="https://github.com/lelotok/KPMG_project/blob/Lena/assets/keywords.png" width="700" height="400"></a></p>

### *The app: Newly scrapped data in a table with tags*
 <p align="center"><img src="https://github.com/lelotok/KPMG_project/blob/Lena/assets/tablewithtags.png"></a></p>
 
### *The app: Tag extractor from the pasted text*
 <p align="center"><img src="https://github.com/lelotok/KPMG_project/blob/Lena/assets/tagfromtext.png"></a></p>
 


 

