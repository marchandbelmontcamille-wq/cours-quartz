---
epoch: 1790091664718
mode: agent
backendId: claude
sessionId: "e7b86257-744f-43a8-b1d0-a286fa8efe2f"
agentLabel: "fais une cheat sheet dans un fichier .typ eu utilisant la sy…"
usage: '{"usedTokens":49916,"contextWindow":200000,"inputTokens":1,"outputTokens":1,"cacheReadTokens":48727,"cacheWriteTokens":1187,"updatedAt":1790092571696}'
tags:
  - copilot-conversation
---

**user**: fais une cheat sheet dans un fichier .typ eu utilisant la syntaxe : #import "@preview/simple-cheatsheet:0.1.0": cheatsheet, container

#show: cheatsheet.with(
  info: (
    title: "Cybersecurity Fundamentals",
    authors: ("John Doe", "Jane Doe"),
  ),
)

= Core Principles
#container[
  == CIA Triad
  The three pillars of information security:
  - *Confidentiality*: Sensitive data must be protected from unauthorised read access
  - *Integrity*: Data and systems must be protected from unauthorised modification
  - *Availability*: Information must be accessible when needed by authorised users
  
  == Key Terminology
  - *Vulnerability*: A defect (bug or flaw) in a system that an attacker can exploit
  - *Threat*: A possible danger that might exploit a vulnerability
    - _Intentional_: Attacker actively developing an exploit
    - _Accidental_: Environmental factors (e.g., server room fire)
  - *Threat Agent*: An individual or entity carrying out an attack
  - *Threat Action*: The actual procedure used to execute an attack
  - *Exploit*: A concrete attack that leverages a vulnerability (e.g., malware program)
  - *Asset*: Anything of value to an organisation (hardware, software, data, etc.)
  - *Risk*: The criticality of a threat or vulnerability
    - Formula: $"Risk" = "Probability" times "Impact"$
  - *Countermeasure*: Any action, device, process, or technique that reduces risk

  == Malware Classification
  - *Malware*: Malicious software designed to disrupt operations, steal information, or gain unauthorised access
  - *Virus*: Spreads by inserting copies into executable programs or documents (requires a host). Typically needs user interaction to propagate
  - *Worm*: Self-replicating malware that spreads autonomously without requiring a host program. Scans networks for vulnerable systems
  - *Trojan*: Disguises itself as legitimate software but contains malicious code. Does not self-replicate
  - *Drive-by Download*: Exploits browser or plugin vulnerabilities to automatically execute malicious code from compromised websites
  - *Ransomware*: Encrypts victim's data and demands payment for decryption keys
  
  == Modern Threat Landscape
  Emerging attack vectors include custom web applications, supply chain attacks, and sophisticated social engineering campaigns

  == Types of Security Defects
  === Implementation Bugs
  - *Nature*: Localised problems introduced during coding phase
  - *Detection*: Code review and static analysis
  - *Examples*:
    - Using `gets()` instead of `fgets()`
    - SQL injection due to string concatenation
    - Missing input validation
  
  === Design Flaws
  - *Nature*: Architectural and systemic problems
  - *Detection*: Threat modelling and security design review
  - *Examples*:
    - Storing passwords in plaintext without hashing or salting
    - Implementing validation only on the client-side
    - Transmitting credentials over un-encrypted HTTP
  
  === The 50/50 Split
  Security defects are roughly evenly distributed between bugs and flaws, making both code review and design review equally critical

  == Reactive Countermeasures
  === Penetration and Patch Approach
  - *Method*: Address vulnerabilities as they are discovered and exploited
  - *Advantages*: Widely adopted, handles zero-day vulnerabilities
  - *Limitations*:
    - Time lag between discovery and patch release
    - Delay in users installing updates
    - Patches may introduce new vulnerabilities
  
  === Network Security Devices
  - *Purpose*: Block or mitigate attacks at the network level
  - *Examples*:
    - _WAF (Web Application Firewall)_: Filters malicious HTTP traffic
    - _IPS (Intrusion Prevention System)_: Detects and blocks suspicious activity

  == Proactive Countermeasures
  === Secure Development Life Cycle (SDLC)
  - *Principle*: Integrate security considerations at every stage of development
  - *Approach*: Adopt an attacker's mindset during design and implementation
  - *Activities*:
    - Threat modelling during design phase
    - Security-focused code reviews
    - Penetration testing before deployment
    - Security training for development teams
  
  === Balanced Strategy
  While proactive measures significantly reduce vulnerabilities, they cannot anticipate all future attack vectors. A comprehensive security strategy requires both proactive and reactive approaches
]

