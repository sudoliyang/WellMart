Step 1: Creating the database and corresponding user account for the project
	
	Run the following command:
        docker-compose exec db psql -f /usr/src/app/schema/create_db.sql

Step 2: Setup the privilege in the database.
	
	Run the following command:
        docker-compose exec db psql -U demo_admin demo_db -f /usr/src/app/schema/setup_db.sql


Step 3: Create the table with django 

	Run the following command:
        python manag.py migrate

