# Acceptance Criteria (BDD Format)

Every User Story MUST have Acceptance Criteria written in Behavior-Driven Development (BDD) format.

## The Format

**Scenario:** [Name of the scenario]
**Given** [Initial context/state]
**When** [Action taken by the persona]
**Then** [Observable outcome/result]
**And** [Additional outcomes, if any]

## Example
*   **Story:** As a user, I want to reset my password so that I can regain access if I forget it.
*   **Scenario 1:** Successful password reset email.
    *   **Given** the user is on the login page
    *   **When** they click "Forgot Password" and enter a valid registered email
    *   **Then** the system should send a password reset link to that email
    *   **And** display a success message on the screen.
*   **Scenario 2:** Unregistered email.
    *   **Given** the user is on the forgot password page
    *   **When** they enter an email that is not registered in the system
    *   **Then** the system should display a generic message "If your email is registered, a link has been sent" to prevent email enumeration attacks.