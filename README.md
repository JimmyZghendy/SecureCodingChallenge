# 🔐 Secure Coding Challenge Repository

> _Practice finding and fixing security vulnerabilities — one challenge at a time._

This repository contains a series of **intentionally vulnerable code challenges** across multiple languages. Each challenge includes:

- A `main.[lang]` file with exploitable code
- A `solution.md` file to document your fix (or explain the vulnerability)
- A space for you to **convert insecure code into secure code**, using tools like **Semgrep**

---

## 🎯 Goal

Use this repo to:

- Learn common security pitfalls in real code
- Practice detecting vulnerabilities with **Semgrep**
- Improve your secure coding skills by remediating issues
- Document your findings and fixes in `solution.md`

---

## 📁 Structure

```
SECURECODINGCHALLENGE/
├── challenge-01/          # Java challenge
│   ├── main.java
│   └── solution.md
├── challenge-02/          # Python challenge
│   ├── main.py
│   └── solution.md
├── challenge-03/          # Go challenge
│   ├── main.go
│   └── solution.md
├── challenge-04/          # Python challenge
│   ├── main.py
│   └── solution.md
├── challenge-05/          # Java challenge
│   ├── main.java
│   └── solution.md
├── challenge-06/          # JavaScript challenge
│   ├── main.js
│   └── solution.md
├── challenge-07/          # JavaScript challenge
│   ├── main.js
│   └── solution.md
└── challenge-08/          # (Next challenge — you fill it!)
    ├── main.[lang]
    └── solution.md
```

---

## 🛠️ How to Get Started

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/SECURECODINGCHALLENGE.git
cd SECURECODINGCHALLENGE
```

### 2. Install Semgrep

✅ **Install via pip:**

```bash
pip install semgrep
```

✅ **Or via Homebrew (macOS/Linux):**

```bash
brew install semgrep
```

✅ **Or use Docker:**

```bash
docker run --rm -v "${PWD}:/src" returntocorp/semgrep semgrep --config=auto .
```

---

## 🧪 Run Semgrep on a Challenge

Scan a single challenge folder:

```bash
semgrep --config=auto challenge-01/
```

Scan all challenges:

```bash
semgrep --config=auto .
```

Scan with specific rules (e.g., security audit + secrets):

```bash
semgrep --config=p/security-audit,p/secrets .
```

> 💡 Tip: Use `--verbose` to see what rules are being applied.

---

## ✅ Your Task per Challenge

For each `challenge-XX/` folder:

1. **Review `main.[lang]`** — Identify the vulnerability.
2. **Run Semgrep** — Let it help you find potential issues.
3. **Fix the code** — Rewrite `main.[lang]` to eliminate the vulnerability.
4. **Document in `solution.md`** — Explain:
   - What the vulnerability was
   - How you fixed it
   - Why the fix is secure
   - Any Semgrep rules that flagged it

> 📝 Example `solution.md` content:
>
> ```
> ## Challenge 01: SQL Injection in Java
>
> ### Vulnerability
> The code uses string concatenation to build SQL queries, allowing attackers to inject malicious input.
>
> ### Fix
> Replaced with PreparedStatement to safely parameterize user input.
>
> ### Semgrep Rule Triggered
> `p/java` rule: `java.sql.Statement.execute*`
>
> ### Why It’s Secure Now
> Parameters are escaped automatically, preventing injection.
> ```

---

## 🧰 Recommended Semgrep Rulesets

| Ruleset                                      | Purpose                                       |
| -------------------------------------------- | --------------------------------------------- |
| `p/security-audit`                           | General security best practices               |
| `p/secrets`                                  | Detect hardcoded secrets, API keys, passwords |
| `p/python`, `p/java`, `p/javascript`, `p/go` | Language-specific checks                      |
| `p/ci`                                       | Optimized for CI pipelines                    |

You can combine them:

```bash
semgrep --config=p/security-audit,p/secrets,p/java challenge-01/
```

---
