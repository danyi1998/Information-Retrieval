This readme concerns the following files and folders: 
final_ir, irproject, IR app 


Indexing with Solr:

1) We are using Solr-8.5.0, it can be downloaded from https://downloads.apache.org/lucene/solr/8.5.0/solr-8.5.0-src.tgz

2) We followed this tutorial to perform the indexing https://lucene.apache.org/solr/guide/8_5/solr-tutorial.html 

3) For the above tutorial, when we got to the part where we had to provide a name for our collection, we chose the name "irproject". 

4) When we got to the part where we had to choose a configuration, we chose "_default".

5) Now, we can launch the Solr Admin UI and see that it is working, and we can begin indexing our data.

6) The data we will index is a CSV file called "final_ir", which is placed inside the "irproject" folder. We will click into the solr-8.5.0 unzipped folder that we downloaded above, and then click into the "example" folder, and place the "irproject" folder inside. 

7) We used this command to index our data: java -jar -Dc=irproject -Dauto example\exampledocs\post.jar example\irproject\*.csv



Running the Web Application:

1) We are using django.

2) Click into the IR app folder.

3) Click into the outer mysite folder. 

4) Run the command py manage.py runserver 

5) Open the webpage(like that http://127.0.0.1:8000/search/) and start searching. 

(For the whole app to work, both django and solr must be started. If solr was stopped, then we need to restart it. Instructions on how to restart solr can be found in the tutorial under the section "Restart Solr".) 



 