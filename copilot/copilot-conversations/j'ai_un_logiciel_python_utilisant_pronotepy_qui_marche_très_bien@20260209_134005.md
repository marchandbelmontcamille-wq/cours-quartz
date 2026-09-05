---
epoch: 1770640805703
modelKey: "eu.anthropic.claude-opus-4-6-v1|amazon-bedrock"
topic: "Pronotepy bloqué sur WiFi lycée"



tags:
  - copilot-conversation
---

**user**: j'ai un logiciel python utilisant pronotepy qui marche très bien sur 4G et wifi maison mais pas sur wifi lycée ou ca me sort l'erreur ❌ HTTPSConnectionPool(host='0920801w.index
[Timestamp: 2026/02/09 13:40:05]

**ai**: 
<think>L'utilisateur a un problème avec un logiciel Python utilisant pronotepy qui fonctionne en 4G et WiFi maison mais pas sur le WiFi du lycée. L'erreur semble être liée à une connexion HTTPS bloquée.

C'est un problème classique de réseau scolaire. Les réseaux WiFi des lycées utilisent généralement :

1. **Un proxy** - Le réseau du lycée route le trafic à travers un proxy (souvent un proxy filtrant comme Amon/EOLE dans l'Éducation Nationale)
2. **Un pare-feu** qui bloque certaines connexions sortantes


3. **Une inspection SSL/HTTPS** qui peut intercepter et modifier les certificats
4. **Un portail captif** nécessitant une authentification préalable

L'erreur `HTTPSConnectionPool` indique que la connexion vers le serveur Pronote est bloquée ou timeout. Le code UAI `0920801w` correspond au lycée Alexandre Dumas à Saint-Cloud, confirmant qu'il s'agit bien du réseau scolaire. Je dois configurer le proxy du lycée dans le code Python pour contourner ces restrictions réseau. Je configure la session requests avec les paramètres proxy (adresse et port) avant de l'utiliser avec pronotepy, ou j'utilise les variables d'environnement. Si le proxy effectue une inspection SSL, je devrai gérer les certificats ou désactiver la vérification SSL selon la situation.</think># Problème de connexion pronotepy sur le WiFi du lycée

C'est un problème **très classique** ! Le réseau WiFi du lycée (réseau Éducation Nationale, souvent géré par la solution **EOLE/Amon**) utilise un **proxy filtrant** qui bloque ou intercepte tes connexions HTTPS sortantes.

## 🔍 Pourquoi ça bloque ?

Le WiFi du lycée passe par :
1. **Un proxy HTTP/HTTPS** (obligatoire pour sortir sur internet)
2. **Un pare-feu** qui bloque les connexions directes
3. Parfois une **inspection SSL** qui casse les certificats

Ton script Python essaie de se connecter **directement** à `0920801w.index-education.net`, mais le réseau exige de passer par le proxy.

## ✅ Solutions

### 1. Trouver le proxy du lycée

Sur un PC connecté au WiFi du lycée, va dans :
- **Windows** : `Paramètres > Réseau > Proxy`
- **Ou** dans ton navigateur : `Paramètres > Proxy`

Tu devrais trouver quelque chose comme :
```
http://proxy:3128
http://10.x.x.x:8080
http://amon.lycee:3128
```

### 2. Configurer le proxy dans ton script Python

```python
import pronotepy
import os

# Configure le proxy AVANT de créer le client
os.environ['HTTP_PROXY'] = 'http://adresse_proxy:port'
os.environ['HTTPS_PROXY'] = 'http://adresse_proxy:port'

client = pronotepy.Client(
    'https://0920801w.index-education.net/pronote/',
    username='ton_identifiant',
    password='ton_mdp'
)
```

### 3. Alternative avec `requests.Session`

```python
import pronotepy
import requests

# Si le proxy nécessite une authentification (identifiants ENT/réseau)
proxies = {
    'http': 'http://utilisateur:motdepasse@proxy:port',
    'https': 'http://utilisateur:motdepasse@proxy:port',
}

# Tu peux aussi désactiver la vérification SSL si le proxy 
# fait de l'interception (pas idéal mais fonctionnel)
import urllib3
urllib3.disable_warnings()
```

### 4. Si problème de certificat SSL (inspection SSL)

```python
# En dernier recours, désactiver la vérification SSL
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
```

## 🔎 Pour diagnostiquer rapidement

Lance ça sur le WiFi du lycée :

```python
import requests

proxies = {
    'http': 'http://PROXY:PORT',  # ← remplace
    'https': 'http://PROXY:PORT',
}

try:
    r = requests.get('https://0920801w.index-education.net/pronote/', 
                      proxies=proxies, timeout=10)
    print(f"✅ Status: {r.status_code}")
except Exception as e:
    print(f"❌ {e}")
```

---

**Le plus important c'est de trouver l'adresse du proxy du lycée.** Tu peux aussi demander discrètement au prof de NSI ou à un assistant informatique 😉. Est-ce que tu arrives à naviguer sur Pronote normalement via le **navigateur** sur le WiFi du lycée ?
[Timestamp: 2026/02/09 13:40:31]

**user**: ca le montre pas. Comment le trouver avec python ?
[Timestamp: 2026/02/09 13:43:09]

**ai**: 
<think>L'utilisateur veut trouver l'adresse du proxy du lycée en utilisant Python. Il y a plusieurs méthodes pour détecter automatiquement les paramètres proxy.</think># Détecter le proxy du lycée avec Python

Lance ces scripts **sur le WiFi du lycée** :

## 1. Méthode la plus simple : proxy système

```python
import urllib.request

# Récupère le proxy configuré au niveau de l'OS
proxies = urllib.request.getproxies()
print("🔍 Proxy système détecté :")
for scheme, url in proxies.items():
    print(f"  {scheme} → {url}")

if not proxies:
    print("  Aucun proxy système trouvé")
```

## 2. Détecter le proxy via WPAD (auto-configuration)

Beaucoup de réseaux scolaires utilisent **WPAD** (Web Proxy Auto-Discovery) :

```python
import requests
import socket

# Tente de résoudre wpad sur le réseau local
wpad_urls = [
    'http://wpad/wpad.dat',
    'http://wpad.local/wpad.dat',
    'http://wpad/proxy.pac',
]

for url in wpad_urls:
    try:
        r = requests.get(url, timeout=5)
        if r.status_code == 200:
            print(f"✅ WPAD trouvé à {url}")
            print(f"Contenu :\n{r.text[:500]}")
            break
    except:
        print(f"❌ {url} — pas de réponse")
```

## 3. Scanner les ports proxy courants sur la gateway

```python
import socket
import subprocess
import re

# Trouve la passerelle (gateway) du réseau
def get_gateway():
    try:
        # Windows
        result = subprocess.run(['ipconfig'], capture_output=True, text=True)
        gateways = re.findall(r'Passerelle.*?:\s*([\d.]+)', result.stdout)
        if not gateways:
            gateways = re.findall(r'Gateway.*?:\s*([\d.]+)', result.stdout)
        return gateways
    except:
        return []

gateways = get_gateway()
print(f"🌐 Passerelle(s) détectée(s) : {gateways}")

# Ports proxy classiques Éducation Nationale
ports_proxy = [3128, 8080, 8888, 8443, 9090, 80, 443, 8000]

# Teste chaque gateway + port
hosts_to_test = gateways + ['proxy', 'proxy.local', 'amon', 'amon.local', '10.0.0.1']

for host in hosts_to_test:
    for port in ports_proxy:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((host, port))
            if result == 0:
                print(f"✅ PROXY TROUVÉ → {host}:{port}")
            sock.close()
        except:
            pass
```

## 4. Vérifier les variables d'environnement

```python
import os

env_vars = ['HTTP_PROXY', 'HTTPS_PROXY', 'http_proxy', 'https_proxy', 
            'NO_PROXY', 'ALL_PROXY', 'PAC_URL']

print("🔍 Variables d'environnement proxy :")
for var in env_vars:
    val = os.environ.get(var)
    if val:
        print(f"  {var} = {val}")
```

## 5. Script tout-en-un 🚀

```python
"""
Lance ce script sur le WiFi du lycée
et envoie-moi le résultat
"""
import urllib.request, socket, subprocess, re, os

print("=" * 40)
print("🔍 DÉTECTION PROXY LYCÉE")
print("=" * 40)

# 1) Proxy OS
print("\n[1] Proxy système :")
for k, v in urllib.request.getproxies().items():
    print(f"    {k} → {v}")

# 2) Variables env
print("\n[2] Variables d'environnement :")
for var in ['HTTP_PROXY','HTTPS_PROXY','http_proxy','https_proxy']:
    v = os.environ.get(var)
    if v: print(f"    {var} = {v}")

# 3) Gateway
print("\n[3] Scan réseau :")
result = subprocess.run(['ipconfig'], capture_output=True, text=True)
gws = re.findall(r'(?:Passerelle|Gateway).*?:\s*([\d.]+)', result.stdout)
print(f"    Gateways: {gws}")

# 4) Scan ports
ports = [3128, 8080, 8888, 9090, 80]
for host in gws + ['proxy', 'amon']:
    for port in ports:
        try:
            s = socket.socket(); s.settimeout(1)
            if s.connect_ex((host, port)) == 0:
                print(f"    ✅ {host}:{port} OUVERT")
            s.close()
        except: pass

print("\n" + "=" * 40)
```

---

Lance le **script tout-en-un** demain au lycée et copie-moi le résultat ici, je te dirai exactement quoi mettre dans ton code pronotepy ! 🎯
[Timestamp: 2026/02/09 13:43:29]

**user**: ========================================
🔍 DÉTECTION PROXY LYCÉE
========================================

[1] Proxy système :

[2] Variables d'environnement :

[3] Scan réseau :
    Gateways: ['172.20.63.254']

[Timestamp: 2026/02/09 13:45:12]

**ai**: 
<think>The scan didn't find any open proxy ports, and there's no system proxy configured. The gateway is `172.20.63.254` which is a typical school network IP range.

Since no proxy was found, the issue might be:
1. The firewall is simply blocking outgoing HTTPS connections to index-education.net
2. There might be a transparent proxy (no configuration needed, but it intercepts traffic)
3. DNS filtering
4. The ports might be blocked

Let me suggest further diagnostics:
- DNS resolution test
- Direct connection test with more details on the error
- Test if it's a port issue
- Try different approaches

The fact that no proxy was detected and no ports were found open on the gateway suggests the network might use a transparent proxy or just firewall rules blocking certain traffic.


I should walk through some additional diagnostic steps to narrow down what's actually blocking the connection.</think># Résultats : pas de proxy classique détecté

Le réseau du lycée utilise probablement soit un **proxy transparent** (invisible), soit un **pare-feu qui bloque directement** les connexions vers Pronote depuis des scripts.

## 🔍 Diagnostic approfondi — Lance ça au lycée

```python
import socket
import subprocess
import requests

print("=" * 50)
print("🔍 DIAGNOSTIC APPROFONDI")
print("=" * 50)

# 1) Test DNS — Est-ce que le nom se résout ?
print("\n[1] Résolution DNS :")
try:
    ip = socket.gethostbyname('0920801w.index-education.net')
    print(f"    ✅ 0920801w.index-education.net → {ip}")
except Exception as e:
    print(f"    ❌ DNS échoué : {e}")

# 2) Test ping gateway
print("\n[2] Ping gateway :")
r = subprocess.run(['ping', '-n', '2', '172.20.63.254'], 
                    capture_output=True, text=True)
print(f"    {'✅' if 'TTL' in r.stdout else '❌'} Gateway")

# 3) Test connexion TCP directe sur port 443
print("\n[3] Connexion TCP port 443 vers Pronote :")
try:
    s = socket.socket()
    s.settimeout(5)
    s.connect(('0920801w.index-education.net', 443))
    print("    ✅ Port 443 ouvert")
    s.close()
except Exception as e:
    print(f"    ❌ Port 443 bloqué : {e}")

# 4) Test connexion TCP port 80
print("\n[4] Connexion TCP port 80 vers Pronote :")
try:
    s = socket.socket()
    s.settimeout(5)
    s.connect(('0920801w.index-education.net', 80))
    print("    ✅ Port 80 ouvert")
    s.close()
except Exception as e:
    print(f"    ❌ Port 80 bloqué : {e}")

# 5) Test HTTPS complet
print("\n[5] Requête HTTPS vers Pronote :")
try:
    r = requests.get('https://0920801w.index-education.net/pronote/', 
                      timeout=10)
    print(f"    ✅ Status: {r.status_code}")
except requests.exceptions.SSLError as e:
    print(f"    ⚠️ Erreur SSL : {e}")
except requests.exceptions.ConnectionError as e:
    print(f"    ❌ Connexion refusée : {e}")
except requests.exceptions.Timeout:
    print(f"    ❌ Timeout — connexion bloquée par le pare-feu")
except Exception as e:
    print(f"    ❌ Autre erreur : {e}")

# 6) Test vers d'autres sites (vérifier si c'est ciblé)
print("\n[6] Test vers d'autres sites :")
for url in ['https://google.com', 'https://education.gouv.fr']:
    try:
        r = requests.get(url, timeout=10)
        print(f"    ✅ {url} → {r.status_code}")
    except Exception as e:
        print(f"    ❌ {url} → {type(e).__name__}")

# 7) Scan ports proxy élargi sur gateway
print("\n[7] Scan élargi gateway 172.20.63.254 :")
for port in [3128, 8080, 8888, 9090, 80, 443, 8443, 1080, 8000, 8880, 10000]:
    try:
        s = socket.socket(); s.settimeout(1)
        if s.connect_ex(('172.20.63.254', port)) == 0:
            print(f"    ✅ Port {port} OUVERT")
        s.close()
    except: pass

print("\n" + "=" * 50)
```

Copie-moi les résultats, ça va nous dire exactement **où ça coince** :
- Si le DNS échoue → problème DNS
- Si le TCP 443 est bloqué → pare-feu
- Si erreur SSL → proxy transparent qui intercepte
- Si Google marche mais Pronote non → blocage ciblé
[Timestamp: 2026/02/09 13:45:32]

**user**: ==================================================
🔍 DIAGNOSTIC APPROFONDI
==================================================

[1] Résolution DNS :
    ✅ 0920801w.index-education.net → 46.33.177.17

[2] Ping gateway :
    ✅ Gateway

[3] Connexion TCP port 443 vers Pronote :
    ✅ Port 443 ouvert

[4] Connexion TCP port 80 vers Pronote :
    ✅ Port 80 ouvert

[5] Requête HTTPS vers Pronote :
    ⚠️ Erreur SSL : HTTPSConnectionPool(host='0920801w.index-education.net', port=443): Max retries exceeded with url: /pronote/ (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate in certificate chain (_ssl.c:1108)')))

[6] Test vers d'autres sites :
    ❌ https://google.com → SSLError
    ✅ https://education.gouv.fr → 403

[7] Scan élargi gateway 172.20.63.254 :

==================================================
[Timestamp: 2026/02/09 13:46:23]

**ai**: 
<think>Now I can see the issue clearly. The results show:

1. DNS works ✅
2. TCP connections work ✅
3. **SSL Error: self signed certificate in certificate chain** ⚠️
4. Google also has SSLError, education.gouv.fr returns 403

This means the school network has a **transparent SSL proxy** (often called SSL inspection/interception) that intercepts HTTPS traffic and re-signs it with its own self-signed certificate. This is very common in French schools using solutions like EOLE/Amon or Pfsense.

The solution is to either:
1. Get the school's CA certificate and use it


2. Disable SSL verification in the requests session used by pronotepy
3. Extract the proxy's CA certificate programmatically

I need to check if pronotepy accepts a custom session parameter or if I can monkey-patch the SSL verification, then provide a practical solution that works with the library.</think># 🎯 Trouvé ! Proxy SSL transparent (interception HTTPS)

Le réseau du lycée utilise une **inspection SSL** : il intercepte **tout** le trafic HTTPS et re-signe les certificats avec son propre certificat auto-signé. C'est pour ça que Google aussi échoue en SSL.

## ✅ Solution 1 : Désactiver la vérif SSL dans pronotepy

```python
import pronotepy
import requests
import urllib3

# Supprime les warnings SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Crée une session custom sans vérification SSL
session = requests.Session()
session.verify = False

# Passe la session à pronotepy
client = pronotepy.Client(
    'https://0920801w.index-education.net/pronote/',
    username='ton_identifiant',
    password='ton_mdp',
    session=session  # ← la clé du problème
)

if client.logged_in:
    print("✅ Connecté !")
```

## ✅ Solution 2 : Récupérer le certificat du lycée (plus propre)

```python
import ssl
import socket

# Extraire le certificat du proxy
print("🔍 Extraction du certificat du proxy...")

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

with ctx.wrap_socket(socket.socket(), server_hostname='0920801w.index-education.net') as s:
    s.connect(('0920801w.index-education.net', 443))
    cert_pem = ssl.DER_cert_to_PEM_cert(s.getpeercert(True))

# Sauvegarde le certificat
with open('proxy_lycee.pem', 'w') as f:
    f.write(cert_pem)

print("✅ Certificat sauvé dans proxy_lycee.pem")
```

Puis utilise-le :

```python
import pronotepy
import requests

session = requests.Session()
session.verify = 'proxy_lycee.pem'  # ← utilise le certif du lycée

client = pronotepy.Client(
    'https://0920801w.index-education.net/pronote/',
    username='ton_identifiant',
    password='ton_mdp',
    session=session
)
```

## ✅ Solution 3 : Auto-détection (marche partout)

Pour que ton script fonctionne **aussi bien au lycée qu'à la maison** :

```python
import pronotepy
import requests
import urllib3

def get_client(url, username, password):
    # Tente d'abord normalement
    try:
        client = pronotepy.Client(url, username=username, password=password)
        if client.logged_in:
            print("✅ Connecté (mode normal)")
            return client
    except Exception as e:
        if 'SSL' in str(e) or 'CERTIFICATE' in str(e):
            print("⚠️ SSL intercepté — mode lycée activé")
            urllib3.disable_warnings()
            session = requests.Session()
            session.verify = False
            client = pronotepy.Client(
                url, 
                username=username, 
                password=password, 
                session=session
            )
            if client.logged_in:
                print("✅ Connecté (mode lycée)")
                return client
        else:
            print(f"❌ Erreur : {e}")
    return None

client = get_client(
    'https://0920801w.index-education.net/pronote/',
    'ton_identifiant',
    'ton_mdp'
)
```

---

> **La Solution 3 est la meilleure** — ton script marchera automatiquement partout : 4G, WiFi maison et WiFi lycée 🚀

Teste la Solution 1 demain au lycée pour confirmer que ça passe, et envoie-moi le résultat !
[Timestamp: 2026/02/09 13:46:43]

**user**: normalement, le certificat est déja installé et quand j'essaie d'acceder à pronote depuis le navigateur ca marche
[Timestamp: 2026/02/09 13:47:21]

**ai**: 
<think>Ah interesting! So the browser works fine because it uses the system's certificate store (which has the school's CA certificate installed). But Python's `requests` library uses its own certificate bundle (`certifi`) which doesn't include the school's proxy CA certificate.

So the solution is to make Python use the system certificate store instead of certifi's bundle.

There are several ways to do this:

1. Use `truststore` package (Python 3.10+) which makes requests use the OS certificate store
2. Export the certificate from the system store and point requests to it
3. Use `ssl.create_default_context()` which uses the system store

The cleanest solution is `truststore` or `pip-system-certs`.


Now I'll walk through the implementation steps for each approach.</think># Ah, c'est logique !

Le navigateur utilise le **magasin de certificats de Windows**, où le certificat du lycée est installé. Mais Python utilise **son propre magasin** (`certifi`) qui ne le connaît pas.

## ✅ Solution propre : forcer Python à utiliser les certificats Windows

### Option A : `truststore` (le plus simple)

```bash
pip install truststore
```

Puis dans ton script :

```python
import truststore
truststore.inject_into_ssl()

# Après ça, pronotepy utilisera les certificats Windows
import pronotepy

client = pronotepy.Client(
    'https://0920801w.index-education.net/pronote/',
    username='ton_identifiant',
    password='ton_mdp'
)
```

### Option B : `pip-system-certs` (encore plus simple)

```bash
pip install pip-system-certs
```

Tu n'as **rien à changer** dans ton code — ça patche automatiquement `certifi` pour utiliser les certificats Windows. Ton script original marchera directement.

### Option C : Exporter le certificat manuellement

Si les deux premières marchent pas :

1. Ouvre Chrome → va sur Pronote → clique sur le 🔒 → **Certificat**
2. Onglet **Chemin de certification** → sélectionne le **certificat racine** (tout en haut)
3. **Exporter** → format **PEM / Base64 (.cer)**
4. Sauvegarde-le par exemple dans `lycee_ca.pem`

Puis :

```python
import pronotepy
import requests

session = requests.Session()
session.verify = 'lycee_ca.pem'

client = pronotepy.Client(
    'https://0920801w.index-education.net/pronote/',
    username='ton_identifiant',
    password='ton_mdp',
    session=session
)
```

---

> **Essaie l'Option A en premier** (`truststore`), c'est la plus propre et ça marchera partout automatiquement 🎯
[Timestamp: 2026/02/09 13:47:35]