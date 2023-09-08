# Email Campaign Manager


## How to setup the Project

Create virtual environment.

```bash
virtualenv venv
```

To Activate the virtual environment run the following command.

```bash
source venv/bin/activate
```

open the terminal run the following command to install all dependencies.

```bash
 pip install -r requirements.txt
```

Now, move to the django-project run the following command.

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

Run the following command to run the project.

```bash
python3 manage.py runserver
```

To Deactivate the virtual environment run the following command.

```bash
deactivate
```

***Important: Create atleast one Campaign



## Dockerize setup
Move to the project folder and type the following command.

```bash
docker-compose up -d --build
```

Then, three container will be created, go inside the web container and type the following command.

```bash
docker exec -it <container_id> bash
python manage.py runserver 0.0.0.0:8000
```

To trigger the send campaign email, there will be a method inside email_app -> task -> send_daily_email_campaign