# Hackathon-Job-Application
**Project setup**
 1 . clone the repository
 

    ~$ git clone https://github.com/mrsidrdx/Hackathon-Job-Application
2 . Install Django

    ~$ pip3 install Django==3.0.1
3 . Install Dependencies

    ~$ pip3 install -r requirements.txt

**Access**

    http://127.0.0.1:8000/admin
Username : admin
Password : admin

**Routes**
1.  [name='index']
2.  admin/
3.  about/ [name='about']
4.  jobapply/ [name='jobapply']
5.  jobapply/thankyou [name='thankyou']
6.  register/jobseeker [name='register']
7.  login/jobseeker [name='user_login']
8.  register/manager [name='manager_register']
9.  login/manager [name='manager_login']
10.  logout/jobseeker [name='logout']
11.  logout/manager [name='manager_logout']
12.  ^media\/(?P<path>.*)$
