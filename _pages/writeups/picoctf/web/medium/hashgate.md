---
layout: terminal_centered
title: Hashgate
permalink: /writeups/picoctf/web/medium/hashgate
date: 2026-04-25
category: writeups
---

# Challenge Description  
**Author:** Yahaya Meddy  
**Description**
You have gotten access to an organisation's portal. Submit your email and password, and it redirects you to your profile. But be careful: just because access to the admin isn’t directly exposed doesn’t mean it’s secure.  
Maybe someone forgot that obscurity isn’t security... Can you find your way into the admin’s profile for this organisation and capture the flag?  

Hint 1: Notice anything about how the ID is being checked? It’s not plain text… maybe a one-way function is involved.  
Hint 2: There are about 20 employees in this organisation.  

### Writeup
We are only given a website here, and there are no other details. There is also no create account option, my only option was to login using an existing account.  
I looked at the source code and we stumble upon credentials for existing accounts.  
![Here lies a picture](/assets/img/picoCTF/hashgate/login_details.png)  

I used that an logged in, and this message was displayed:  
Access level: Guest (ID: 3000). Insufficient privileges to view classified data. Only top-tier users can access the flag.  

Having a look at the link it displayed this:  
/profile/user/e93028bdc1aacdfb3687181f2031765d  

The remaining gibberish reminded me of the first hint where a one-way function is involved, more specifically a hash function.  
Inserting e93028bdc1aacdfb3687181f2031765d into a [rainbow table](https://crackstation.net) which returned that that was the hash of 3000 using MD5.  
This accurately reflected the ID of the current account.  

The second hint is rather guessy, however, that meant that one of the 20 IDs from 3001 to 3020 was the admin account which contained the flag.  
I bruteforced it by using cyberchef to hash the different ID numebers to try and on ID 3013, it worked and outputted the flag.  

I didn't really like this challenge due to the ID guessing part and alot of people think so given its 40% liked rate. :P  