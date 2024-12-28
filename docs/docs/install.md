# Contribute

This section is dedicated to helping you join our project. Whether you're an experienced developer or just starting out, we value your enthusiasm and willingness to contribute. Here you'll find resources and guides that will help you get started contributing to our project.

If you have any questions or need assistance getting started, don't hesitate to ask. We're always happy to collaborate with you!

## Installation and launch of the application

You can launch the application using either Poetry.

To install **Poetry**, run the following command:

**Linux, macOS, Windows (WSL):**

``` bash
curl -sSL https://install.python-poetry.org | python3 -
```
A detailed installation guide for Poetry is available at [official documentation](<https://python-poetry.org/docs/>).

------------------------------------------------------------------------

## 1. Installation

### 1.1 Cloning the Repository and Activating the Virtual Environment

#### Cloning the repository

``` bash
git clone https://github.com/TurtleOld/hasta-la-vista-money.git
cd hasta-la-vista-money
```

### 1.2 Populating values in the .env file
```bash
make .env
```

SECRET_KEY - Key for the settings.py file. You can generate the key using the command - ```make secretkey```

> SECRET_KEY=

DEBUG - Debugging activation. Do not enable on a production server.
Set one of the following values: true, 1, yes.

> DEBUG=

DATABASE_URL - Database connection URL  
postgres://username:password@name or IP server:port/name_database

> DATABASE_URL=

ALLOWED_HOSTS - List of allowed hosts. Example 'localhost',
'127.0.0.1'. By default, hosts - localhost, 127.0.0.1

> ALLOWED_HOSTS=

------------------------------------------------------------------------

### 1.3 Activating the virtual environment:

``` bash
make shell
```

If you encounter the error: ```Command 'make' not found...```  
Run the following command in the console:

``` bash
sudo apt install make
```

Then:

``` bash
make install
```

------------------------------------------------------------------------

## 2. Running the application in development mode

``` bash
make start
```