= Authentication & Authorisation
#container[
  == Authentication Mechanisms
  === Password-Based Authentication
  - *Best Practices*:
    - Use bcrypt, scrypt, or Argon2 for password hashing
    - Implement salting to prevent rainbow table attacks
    - Enforce strong password policies (length, complexity)
    - Enable multi-factor authentication (MFA)
  
  === Token-Based Authentication
  - *JWT (JSON Web Tokens)*: Stateless authentication for distributed systems
  - *OAuth 2.0*: Industry-standard authorisation framework
  - *Session Tokens*: Server-side session management with secure cookies
  
  === Biometric Authentication
  Fingerprint, facial recognition, and iris scanning for high-security applications

  == Authorisation Models
  === Role-Based Access Control (RBAC)
  Users assigned to roles; permissions granted to roles rather than individuals
  
  === Attribute-Based Access Control (ABAC)
  Decisions based on attributes of users, resources, and environmental conditions
  
  === Principle of Least Privilege
  Users should have only the minimum permissions necessary to perform their duties
]

= Network Security
#container[
  == Encryption Protocols
  === Transport Layer Security (TLS)
  - *Purpose*: Secure communication over networks
  - *Use Cases*: HTTPS, email encryption, VPNs
  - *Current Standard*: TLS 1.3 (avoid TLS 1.0 and 1.1)
  
  === IPsec
  Secures IP communications by authenticating and encrypting each packet
  
  === SSH (Secure Shell)
  Provides secure remote access and file transfer capabilities

  == Firewall Types
  === Packet Filtering
  Examines packet headers and filters based on IP addresses, ports, and protocols
  
  === Stateful Inspection
  Tracks connection state and filters based on traffic context
  
  === Application Layer (Proxy)
  Operates at Layer 7, inspecting application-specific protocols (HTTP, FTP, etc.)
  
  === Next-Generation Firewalls (NGFW)
  Combines traditional firewall with IPS, deep packet inspection, and application awareness
]

= Secure Coding Practices
#container[
  == Input Validation
  === Whitelist Approach
  Accept only known-good input patterns (preferred method)
  
  === Sanitisation
  Remove or encode dangerous characters from user input
  
  === Parameterised Queries
  Use prepared statements to prevent SQL injection attacks
  
  === Example Vulnerabilities
  - Cross-Site Scripting (XSS): Unsanitized user input rendered in HTML
  - SQL Injection: Concatenated SQL queries with user input
  - Command Injection: Unvalidated input passed to system commands

  == Output Encoding
  === Context-Aware Encoding
  - *HTML Context*: Encode `<`, `>`, `&`, `"`, `'`
  - *JavaScript Context*: Use JSON serialisation or JavaScript encoding
  - *URL Context*: Apply URL encoding for query parameters
  
  === Content Security Policy (CSP)
  HTTP header that prevents XSS by controlling resource loading sources
]
[Timestamp: 2026/09/22 17:41:04]

**ai**: Je vais lire la note sur les polynômes du 2nd degré pour créer la cheat sheet.Je vais maintenant créer le fichier `.typ` avec la cheat sheet sur les polynômes du 2nd degré.Le fichier `Chapitre 1 - Polynomes du 2nd degré.typ` a été créé dans `content/Mathématiques/`. Il couvre :

- **Forme développée** — définition et coefficients $a$, $b$, $c$
- **Forme canonique** — formule $a(x-\alpha)^2 + \beta$, méthode pas à pas et exemple
- **Forme factorisée** — les trois cas selon $\Delta$
- **Parabole** — orientation, sommet $S(\alpha;\beta)$, axe de symétrie $x=\alpha$, intersections avec les axes
- **Discriminant et équations** — formule $\Delta = b^2 - 4ac$, les trois cas avec formules et exemple complet
- **Variations** — tableaux de variations pour $a>0$ et $a<0$, signe du trinôme

Pour compiler le fichier, tu peux utiliser `typst compile` si tu as Typst installé, ou l'éditeur en ligne [typst.app](https://typst.app).
[Timestamp: 2026/09/22 17:41:04]

**user**: exclus la factorisatio,
[Timestamp: 2026/09/22 17:44:12]

**ai**: Je supprime la section "Forme factorisée" et la section entière "Discriminant et équations".Aussi, dans la section Variations, le signe de $f$ fait référence aux racines — je retire ça aussi.La cheat sheet ne contient plus rien sur la factorisation : la forme factorisée, la section "Discriminant et équations" (avec les formules $x_1$, $x_2$, $x_0$), et la partie "Signe de $f$" ont été supprimées. Il reste les trois sections : Définitions (forme développée + canonique), Parabole, et Variations.
[Timestamp: 2026/09/22 17:44:12]

**user**: remplace avec #import "@preview/cram-snap:0.2.2": cram-snap, theader

#set page(
  paper: "a4",
  flipped: true,
  margin: 1cm,
)
#set text(font: "Arial", size: 11pt)

#show: cram-snap.with(
  title: [Git Cheatsheet],
  icon: image("git-icon.svg"),
)

