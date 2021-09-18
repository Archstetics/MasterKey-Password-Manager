## MasterKey Password Manager

MasterKey 🔐 is a CLI password manager and generator built in **Python** and **SQL**. The password manager relies on a Docker container 🐋 which runs a PostgreSQL image.
Each user has the possibility to save the name of the service, the username, the url and the passwords in the database for each account.

The user interface is very simple to use, and allows you to save and access your passwords by automatically copying them to the clipboard once selected.

All passwords are encrypted through the **AES** (Advanced Encryption Standard) algorithm before being entered into the database, and are protected by
a master password hashed and salted through the **Bcrypt** algorithm. 

It is also possible to use the password generator function, being able to choose its length and
type (only characters, characters and numbers, characters and special characters, characters, numbers and special characters).


## Libraries and Requirements

In order to run MasterKey, you need the following libraries:

- psycopg2
- clipboard
- string
- random
- secrets
- getpass
- sys
- os
- PyInquirer
- bcrypt
- base64
- cryptodomex

It is possible to install the following libraries through the terminal command: <code>$ pip install library_name</code>

Also you need to have a running PostgreSQL database called <code>accounts</code>, with a <code>uservault</code> table and four columns, respectively:
<code>account</code>, <code>userid</code>, <code>passwd</code>, <code>site_url</code>. I recommend using PostgreSQL in a Docker container.

To start the container, after installing Docker, use the command: <code> $ docker run --name container-name -p 5432:5432 -e POSTGRES_PASSWORD=mysecretpassword
-d postgres</code>


## Getting Started

