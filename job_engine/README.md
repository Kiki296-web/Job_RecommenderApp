Job Recommendation Engine

## Setting up the project

1. Clone the repository

   ```bash

   ```

- git clone https://github.com/username/project-name.git
  cd project-name

- Configure the databse in the settings.py file

2. Create Virtual enviroment and reqirements text file

pip install -r requirements.txt

3. Run migration and start server

- python manage.py migrate

- python manage.py runserver

4. Apps created

- users - Handles user authentication and profiles

- jobs - Handles job listings and recommendations

- applications -handles jobs applied to based on recommendation
