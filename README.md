# mysql-selfmanaged

## Cloud environment of use: GCP

## Set up your VM
1. Create an account
2. Login to GCP account
3. Once on your google console click on create a VM
   - another way to navigate to creating a VM is to click into the navigation menu
   - find compute engine and hover over it
   - click on VM instances
   - at the top of the page click create instance
4. Create your VM
   - choose a name for your instance | mine was 'mysql-environment'
   - choose the image type Ubuntu 18.04 x86/64
   - choose the size needed to sustain and run the environment | for my 'mysql' environment I am using e2 medium 2 vCPU 4 GB memory
   - turn on firewalls for http and https
   - click create at the bottom of the page

## Commands used to set up the operating system (os) image
1. First thing to do always when working in a new remote environment | ``` sudo apt-get update ```
2. Install MYSQL server and MYSQL client | ``` sudo apt install mysql-server mysql-client ```
3. You can now login to mysql using this command | ``` sudo mysql ```

## Basic Commands in mysql server
- ``` show databases; ```

## How to make mysql instance available to external computers
- to make mysql database available to external computers we must create users
   -  use this command to create a new user | ``` CREATE USER 'dba'@'%' IDENTIFIED BY 'ahi2020'; ```
      - CREATE --> what we're asking the machine to do
      - USER --> what we're asking the machine to create
      - 'dba' --> the username
      - @ --> in other words it is pointing to the question 'where'
      - '%' --> wild card for who can connect stating the user can connect from multiple machines or anywhere
      - IDENTIFY BY --> what is the password
      - 'ahi2020' --> password
   - how to check if this command works | ``` select * from mysql.user; ``` | this provides a better looking list --> ``` select * from mysql.user \G ```
- 

## Inserting dataset into mysql database
