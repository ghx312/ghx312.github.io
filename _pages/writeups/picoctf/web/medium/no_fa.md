---
layout: terminal_centered
title: No FA
permalink: /writeups/picoctf/web/medium/no_fa
date: 2026-04-25
category: writeups
---

# Challenge Description  
**Author:** Darkraicg492  
**Description:**  
Seems like some data has been leaked! Can you get the flag?  
Additional details will be available after launching your challenge instance.  

Hint 1: What happens when there's no salt?  
Hint 2: rockyou rockyou rockyou  
Hint 3: What makes 2FA safe?  

### Writeup
We are given 2 files and a website.  
The first file is a SQLit3 Database with the id, username, email, password and two_fa status.  
The second file is a Flask Webapp showing the code for the website.  

Having a look at the code for the website, we can see that we can onlyy get the flag if we are logged in as admin.  
![Here lies a picture](/assets/img/picoCTF/no_fa/admin_logic.png)  

So I first tried using the password given within the database.  
Credentials:  
Username: admin  
Password: c20fa16907343eef642d10f0bdb81bf629e6aaf6c906f26eabda079ca9e5ab67  

This did not work as the password was hashed, which means that this is not the real password but an "encrypted" version of the password.  
We can come to this conclusion using the first hint, where no salt is used. A salt is a chunk of text concatonated to the end of the password before hashing it.  
Not using a salt means that it is easier to recover the original password.  

I used [Rainbow Table](https://crackstation.net) in order to recover the admin's original password.  
Username: admin  
Password: apple@123  

Even though we have the password to the admin's account, they have set up a 2FA process and it requires us to have a 4-digit OTP.  
From the Webapp file, we can see that the randomly generated OTP is stored within the website's cookies.  
![Here lies a picture](/assets/img/picoCTF/no_fa/2fa_logic.png)  

By decoding the cookie, we can obtain the information about the OTP for the current session. I used [cookie decoder](https://www.kirsle.net/wizards/flask-session.cgi).  
![Here lies a picture](/assets/img/picoCTF/no_fa/cookie_decode.png)  

From the picture you can see that the OTP for the current session is 8495.  
Keying in the OTP, we are given the flag.  