# PDF_Sharing_Platform
ShareDocs a PDF Management &amp; Collaboration System


# .env
SECRET_KEY={{SECRET_KEY}}  
DATABASE_NAME={{DATABASE_NAME}}  
DATABASE_USER={{DATABASE_USER}}  ``` Generally "postgres"```  
DATABASE_PASS={{DATABASE_PASS}}  

# HOW TO TEST PROJECT
1. Clone the repository in your local.  
   ``` git clone https://github.com/naresh2002/PDF_Sharing_Platform.git ```
3. Create .env file inside PDF_SHARING_PLATFORM folder using  
   ``` touch .env ```
4. Write .env file as  
   SECRET_KEY={{SECRET_KEY}}  
   DATABASE_NAME={{DATABASE_NAME}}  
   DATABASE_USER={{DATABASE_USER}}  
   DATABASE_PASS={{DATABASE_PASS}}
5. Go to your postgres shell and create a new database as {{DATABASE_NAME}}  
   a. To enter postgres shell in terminal for Ubuntu (varies for OS to OS)  
   ``` sudo -u postgres psql ```  
   b. In postgres shell  
   ``` CREATE DATABASE {{DATABASE_NAME}}; ```
7. Make migration  
   ``` python manage.py makemigrations ```  
8. Migrate schemas to DB  
   ``` python manage.py migrate```  
9. Start the server.  
   ``` python manage.py runserver ```
10. Open http://127.0.0.1:8000/ in browser and explore the project
