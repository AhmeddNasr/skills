# Use Case Points (UCP) Factor Guidelines

Use these guidelines to evaluate User Stories and determine the inputs for the `ucp_ucp_calculate_from_factors` tool.

## 1. Determine Actors and Use Cases
*   **Simple Actor:** Another system with a defined API.
*   **Average Actor:** Another system interacting through a protocol (e.g., TCP/IP), or a human using a simple text-based interface.
*   **Complex Actor:** A human interacting via a graphical user interface (GUI).
*   **Simple Use Case:** 1-3 transactions/steps.
*   **Average Use Case:** 4-7 transactions/steps.
*   **Complex Use Case:** >7 transactions/steps.

## 2. Technical Complexity Factors (TCF)
Rate each from 0 (Irrelevant) to 5 (Essential).
*   **T1:** Distributed System (Does it require networking/cloud distribution?)
*   **T2:** Response time or throughput performance objectives
*   **T3:** End-user efficiency (Is high usability critical?)
*   **T4:** Complex internal processing (Heavy math, algorithms, data processing)
*   **T5:** Reusable code (Is the system required to be built as reusable components?)
*   **T6:** Easy to install (Does it need automated/seamless installation?)
*   **T7:** Easy to use (Does it require high UX focus?)
*   **T8:** Portable (Does it need to run on multiple platforms/OS?)
*   **T9:** Easy to change (Is high maintainability/configuration required?)
*   **T10:** Concurrent (Will many users use it simultaneously?)
*   **T11:** Includes special security features (Encryption, strict auth)
*   **T12:** Provides direct access for third parties (External APIs)
*   **T13:** Special user training facilities are required

## 3. Environmental Complexity Factors (ECF)
Rate each from 0 (No experience/Low) to 5 (Expert/High).
*   **E1:** Familiarity with the project model that is used (e.g., UML)
*   **E2:** Application experience (Does the team know this business domain?)
*   **E3:** Object-oriented experience (Does the team know OOP?)
*   **E4:** Lead analyst capability (Is the lead BA experienced?)
*   **E5:** Motivation (Is the team highly motivated?)
*   **E6:** Stable requirements (Are the requirements locked in, or changing rapidly?)
*   **E7:** Part-time staff (0 = All part-time, 5 = All full-time dedicated)
*   **E8:** Difficulty of programming language (0 = Very hard language, 5 = Very easy language)