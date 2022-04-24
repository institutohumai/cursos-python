#!/usr/bin/env python
# coding: utf-8
 schtasks /Create [/S <system> [/U <username> [/P [<password>]]]]
    [/RU <username> [/RP <password>]] /SC <schedule> [/MO <modifier>] [/D <day>]
    [/M <months>] [/I <idletime>] /TN <taskname> /TR <taskrun> [/ST <starttime>]
    [/RI <interval>] [ {/ET <endtime> | /DU <duration>} [/K] [/XML <xmlfile>] [/V1]]
    [/SD <startdate>] [/ED <enddate>] [/IT] [/Z] [/F]
# In[1]:


import subprocess


# In[ ]:


subprocess.Popen('schtasks /create /ru Admin /rp paswd /tn "daily work" '
                 '/tr "{0}" /sc daily /st 23:55:00 '.format(path))


# In[ ]:


https://ole.michelsen.dk/blog/schedule-jobs-with-crontab-on-mac-osx/

