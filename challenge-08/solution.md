# 🛑 SSRF Vulnerability in Flask `/fetch` Endpoint

This repository contains a simple Flask endpoint that fetches remote URLs.
However, the current implementation introduces a **critical Server-Side Request Forgery (SSRF) vulnerability**.

---

## 📌 Vulnerable Code

```python
from flask import Flask, request, redirect
import urllib.request

app = Flask(__name__)

@app.route('/fetch')
def fetch():
    url = request.args.get('url', '')
    if url.startswith("https://ul.edu.lb"):
        response = urllib.request.urlopen(url)
        html = response.read()
        return html
    return redirect('/')
```

---

## 🚨 What Is the Vulnerability?

The endpoint allows a user to supply a URL parameter:

```
/fetch?url=<user-controlled URL>
```

If the URL begins with `https://ul.edu.lb`, the server makes a backend request to it.

This check is **unsafe and bypassable**, allowing an attacker to force the server to make requests to unintended destinations.

This is a classic **Server-Side Request Forgery (SSRF)** vulnerability.

---

## ⚠️ Why the Check Is Weak

The condition:

```python
url.startswith("https://ul.edu.lb")
```

can be easily bypassed, for example using:

- **Hostname tricks**

  ```
  https://ul.edu.lb.evil.com
  https://ul.edu.lb@evil.com
  ```

- **Redirections (302 redirects)**

  ```
  https://ul.edu.lb/path → 302 → http://127.0.0.1:5000/admin
  ```

- **Encoded URLs**

  ```
  https://ul.edu.lb:443@127.0.0.1
  https://ul.edu.lb%00.evil.com
  ```

Once bypassed, the attacker can make the server access **internal services**, such as:

- `http://localhost/admin`
- `http://127.0.0.1:3306` (port scan)
- Cloud instance metadata endpoints (very dangerous)

---

## 🧨 Impact

An attacker could:

- Access internal admin panels
- Query internal-only APIs
- Steal metadata & credentials from cloud environments
- Bypass firewalls using your backend server
- Perform internal port scanning
- Exfiltrate sensitive configuration files

---

## 🔒 How to Fix

### 1. Use strict URL parsing and domain allowlists

```python
from flask import abort
from urllib.parse import urlparse
import urllib.request

allowed_domains = ["ul.edu.lb"]

@app.route('/fetch')
def fetch():
    url = request.args.get('url','')
    parsed = urlparse(url)

    # Only allow HTTPS
    if parsed.scheme != "https":
        abort(400, "Invalid scheme")

    # Only allow exact hostname
    if parsed.hostname not in allowed_domains:
        abort(403, "Domain not allowed")

    # Disable automatic redirections
    req = urllib.request.Request(url, method="GET")
    opener = urllib.request.build_opener(
        urllib.request.HTTPRedirectHandler()
    )
    response = opener.open(req)
    return response.read()
```

---

## 🛡 Additional Mitigations

- Limit outbound requests to known services
- Disable redirects entirely
- Set timeouts and size limits
- Log all outgoing requests
- Consider removing the feature if not essential

---

## 📄 Summary

**The original implementation is vulnerable to SSRF**, which can be exploited to:

✔ Access internal servers
✔ Leak sensitive data
✔ Bypass network security
✔ Attack cloud metadata endpoints

Always validate URLs with full parsing and domain-level controls—not simple string checks.

---

If you'd like, I can also generate:

✅ A full secure refactor
✅ A demonstration exploit
✅ A PDF version of this README
