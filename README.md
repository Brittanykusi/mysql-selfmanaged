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
1. first thing to do always when working in a new remote environment | ``` sudo apt-get update ```
2. 

## How to make mysql instance available to external computers

## inserting dataset into mysql database
