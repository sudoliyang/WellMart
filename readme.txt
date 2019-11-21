Install
	Run the following command:
        docker-compose pull && docker-compose build

Start Services
	Run the following command:
        docker-compose up

Setup Database

Step 1: Creating the database and corresponding user account for the project
	
	Run the following command:
        docker-compose exec db psql -f /usr/src/app/schema/create_db.sql

Step 2: Setup the privilege in the database.
	
	Run the following command:
        docker-compose exec db psql demo_db -f /usr/src/app/schema/setup_db.sql

Step 3: Create the table with django 

	Run the following command:
        docker-compose exec app python manage.py migrate

Step 4: Grant table privilege to the users.

	Run the following command:
        docker-compose exec db psql demo_db -f /usr/src/app/schema/grant_table_privilege.sql

Step 5: Add Test Data

	Run the following command:
        docker-compose exec db psql demo_db -f /usr/src/app/schema/testing_data.sql

Setup Cronjob

    Edit /etc/crontab add
    ```
        0 9 * * * docker-compose -f <path_to>/docker-compose.yml  exec app python manage.py report
    ```
    It will execute every day 9:00, and export as report.csv