#table(
  theader[Adding changes],
  [`git add -u <path>`], [add all tracked files to the *staging area*],
  [`git add -p <path>`], [interactively pick which files to *stage*],
)

#table(
  theader[Storing changes],
  [`git stash [push] [path]`], [put current changes in the *working tree* into *stash* for later use],
  [`git stash pop`], [apply stored *stash* content into *working tree*, and clear *stash*],
  [`git stash drop`], [delete a specific *stash* from all the previous *stashes*],
)

#table(
  theader[Inspecting diffs],
  [`git diff [path]`], [show changes between *working tree* and *staging area*],
  [`git diff --cached/--staged [path]`], [show any changes between the *staging area* and the *repository*],
  [`git diff > file.patch`], [generate a patch file for current changes],
)

#table(
  theader[Reverting changes],
  [`git rebase`], [rebase the current branch on top of another specified branch],
  [`git rebase -i [commit sha]`], [start an interactive rebase],
  [`git revert [commit sha]`], [Create a new commit, reverting changes from the specified commit. It generates an *inversion* of changes.],
  [`git checkout <path>`], [discard changes in the *working tree*],
  [`git restore [-W/--worktree] <path>`], [discard changes in the *working tree*],
  [`git restore -S/--staged <path>`], [remove a file from a *staging area*],
  [`git restore -SW <path>`], [discard changes in the *working tree* and to the *staged* files],
  [`git reset <path>`], [remove a file from the *staging area*],
  [`git reset [mode] HEAD^`], [remove the latest *commit* from the current branch and:
    - `--soft` - keep file changes in the
      *working tree* and *stage* them;
    - `--mixed` - keep file changes;
    - `--keep` - reset only files which are
      different between current `HEAD` and the
      last commit
    - `--hard` - do *not* keep file changes],
)

#table(
  theader[Tagging commits],
  [`git tag`], [list all tags],
  [`git tag <name> [commit sha]`], [create a tag reference named `name` for the current or specific commit],
  [`git tag -a <name> -m <message>`], [create an annotated tag with the given message],
  [`git tag -d <name>`], [delete the tag with the given name],
)

#table(
  theader[Synchronizing repositories],
  [`git fetch [remote]`], [fetch changes from the *remote*, but not update tracking branches],
  [`git fetch --prune [remote]`], [delete remote refs that were removed from the *remote* repository],
  [`git pull [remote]`], [fetch changes from the *remote* and *merge* current branch with its upstream],
  [`git pull -r/--rebase [remote]`], [fetch changes from the *remote* and *rebase* current branch on top of the upstream],
  [`git push -u [remote] [branch]`], [push local branch to a *remote* repository and set its copy as an upstream],
)
[Timestamp: 2026/09/22 17:47:47]

**ai**: Le fichier a été réécrit avec la syntaxe `cram-snap`. Le contenu est organisé en cinq tableaux :

- **Définitions** — formes développée et canonique, identité remarquable
- **Obtenir la forme canonique** — méthode en 3 étapes + exemple
- **Parabole** — orientation, sommet, axe de symétrie, intersection
- **Variations si $a > 0$** — minimum
- **Variations si $a < 0$** — maximum

Note : j'ai retiré le paramètre `icon:` car tu n'as pas de fichier SVG associé — tu peux l'ajouter toi-même si besoin.
[Timestamp: 2026/09/22 17:47:47]

**user**: retourne sur simple cheat sheet
[Timestamp: 2026/09/22 17:51:10]

**ai**: Revenu sur `simple-cheatsheet` avec les trois sections en `#container[]` : Définitions et formes, Parabole, et Variations.
[Timestamp: 2026/09/22 17:51:10]

**user**: mets des exemples dans la cheat sheet
[Timestamp: 2026/09/22 17:52:23]

**ai**: Des exemples ont été ajoutés dans chaque section :

- **Forme développée** : $f(x) = 2x^2 + x + 3$ avec identification de $a$, $b$, $c$
- **Sommet et axe de symétrie** : $f(x) = -2(x+3)^2 + 5$ → $S(-3;5)$
- **Intersection avec les axes** : $f(x) = x^2 - 3x + 2$ passant par $(0;2)$
- **Variations** : un exemple pour le minimum et un pour le maximum

La section "Forme canonique" avait déjà son exemple détaillé ($3x^2 - 24x + 10$).
[Timestamp: 2026/09/22 17:52:23]

**user**: fais une simple fiche de révision en .md
[Timestamp: 2026/09/22 17:55:45]

**ai**: Le fichier [[Fiche de révision - Polynomes du 2nd degré]] a été créé dans `content/Mathématiques/`. Il couvre les quatre points essentiels — forme développée, forme canonique (avec méthode), parabole (tableau + sommet + axe), et variations — avec un exemple concret à chaque fois.
[Timestamp: 2026/09/22 17:55:45]