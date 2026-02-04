class RoadmapGenerator:
    def __init__(self):
        self.roadmaps = {
            "UI/UX Designer": {
                "Beginner": [
                    "Design Fundamentals (layout, color theory, typography, visual hierarchy)",
                    "UX Research Basics (user personas, wireframing, journey mapping)",
                    "Design Tools (Figma, Adobe XD, Photoshop, Illustrator basics)",
                    "User Interface Principles (consistency, feedback, accessibility)",
                    "Basic Prototyping (low-fidelity wireframes, mockups)",
                    "Design Process (research, ideate, prototype, test)"
                ],
                "Intermediate": [
                    "Interactive Prototyping (Figma/Adobe XD advanced, micro-interactions)",
                    "Component Libraries (design systems, buttons, forms, cards)",
                    "User Testing & Research (usability testing, feedback sessions, analytics)",
                    "Accessibility Design (WCAG guidelines, color contrast, keyboard navigation)",
                    "Responsive Design (mobile-first, breakpoints, adaptive layouts)",
                    "Client Projects (real-world design challenges, presentations)"
                ],
                "Advanced": [
                    "Design Systems Leadership (design tokens, component libraries, style guides)",
                    "Advanced UX Research (A/B testing, analytics-driven design, user behavior)",
                    "Advanced Accessibility (screen reader testing, ARIA, inclusive design)",
                    "Branding & Visual Identity (brand guidelines, logo design, marketing materials)",
                    "Design Leadership (team management, design strategy, stakeholder communication)",
                    "Portfolio & Career (case studies, design thinking, industry expertise)"
                ]
            },
            "Network Engineer": {
                "Beginner": [
                    "Networking Fundamentals (OSI model, TCP/IP, LAN/WAN, IP addressing)",
                    "Network Protocols (HTTP/HTTPS, DNS, DHCP, FTP, SSH)",
                    "Basic Network Hardware (routers, switches, hubs, cables)",
                    "Operating Systems Basics (Linux/Windows commands, file systems)",
                    "Network Troubleshooting (ping, traceroute, basic diagnostics)",
                    "Network Security Basics (firewalls, VPN, basic encryption)"
                ],
                "Intermediate": [
                    "Routing & Switching (VLANs, NAT, routing protocols, switch configuration)",
                    "Network Services (DNS servers, DHCP, web servers, mail servers)",
                    "Firewalls & Security (packet filtering, VPN setup, network monitoring)",
                    "System Administration (user management, services, performance monitoring)",
                    "Network Design (topology planning, capacity planning, documentation)",
                    "Intermediate Projects (network setup, server configuration)"
                ],
                "Advanced": [
                    "Advanced Networking (BGP, OSPF, SDN, network automation)",
                    "Enterprise Infrastructure (clustering, failover, load balancing)",
                    "Network Automation (Ansible, Python scripting, configuration management)",
                    "Security Hardening (compliance, auditing, patch management)",
                    "Cloud Networking (AWS/Azure networking, hybrid cloud)",
                    "Enterprise Projects (large-scale networks, disaster recovery)"
                ]
            },
            "Cybersecurity Specialist": {
                "Beginner": [
                    "Networking Fundamentals (OSI/TCP-IP, IP addressing, ports, protocols)",
                    "Security Basics (CIA triad, threat landscape, risk assessment)",
                    "Ethical Hacking Introduction (white/black hat, methodologies, legal aspects)",
                    "Cryptography Basics (symmetric/asymmetric encryption, hashing, SSL/TLS)",
                    "Operating Systems Security (Windows/Linux hardening, user management)",
                    "Basic Security Tools (antivirus, firewalls, VPN setup)"
                ],
                "Intermediate": [
                    "Penetration Testing (reconnaissance, Nmap, vulnerability scanning, Metasploit)",
                    "Web Security (OWASP Top 10, XSS, SQL injection, secure authentication)",
                    "Cloud Security (IAM, shared responsibility, encryption, monitoring)",
                    "Malware Analysis (static/dynamic analysis, sandbox, threat detection)",
                    "SOC Operations (SIEM tools, IDS/IPS, log monitoring, correlation)",
                    "Security Assessment Projects (vulnerability reports, remediation)"
                ],
                "Advanced": [
                    "Advanced Ethical Hacking (exploit development, social engineering, red teaming)",
                    "Advanced Cryptography (PKI, certificates, blockchain security)",
                    "Malware Reverse Engineering (IDA Pro, Ghidra, rootkit analysis)",
                    "Incident Response & Forensics (DFIR lifecycle, threat hunting, compliance)",
                    "Security Architecture (zero trust, secure design, risk management)",
                    "Enterprise Security (governance, compliance, security leadership)"
                ]
            },
            "Data & Analytics Specialist": {
                "Beginner": [
                    "Excel Fundamentals (formulas, VLOOKUP, conditional formatting, charts)",
                    "SQL Basics (SELECT, WHERE, JOINs, aggregate functions)",
                    "Python for Data (Pandas, NumPy, Jupyter Notebook, CSV handling)",
                    "R Basics (RStudio, data frames, vectors, basic plotting)",
                    "Data Types & Structures (understanding different data formats)",
                    "Basic Visualization (charts, graphs, simple dashboards)"
                ],
                "Intermediate": [
                    "Data Cleaning & Transformation (missing values, duplicates, outliers)",
                    "Advanced SQL (subqueries, window functions, performance tuning)",
                    "Python Analytics (Pandas advanced, pivot tables, time series)",
                    "R Intermediate (dplyr, tidyverse, ggplot2, data reshaping)",
                    "Visualization Tools (Power BI, Tableau basics, interactive charts)",
                    "Statistical Analysis (correlation, regression, hypothesis testing)"
                ],
                "Advanced": [
                    "Business Intelligence (KPIs, dashboard design, live data sources)",
                    "Advanced Analytics (forecasting, time series, predictive modeling)",
                    "Advanced Visualization (Power BI DAX, Tableau advanced, Plotly)",
                    "Data Pipelines (automated cleaning, ETL processes)",
                    "Statistical Modeling (machine learning, advanced regression)",
                    "Enterprise Analytics (Shiny dashboards, report automation)"
                ]
            },
            "Mobile App Developer": {
                "Beginner": [
                    "Platform Setup & Basics (Android Studio, Xcode, Flutter SDK)",
                    "Programming Fundamentals (Java/Kotlin, Swift, Dart basics)",
                    "UI Basics & Layouts (XML layouts, Views, Widgets, Components)",
                    "Control Flow & Functions (if/else, loops, optionals, events)",
                    "First Apps Development (Hello World apps, basic interactions)",
                    "Development Environment (Emulators, simulators, hot reload)"
                ],
                "Intermediate": [
                    "Navigation & Screens (Intents, ViewControllers, routing, fragments)",
                    "Data Management (SQLite, Core Data, local storage, databases)",
                    "API Integration (REST APIs, networking, JSON parsing, HTTP)",
                    "State Management (setState, Provider, Redux, MVVM patterns)",
                    "Device Features (Camera, GPS, sensors, permissions)",
                    "Intermediate Projects (CRUD apps, API-based apps)"
                ],
                "Advanced": [
                    "Advanced UI & Animations (Material Design, SwiftUI, custom views)",
                    "Performance Optimization (memory management, caching, lazy loading)",
                    "Push Notifications & Background Tasks (Firebase, WorkManager)",
                    "Security & Testing (encryption, unit tests, UI tests)",
                    "App Store Deployment (Play Store, App Store, CI/CD)",
                    "Production Apps (scalable architecture, enterprise features)"
                ]
            },
            "Full-Stack Web Developer": {
                "Beginner": [
                    "HTML & CSS Fundamentals (semantic HTML, box model, flexbox, grid)",
                    "JavaScript Basics & DOM (variables, functions, events, manipulation)",
                    "Version Control & Git (clone, commit, push, GitHub workflow)",
                    "Backend Basics (Node.js/Express or Python/Flask, REST APIs)",
                    "Database Fundamentals (MySQL/PostgreSQL basics, MongoDB intro)",
                    "Beginner Projects (portfolio site, simple CRUD app)"
                ],
                "Intermediate": [
                    "Frontend Frameworks (React/Vue/Angular basics, components, state)",
                    "Advanced JavaScript & APIs (async/await, fetch, error handling)",
                    "Backend Development (Express middleware, authentication, JWT)",
                    "Database Integration (ORM, relationships, query optimization)",
                    "Styling Frameworks (Tailwind CSS, Bootstrap, responsive design)",
                    "Intermediate Projects (e-commerce site, social media app)"
                ],
                "Advanced": [
                    "Advanced Frontend (Next.js SSR/SSG, state management, performance)",
                    "Microservices & APIs (RESTful design, GraphQL, WebSockets)",
                    "DevOps & Deployment (Docker, CI/CD, cloud platforms)",
                    "Database Optimization & Caching (Redis, query tuning, scaling)",
                    "Security & Testing (authentication, authorization, unit/integration tests)",
                    "Production Projects (scalable web apps, enterprise systems)"
                ]
            },
            "Rust Developer": {
                "Beginner": [
                    "Rust Installation & Basics (cargo, rustc, safety concepts)",
                    "Variables & Mutability (let vs let mut, ownership rules)",
                    "Data Types & Functions (scalars, compounds, expressions)",
                    "Ownership & Borrowing (references, mutable references)",
                    "Control Flow & Pattern Matching (if/else, loops, match)",
                    "Beginner Projects (CLI calculator, file reader)"
                ],
                "Intermediate": [
                    "Structs & Enums (defining, impl methods, pattern matching)",
                    "Traits & Error Handling (trait bounds, Result, Option, ? operator)",
                    "Modules & Crates (mod, use, Cargo.toml, packages)",
                    "Lifetimes & Advanced Borrowing (reference scopes)",
                    "Collections & Iterators (Vec, HashMap, iterator patterns)",
                    "Intermediate Projects (REST API, file processor)"
                ],
                "Advanced": [
                    "Unsafe Rust & Memory Optimization (raw pointers, zero-cost abstractions)",
                    "Async Rust & Concurrency (async/await, Futures, threads, Mutex)",
                    "Systems Programming (OS-level tools, performance optimization)",
                    "Advanced Traits & Macros (associated types, procedural macros)",
                    "Embedded & WebAssembly (no_std, WASM targets)",
                    "Advanced Projects (distributed systems, embedded applications)"
                ]
            },
            "Swift Developer": {
                "Beginner": [
                    "Swift Basics & Playgrounds (syntax, Xcode setup)",
                    "Variables & Data Types (var vs let, Int, String, Bool, tuples)",
                    "Control Flow & Functions (if/else, switch, loops, parameters)",
                    "Optionals & Safety (?, !, optional binding, nil coalescing)",
                    "Collections & Basic OOP (Array, Dictionary, classes, structs)",
                    "Beginner Projects (calculator app, simple iOS app)"
                ],
                "Intermediate": [
                    "Classes, Structs & Protocols (properties, methods, inheritance)",
                    "Error Handling & Closures (try/catch, anonymous functions)",
                    "iOS Development Basics (UIKit, SwiftUI, views, controllers)",
                    "Memory Management (ARC, strong/weak references)",
                    "Advanced Collections & Generics (custom types, constraints)",
                    "Intermediate Projects (iOS app with UI, data persistence)"
                ],
                "Advanced": [
                    "Advanced SwiftUI & Animations (custom views, complex layouts)",
                    "Concurrency & Performance (DispatchQueue, async/await, profiling)",
                    "App Architecture & Patterns (MVVM, Combine, data flow)",
                    "Core Data & Networking (persistence, REST APIs, JSON)",
                    "App Store & Distribution (testing, deployment, optimization)",
                    "Advanced Projects (production iOS apps, cross-platform)"
                ]
            },
            "Kotlin Developer": {
                "Beginner": [
                    "Kotlin Basics & Setup (vs Java, IntelliJ/Android Studio)",
                    "Variables & Functions (val vs var, named params, default values)",
                    "Null Safety & Collections (?, !!, ?:, List, Set, Map)",
                    "Classes & Inheritance (open classes, data classes)",
                    "Control Flow & Lambdas (when, loops, functional programming)",
                    "Beginner Projects (console app, basic Android activity)"
                ],
                "Intermediate": [
                    "Advanced OOP & Data Classes (sealed classes, objects)",
                    "Coroutines & Async Programming (suspend functions, async tasks)",
                    "Android Development (Activities, Fragments, layouts, XML)",
                    "Collections & Higher-Order Functions (map, filter, reduce)",
                    "Interoperability & Extensions (Java interop, extension functions)",
                    "Intermediate Projects (Android app with database, REST API)"
                ],
                "Advanced": [
                    "Flow & Channels (reactive streams, concurrency patterns)",
                    "Multiplatform Projects (shared code, KMM, native targets)",
                    "Backend Development (Ktor, REST APIs, server setup)",
                    "Performance & Architecture (profiling, MVVM, Clean Architecture)",
                    "Advanced Android (Jetpack Compose, dependency injection)",
                    "Advanced Projects (multiplatform app, enterprise backend)"
                ]
            },
            "PHP Developer": {
                "Beginner": [
                    "PHP Basics & Setup (syntax, XAMPP/WAMP, web server basics)",
                    "Variables & Forms (dynamic typing, GET/POST, form handling)",
                    "Control Structures & Functions (if/else, loops, user-defined functions)",
                    "Arrays & Strings (indexed/associative arrays, string manipulation)",
                    "MySQL Integration (connecting, basic queries, CRUD operations)",
                    "Beginner Projects (contact form, simple blog, user registration)"
                ],
                "Intermediate": [
                    "Object-Oriented PHP (classes, objects, inheritance, encapsulation)",
                    "Sessions & Authentication (cookies, login systems, password hashing)",
                    "MVC Pattern & Frameworks (Laravel basics, routing, Blade templates)",
                    "Database Design & ORM (relationships, Eloquent, migrations)",
                    "APIs & JSON (REST API creation, JSON handling, HTTP methods)",
                    "Intermediate Projects (e-commerce site, CMS, REST API)"
                ],
                "Advanced": [
                    "Laravel Advanced (middleware, queues, caching, Artisan commands)",
                    "Performance & Security (query optimization, SQL injection prevention)",
                    "Payment Integration & APIs (Stripe, PayPal, third-party services)",
                    "Testing & Deployment (PHPUnit, CI/CD, server configuration)",
                    "Scalable Architecture (microservices, load balancing, Redis)",
                    "Advanced Projects (enterprise web app, SaaS platform)"
                ]
            },
            "Go Developer": {
                "Beginner": [
                    "Go Installation & Setup (GOROOT, GOPATH, workspace structure)",
                    "Go Syntax & Program Structure (package main, imports, gofmt)",
                    "Variables, Constants & Control Structures (var, :=, if, for, defer)",
                    "Functions & Multiple Returns (parameters, named returns, variadic)",
                    "Arrays, Slices & Maps (slice operations, key-value pairs)",
                    "Structs & Methods (struct literals, embedded structs)"
                ],
                "Intermediate": [
                    "Interfaces & Error Handling (implicit implementation, custom errors)",
                    "Packages & Modules (go.mod, dependency management, exports)",
                    "File I/O & Buffered Operations (reading/writing files, directories)",
                    "Goroutines Basics (creating goroutines, lifecycle, pitfalls)",
                    "Channels & Communication (buffered/unbuffered, select statement)",
                    "Intermediate Projects (REST API, file processor)"
                ],
                "Advanced": [
                    "Concurrency Patterns (worker pools, fan-in/out, pipelines, context)",
                    "Memory Management & Performance (GC, escape analysis, profiling)",
                    "Networking & HTTP (TCP/UDP, REST APIs, WebSockets, gRPC)",
                    "Microservices Architecture (service discovery, API gateways)",
                    "Cloud-Native Development (Docker, Kubernetes, observability)",
                    "Advanced Projects (distributed systems, concurrent web crawler)"
                ]
            },
            "TypeScript Developer": {
                "Beginner": [
                    "TypeScript Basics & Setup (Why TS, installation, tsc compiler)",
                    "Basic Types & Type Inference (number, string, arrays, tuples)",
                    "Functions & Interfaces (Typed parameters, optional properties)",
                    "Variables & Type Safety (Explicit typing, const assertions)",
                    "Compilation & Project Setup (tsconfig.json basics, watching files)",
                    "Beginner Projects (Typed calculator, form validation)"
                ],
                "Intermediate": [
                    "Enums & Union Types (String enums, intersection types, narrowing)",
                    "Generics & Classes (Generic functions, access modifiers, inheritance)",
                    "Modules & Type Guards (ES modules, custom type guards, discriminated unions)",
                    "API Integration (Typing responses, Fetch with TS, error handling)",
                    "Framework Integration (React with TS, Node.js typing, Express types)",
                    "Intermediate Projects (Typed REST API, React + TS app)"
                ],
                "Advanced": [
                    "Advanced Generics & Utility Types (Conditional types, Partial, Pick, Omit)",
                    "Decorators & Compiler Options (Method decorators, strict mode, performance)",
                    "Type Performance & Architecture (Large-scale TS, monorepos, migration)",
                    "Advanced Patterns (Mapped types, recursive types, variance)",
                    "Enterprise TypeScript (Domain-driven design, API contracts, versioning)",
                    "Advanced Projects (Full-stack TS, design systems, SDK development)"
                ]
            },
            "JavaScript Developer": {
                "Beginner": [
                    "JavaScript Basics & Environment (History, V8 engine, Node.js setup)",
                    "Variables & Data Types (let/const, primitives, objects)",
                    "Control Structures & Functions (if/else, loops, arrow functions)",
                    "Arrays & Objects (Methods, DOM manipulation basics)",
                    "Events & Form Handling (Event listeners, validation)",
                    "Beginner Projects (To-do list, calculator, quiz app)"
                ],
                "Intermediate": [
                    "Scope, Closures & Hoisting (Function scope, closures)",
                    "Asynchronous JavaScript (Promises, async/await, event loop)",
                    "ES6+ Features (Destructuring, modules, template literals)",
                    "APIs & Browser Storage (Fetch, REST APIs, localStorage)",
                    "OOP JavaScript & Node.js (Classes, prototypes, Express basics)",
                    "Intermediate Projects (Weather app, CRUD app, chat app)"
                ],
                "Advanced": [
                    "Performance & JavaScript Internals (Optimization, execution context)",
                    "Design Patterns & Frontend Frameworks (Module pattern, React/Vue)",
                    "State Management & Testing (Redux, Context API, Jest)",
                    "Build Tools & Security (Webpack, Babel, XSS prevention)",
                    "Advanced Async & WebSockets (Promise chaining, real-time apps)",
                    "Full-Stack Projects (SPA, e-commerce, scalable APIs)"
                ]
            },
            "C# Developer": {
                "Beginner": [
                    "C# Basics & .NET Setup (History, CLR, Visual Studio)",
                    "Basic Syntax & Variables (Data types, var keyword, casting)",
                    "Control Structures & Methods (if/else, loops, overloading)",
                    "Arrays & Collections Basics (Lists, dictionaries, foreach)",
                    "Input/Output & Console Operations (ReadLine, WriteLine)",
                    "Beginner Projects (Calculator, to-do app)"
                ],
                "Intermediate": [
                    "Object-Oriented Programming (Classes, inheritance, interfaces)",
                    "Exception Handling & Collections (try-catch, LINQ basics)",
                    "File Handling & Serialization (File operations, JSON)",
                    "Delegates, Events & Async Programming (async/await, Tasks)",
                    "Database & Entity Framework (EF Core, CRUD operations)",
                    "Application Development (WPF, ASP.NET basics)"
                ],
                "Advanced": [
                    "Advanced C# & Memory Management (GC, Span, structs vs classes)",
                    "Advanced LINQ & Multithreading (Complex queries, synchronization)",
                    "ASP.NET Core & Web APIs (MVC, authentication, middleware)",
                    "Design Patterns & Testing (DI, Repository, unit testing)",
                    "DevOps & Cloud Deployment (Docker, Azure, CI/CD)",
                    "Enterprise Applications (Microservices, performance optimization)"
                ]
            },
            "C++ Developer": {
                "Beginner": [
                    "C++ Basics & Compilation (History, GCC, IDEs setup)",
                    "Basic Syntax & Variables (Data types, operators)",
                    "Control Structures & Functions (if/else, loops, overloading)",
                    "Arrays, Strings & Pointers (Memory addresses, references)",
                    "Input/Output & File Basics (cin/cout, streams)",
                    "Beginner Projects (Calculator, ATM program)"
                ],
                "Intermediate": [
                    "Object-Oriented Programming (Classes, inheritance, polymorphism)",
                    "Memory Management (Stack/heap, new/delete, smart pointers)",
                    "STL Containers & Algorithms (vector, map, sort, find)",
                    "Templates & Exception Handling (Generic programming, try-catch)",
                    "File Handling & Multithreading Basics (Streams, threads, mutex)",
                    "Intermediate Projects (Library system, file tools)"
                ],
                "Advanced": [
                    "Advanced Memory & Move Semantics (RAII, unique_ptr, move constructors)",
                    "Concurrency & Performance (Thread pools, atomic operations, optimization)",
                    "Low-Level Programming (Bit manipulation, cache optimization)",
                    "Design Patterns & Testing (Singleton, Factory, unit testing)",
                    "Specialized Domains (Game dev, embedded systems, real-time apps)",
                    "Large-Scale Projects (Game engines, system software)"
                ]
            },
            "Java Developer": {
                "Beginner": [
                    "Java Basics & JVM (Installation, JDK, JRE setup)",
                    "Basic Syntax & Variables (Data types, operators)",
                    "Control Structures (if/else, loops, switch)",
                    "Arrays & Strings (Methods, StringBuilder)",
                    "Methods & Exception Basics (try-catch, finally)",
                    "Beginner Projects (Calculator, Banking app)"
                ],
                "Intermediate": [
                    "Object-Oriented Programming (Classes, Inheritance, Polymorphism)",
                    "Collections Framework (List, Set, Map, Iterators)",
                    "File Handling & Serialization",
                    "Multithreading Basics & Synchronization",
                    "Java 8+ Features (Lambda, Streams, Optional)",
                    "JDBC & Database Integration"
                ],
                "Advanced": [
                    "Advanced Multithreading & JVM Internals",
                    "Spring Framework & Spring Boot",
                    "Design Patterns & Data Structures/Algorithms",
                    "Web Development (Servlets, REST APIs, Microservices)",
                    "Testing (JUnit, Mockito) & DevOps (Docker, CI/CD)",
                    "Enterprise Applications & Performance Tuning"
                ]
            },
            "Python Developer": {
                "Beginner": [
                    "What is Python & How It Works - History, use cases, interpreted vs compiled languages, Python versions",
                    "Installing Python & IDEs - Installation on OS, environment variables, REPL, VS Code/PyCharm/Jupyter",
                    "Variables & Data Types - Variables, naming rules, int/float/string/boolean, type casting, dynamic typing",
                    "Input / Output - input() function, print() function, f-strings, format(), escape characters",
                    "Conditional Statements - if/elif/else, comparison operators, logical operators, nested conditions",
                    "Loops - for/while loops, range(), break/continue/pass, nested loops",
                    "Functions - Defining functions, parameters & arguments, return values, default/keyword arguments, scope",
                    "Lists - Creating lists, indexing & slicing, list methods, list comprehensions",
                    "Tuples - Tuple creation, immutable nature, packing & unpacking",
                    "Sets - Set operations, union/intersection/difference, removing duplicates",
                    "Dictionaries - Key-value pairs, dictionary methods, iterating dictionaries",
                    "Basic Error Handling - Syntax vs runtime errors, try/except, multiple exceptions, finally block",
                    "Simple Programs & Mini Projects - Calculator, number guessing game, password generator, CLI to-do list"
                ],
                "Intermediate": [
                    "Advanced Functions & Modules - Lambda functions, *args/**kwargs, nested functions, importing/creating modules",
                    "File Handling - Reading/writing files, file modes (r/w/a), CSV & text files, with statement",
                    "Exception Handling - Custom exceptions, raising exceptions, exception hierarchy",
                    "Object-Oriented Programming - Classes & objects, constructors, inheritance, polymorphism, encapsulation",
                    "Standard Libraries - math, random, datetime, os, sys, json modules",
                    "Virtual Environments & Package Management - venv, pip, requirements.txt, third-party libraries",
                    "Working with APIs - REST APIs, HTTP methods, requests library, parsing JSON responses",
                    "Regular Expressions - Regex basics, common patterns, re module, searching & matching text",
                    "Python Project Structure - Folder organization, __init__.py, main vs helper files, config files",
                    "Intermediate Projects - File-based contact manager, weather app (API), URL shortener, CLI quiz app"
                ],
                "Advanced": [
                    "Advanced OOP Concepts - Multiple inheritance, Method Resolution Order (MRO), operator overloading, magic methods",
                    "Data Structures & Algorithms - Arrays/strings, linked lists, stacks/queues, trees/graphs, searching/sorting",
                    "Multithreading & Multiprocessing - Threads vs processes, GIL, threading module, multiprocessing module",
                    "Asynchronous Programming - Async vs sync, async/await, asyncio, event loop",
                    "Memory Management - Garbage collection, reference counting, memory leaks, profiling memory usage",
                    "Performance Optimization - Code profiling, optimization techniques, C extensions, caching",
                    "Testing - Unit testing, unittest, pytest, test-driven development (TDD)",
                    "Packaging & Deployment - Creating packages, setup.py, virtual environments in production, Docker, CI/CD",
                    "Web Development - Flask, Django, REST APIs, authentication",
                    "Data Science - NumPy, Pandas, Matplotlib, machine learning basics",
                    "Automation & Scripting - Web scraping, task automation, Selenium, scheduling scripts",
                    "Large-Scale Projects - Code architecture, design patterns, logging & monitoring, version control best practices"
                ]
            },
            "Software Developer": {
                "Beginner": [
                    "Programming Fundamentals (Python/JavaScript)",
                    "Version Control (Git)",
                    "Basic Data Structures & Algorithms",
                    "Web Development Basics (HTML/CSS)",
                    "Database Fundamentals (SQL)",
                    "Build First Project"
                ],
                "Intermediate": [
                    "Advanced Programming Concepts",
                    "Framework Learning (React/Django)",
                    "API Development & Integration",
                    "Testing & Debugging",
                    "Cloud Basics (AWS/Azure)",
                    "System Design Fundamentals"
                ],
                "Advanced": [
                    "Microservices Architecture",
                    "DevOps & CI/CD",
                    "Advanced System Design",
                    "Performance Optimization",
                    "Security Best Practices",
                    "Leadership & Mentoring"
                ]
            },
            "Data Scientist": {
                "Beginner": [
                    "Python Programming",
                    "Statistics & Mathematics",
                    "Data Manipulation (Pandas)",
                    "Data Visualization (Matplotlib/Seaborn)",
                    "SQL & Databases",
                    "First ML Project"
                ],
                "Intermediate": [
                    "Machine Learning Algorithms",
                    "Feature Engineering",
                    "Model Evaluation & Validation",
                    "Deep Learning Basics",
                    "Big Data Tools (Spark)",
                    "MLOps Fundamentals"
                ],
                "Advanced": [
                    "Advanced ML Techniques",
                    "Production ML Systems",
                    "A/B Testing & Experimentation",
                    "Advanced Statistics",
                    "Research & Publications",
                    "Team Leadership"
                ]
            },
            "DevOps Engineer": {
                "Beginner": [
                    "Version Control & Linux (Git/GitHub, Linux commands, file systems)",
                    "Containerization Basics (Docker fundamentals, images, Dockerfile)",
                    "CI/CD Concepts (continuous integration/deployment, pipeline basics)",
                    "Cloud Platforms Basics (AWS/Azure/GCP introduction, basic services)",
                    "Infrastructure Basics (servers, networking, monitoring fundamentals)",
                    "Scripting Basics (Bash, Python for automation)"
                ],
                "Intermediate": [
                    "Docker Advanced & Kubernetes (Docker Compose, K8s pods, services, deployments)",
                    "CI/CD Implementation (Jenkins, GitHub Actions, pipeline automation)",
                    "Infrastructure as Code (Terraform basics, HCL, cloud resource management)",
                    "Configuration Management (Ansible playbooks, inventory, automation)",
                    "Monitoring & Logging (Prometheus, Grafana, ELK stack, alerting)",
                    "Intermediate Projects (automated deployments, monitoring setup)"
                ],
                "Advanced": [
                    "Kubernetes Advanced (Helm charts, operators, scaling, rolling updates)",
                    "Advanced IaC & Automation (Terraform modules, Ansible roles, large-scale automation)",
                    "Production Systems (performance tuning, security hardening, compliance)",
                    "Advanced Monitoring (centralized logging, alert optimization, SRE practices)",
                    "Cloud Architecture (multi-cloud, disaster recovery, cost optimization)",
                    "Enterprise DevOps (team leadership, process optimization, toolchain management)"
                ]
            }
        }
    
    def get_available_roles(self):
        return list(self.roadmaps.keys())
    
    def generate_roadmap(self, role, level):
        if role not in self.roadmaps:
            return None
        if level not in self.roadmaps[role]:
            return None
        return self.roadmaps[role][level]

