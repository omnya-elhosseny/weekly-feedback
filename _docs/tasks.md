# Weekly Team Feedback Tool Backlog

Tasks marked **Post-MVP** are deferred from the initial release. Create or label their GitHub issues `post-mvp` so they do not block MVP delivery.

##  Create an empty Django project with a passing test
**MVP**
Goal: Establish a minimal, runnable Django project and prove its test setup works.
Description: Create the Django project scaffold using server-rendered pages, with no product features or application data models. Add a basic health page and document the test command.

##  Add local development and environment configuration
**MVP**
Goal: Make the project straightforward to configure and run locally.
Description: Document required environment variables and provide safe development defaults for Django secret key, debug mode, allowed hosts, and database connection. Add an example environment file with placeholders only, and ensure secrets are not committed.

##  Run PostgreSQL for development with Docker
**MVP**
Goal: Provide a repeatable local PostgreSQL database using Docker.
Description: Add a Docker Compose configuration for PostgreSQL with environment-based credentials, a persistent named data volume, and a health check. Document how to start and stop the database, configure Django to connect to it, and run migrations. Keep real credentials out of source control and preserve a clear path for isolated test databases.

##  Add a shared server-rendered page layout
**MVP**
Goal: Provide a consistent, responsive base layout for the application.
Description: Create Django templates and plain CSS for a shared page shell with navigation, content area, and visible page titles. Ensure the layout works on narrow and wide screens without requiring a frontend framework.

##  Set up account login and logout
**MVP**
Goal: Let team members securely sign in and out.
Description: Use Django’s built-in authentication views and server-rendered forms. Require authentication on private application pages and show clear validation feedback without exposing account secrets.

##  Create the single-team setup flow
**MVP**
Goal: Let the first administrator establish the installation’s team and initial account.
Description: Build a one-time setup page that collects the team name and first administrator’s account details, then creates the team and marks that account as its administrator. Prevent public creation of additional teams or a second initial administrator through this flow.

##  Define team membership and the designated administrator
**MVP**
Goal: Represent the one-team membership model and its two supported roles.
Description: Add data structures for the single team, its members, and the designated administrator using Django’s authentication system where appropriate. Enforce one team per installation and one designated administrator, with ordinary members as the only other role.

##  Build administrator member management
**MVP**
Goal: Allow the administrator to create and remove member accounts.
Description: Provide server-rendered administrator pages to create a member with a confirmed, immediately usable account and remove an existing member. Do not send an invitation email. Ensure only the designated administrator can manage accounts and removed members can no longer access team feedback.

##  Confirm member accounts at creation without invitations
**MVP**
Goal: Let members use accounts created by the administrator without email onboarding.
Description: Treat an administrator-created member account as confirmed and available for login immediately. Do not generate invitation tokens, send emails, or require an acceptance step. Keep authentication and password handling secure.

##  Add administrator controls for the manual cycle lifecycle
**MVP**
Goal: Let the administrator explicitly start, open the retrospective for, and close a cycle.
Description: Add administrator-only actions to start one cycle, open its retrospective, and close it. Record lifecycle timestamps and enforce valid transitions and one active cycle at a time. Do not add recurring schedule settings or automatic transitions.

##  Create and store a cycle when the administrator starts it
**MVP**
Goal: Persist the cycle and its lifecycle state for feedback workflows.
Description: Create a cycle record when the admin starts a cycle, record its start time, and update its state through the manual controls. Prevent a second active cycle and make invalid or repeated transitions safe.

##  Add background worker and recurring scheduler configuration
**Post-MVP**
Goal: Run recurring cycle jobs reliably outside web requests.
Description: Configure Celery workers and Celery Beat for automatic weekly cycle creation, retrospective activation, and closure. Document local commands and deployment process roles. Ensure missed or retried jobs can run safely without duplicating cycle transitions. Track this work in GitHub with the `post-mvp` label.

##  Build the personal Start / Stop / Continue submission form
**MVP**
Goal: Let each member submit one feedback entry with three categories for the active cycle.
Description: Add a server-rendered form for Start, Stop, and Continue text, allowing any individual category to be blank while requiring at least one non-empty category. Associate the entry with its author and active cycle and show a clear validation message for an entirely empty submission.

##  Allow members to edit and delete their own feedback
**MVP**
Goal: Give members control over their submission until the cycle closes.
Description: Let an authenticated member update or delete only their own feedback for the active cycle while it remains open. Reject changes after closure and prevent members from changing another person’s entry.

##  Enforce private feedback before the retrospective
**MVP**
Goal: Keep feedback and participation hidden from other members until the admin opens the retrospective.
Description: Apply server-side access checks to every page and request that could reveal another member’s feedback or submission status. Before the retrospective is opened, members can see and edit only their own entry, and the interface must not reveal who has or has not submitted.

##  Activate the retrospective automatically on schedule
**Post-MVP**
Goal: Open the shared feedback board automatically at its configured recurring time.
Description: Use the background scheduler to activate the retrospective at the configured local time. Make the transition safe to retry and ensure the board reflects the active state even if the scheduled job is delayed. Track this work in GitHub with the `post-mvp` label.

##  Build the shared retrospective board
**MVP**
Goal: Let eligible members review cycle feedback grouped by category.
Description: Display submitted entries together in Start, Stop, and Continue groups after the admin opens the retrospective. Require a member to submit their own feedback before showing anyone else’s, while still allowing members without a submission to submit during the retrospective.

##  Close cycles and lock feedback automatically on schedule
**Post-MVP**
Goal: End recurring cycles automatically and make feedback read-only.
Description: Close the cycle at its configured time regardless of retrospective activity, and reject new submissions, edits, and deletions after closure. Make the operation safe to retry and show the closed status clearly. Track this work in GitHub with the `post-mvp` label.

##  Provide administrator-only cycle history
**MVP**
Goal: Let the administrator review archived cycles while members cannot browse past feedback.
Description: Add an administrator-only history page listing completed cycles and their dates, with each archived board preserving feedback, author, and category. Enforce the restriction on the server for list and detail pages.

##  Add authorization and visibility coverage for core workflows
**MVP**
Goal: Verify role and feedback visibility rules with automated tests.
Description: Add tests for administrator-only member management and history, member access limits, pre-retrospective privacy, submit-before-view behavior, author-only edits, and closed-cycle immutability. Cover allowed and denied requests so access rules are checked independently of page presentation.

##  Document deployment and operation
**MVP; recurring scheduler guidance is Post-MVP**
Goal: Give an operator enough information to run and deploy the MVP.
Description: Document Docker-based PostgreSQL, environment configuration, migrations, static files, and the web process. Include a concise release checklist. Add worker and scheduler process guidance when the post-MVP scheduling work is implemented.

## Post-MVP follow-up: recurring schedule configuration
**Post-MVP**
Goal: Let the administrator configure when weekly cycles start, retrospectives open, and cycles close.
Description: Add an administrator-only recurring schedule form and IANA timezone support. Validate the configured times and display them in the selected timezone. Coordinate this work with task 12 and track its GitHub issue with the `post-mvp` label.

## Post-MVP follow-up: email invitations
**Post-MVP**
Goal: Let invited people activate team accounts through email.
Description: Send a secure, expiring acceptance link and create or activate the invited member account when accepted. Keep this email limited to onboarding; do not add weekly event notifications or reminders. Track this work in GitHub with the `post-mvp` label.
