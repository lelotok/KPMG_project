<h1> <p align="center">Text classification project for KPMG at Becode Ghent  </p> </h1>
<h3> <p align="center">This is a group project by BLY-TEAM as part of a collaboration between <a href="https://github.com/becodeorg"><strong>BeCode Ghent </strong></a> and <a href="https://www.linkedin.com/company/kpmg-belgium/?originalSubdomain=be"<strong>KPMG</strong></a>
 </p> </h3>
<h3> <p align="center">BLY-team members: <a href="https://github.com/bakiguher">  Baki Guher, <a href="https://github.com/lelotok"> Lelo Manou Tokwaulu, <a href="https://github.com/Len-Fid"> Lena-Fidrmuc </a></p> </h3>

<p align = "center">
  <img src="https://becode.org/app/uploads/2021/06/logo-becode.png" alt="Logo" width="200" height="200"/>
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Plus_symbol.svg/1200px-Plus_symbol.svg.png" alt="plus" width="200" height="200"/>
  <img src="https://www.epra.com/application/files/7316/3162/2252/KPMG-logo.png" alt="KPMG" width="200" height="200"/></p>

 
# Project description: 
<img src="https://github.com/lelotok/KPMG_project/blob/Lena/assets/Text-Classification-using-Deep-Learning-1.png" align="right" width="550px"/>
The tax department at KPMG needs to be up to date with the changes in the law in order to help their customers. They do that by checking all the articles that are published in the <a href="https://www.ejustice.just.fgov.be/cgi/welcome.pl"> National Gazette. </a> Going through every article is very time consuming and costly to our client. <br><br>
That is why our team has automated this process. We scrape the articles from the website,pre-process them and then by using the NLP( Natural Processing Language) techniquues, our app reads the entire article and extracts the main key points.<br clear="right"/>
 
 **Timeline assigned for the project:
 01/06/22 - 15/06/22**
 
 # Steps of the project: 
 *Click on the step to access the Jupyter Notebook with the code*
 * <a href="https://github.com/lelotok/KPMG_project/blob/baki/01_scrape.ipynb"> Scrapping the data </a> <br>
    * **Beautiful Soup** package for scraping the articles from the <a href="https://www.ejustice.just.fgov.be/cgi/welcome.pl"> National Gazette <a>
 * <a href="https://github.com/lelotok/KPMG_project/blob/baki/02_summary.ipynb"> Extracting short summaries </a> <br>
    * <a href="https://huggingface.co/ml6team/mbart-large-cc25-cnn-dailymail-nl-finetune"> A pre-trained NLP model </a> for summarization from **Hugging Face** developed by <a href="https://huggingface.co/ml6team"> ML6 Team </a>
 * <a href="https://github.com/lelotok/KPMG_project/blob/baki/03_keywords.ipynb"> Generating the keywords </a> <br>
    * <a href="https://spacy.io/models/nl#nl_core_news_lg"> A dutch NLP model </a> from **Spacy** for generating the relevant tax keywords
 * <a href="https://github.com/lelotok/KPMG_project/blob/baki/04_tagging.ipynb"> Tagging the text </a>

 
 