def main():
    generator = RoadmapGenerator()
    
    print("=== Personalized Learning Roadmap Generator ===\n")
    
    # Role selection
    print("Available Career Roles:")
    roles = generator.get_available_roles()
    for i, role in enumerate(roles, 1):
        print(f"{i}. {role}")
    
    try:
        role_choice = int(input("\nSelect a role (1-20): ")) - 1
        selected_role = roles[role_choice]
    except (ValueError, IndexError):
        print("Invalid selection!")
        return
    
    # Level selection
    print(f"\nSkill Levels for {selected_role}:")
    levels = ["Beginner", "Intermediate", "Advanced"]
    for i, level in enumerate(levels, 1):
        print(f"{i}. {level}")
    
    try:
        level_choice = int(input("\nSelect your level (1-3): ")) - 1
        selected_level = levels[level_choice]
    except (ValueError, IndexError):
        print("Invalid selection!")
        return
    
    # Generate and display roadmap
    roadmap = generator.generate_roadmap(selected_role, selected_level)
    
    print(f"\n=== Learning Roadmap: {selected_role} ({selected_level}) ===")
    for i, step in enumerate(roadmap, 1):
        print(f"{i}. {step}")
    
    print(f"\nTotal Steps: {len(roadmap)}")
    print("Good luck on your learning journey! 🚀")

if __name__ == "__main__":
    main()