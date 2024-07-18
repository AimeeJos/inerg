# Inerg Project: Oil And Gas

### install

```bash
git clone https://github.com/AimeeJos/inerg.git
cd inerg

```

### run

```bash
# activate virtual environment
C:\Users\hp\Desktop\in\inerg> env\scripts\activate  
(env) PS C:\Users\hp\Desktop\in\inerg>

```
```bash
(env) PS C:\Users\hp\Desktop\in\inerg> python manage.py runserver   
```
##### server will be running in http://localhost:8000/api/swagger/#/

#### APIs
* /upload/ - Post api to upload xls file and data will be stored in database after calculating the total values of gas, oil and brine.
* /production/ - Get api to show total oil, gas and brine with filter based on well no.