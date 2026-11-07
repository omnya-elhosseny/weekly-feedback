# Weekly Team Feedback Tool Backlog

## 1. Create an empty Django project with a passing test
Goal: Establish a minimal, runnable Django project and prove its test setup works.
Description: Create the Django project scaffold for the Weekly Team Feedback Tool using server-rendered pages, with no product features or application data models. Add one automated test that verifies the project responds successfully to a basic health page, and document the command used to run the test.

## 2. Add local development and environment configuration
Goal: Make the project straightforward to configure and run in a local development environment.
Description: Document required environment variables and provide safe development defaults for the Django secret key, debug mode, allowed hosts, and database connection. Add an example environment file with placeholders only, and ensure secrets are not committed.

## 3. Configure PostgreSQL for development and deployment
Goal: Run the application against PostgreSQL with repeatable database setup.
Description: Configure Django to use PostgreSQL through environment-provided connection settings and document how to create and migrate the database. Keep database credentials out of source control and preserve a clear path for isolated test databases.

## 4. Add a shared server-rendered page layout
Goal: Provide a consistent, responsive base layout for the application.
Description: Create Django templates and plain CSS for a shared page shell with navigation, content area, and visible page titles. Ensure the layout works on narrow and wide screens without requiring a frontend framework.

## 5. Set up account login and logout
Goal: Let team members securely sign in and out of the application.
Description: Use Django’s built-in authentication views and server-rendered forms for login and logout. Require authentication on private application pages and show clear validation feedback without exposing account secrets.

## 6. Create the single-team setup flow
Goal: Let the first administrator establish the installation’s team and initial account.
Description: Build a one-time setup page that collects the team name and the first administrator’s account details, then creates the team and marks that account as its administrator. Prevent public creation of additional teams or a second initial administrator through this setup flow.

## 7. Define team membership and the designated administrator
Goal: Represent the one-team membership model and its two supported roles.
Description: Add data structures for the single team, its members, and the designated administrator using Django’s authentication system where appropriate. Enforce one team per installation and one designated administrator, with ordinary members as the only other role.

## 8. Build administrator member management
Goal: Allow the administrator to invite and remove team members.
Description: Provide server-rendered administrator pages to invite a person by email and remove an existing member. Ensure only the designated administrator can use these actions and that a removed member can no longer access team feedback.

## 9. Send and accept email invitations
Goal: Let invited people activate their team accounts through email.
Description: Send an invitation email containing a secure, expiring acceptance link and create or activate the invited member’s account when the link is accepted. Keep this email limited to onboarding; the product does not send weekly event notifications or reminders.

## 10. Configure the recurring weekly schedule and team timezone
Goal: Let the administrator define when weekly cycles start, retrospectives open, and cycles close.
Description: Add an administrator-only settings form for the three weekly times and an IANA timezone. Validate the values and present the saved schedule in the selected team timezone so members can understand the cycle timing.

## 11. Create weekly cycles from the configured schedule
Goal: Ensure each recurring schedule produces a weekly feedback cycle.
Description: Add a background scheduling mechanism that creates the correct cycle for the team’s configured weekly start time, including after application restarts. Prevent duplicate cycles and calculate cycle boundaries using the team timezone, including daylight-saving transitions.

## 12. Add background worker and scheduler configuration
Goal: Run scheduled cycle jobs reliably outside web requests.
Description: Configure Celery workers and Celery Beat for the Django application, with documented local commands and deployment process roles. Include operational handling so missed or retried jobs can safely run without duplicating cycle transitions.

## 13. Build the personal Start / Stop / Continue submission form
Goal: Let each member submit one weekly feedback entry with three categories.
Description: Add a server-rendered form for Start, Stop, and Continue text, allowing any individual category to be blank while requiring at least one non-empty category. Associate the entry with its author and active weekly cycle, and show a clear validation message for an entirely empty submission.

## 14. Allow members to edit and delete their own feedback
Goal: Give members control over their submission until the cycle closes.
Description: Let an authenticated member update or delete only their own feedback for the active cycle while it remains open. Reject changes after closure and prevent members from changing another person’s entry.

## 15. Enforce private feedback before the retrospective
Goal: Keep feedback and participation hidden from other members before the retrospective opens.
Description: Apply server-side access checks to every page and request that could reveal another member’s feedback or submission status. Before the configured retrospective time, members can see and edit only their own entry, and the interface must not reveal who has or has not submitted.

## 16. Activate the retrospective on schedule
Goal: Open the shared feedback board automatically at its configured weekly time.
Description: Use the background scheduler to mark the current cycle’s retrospective active at the configured local time. Make the transition safe to retry and ensure the board reflects the active state even if the scheduled job was delayed.

## 17. Build the shared retrospective board
Goal: Let eligible members review all cycle feedback grouped by category.
Description: Display submitted entries together in Start, Stop, and Continue groups after the retrospective is active. Require a member to submit their own feedback before showing any other member’s feedback, while still allowing members without a submission to submit during the retrospective.

## 18. Close cycles and lock feedback on schedule
Goal: End each weekly cycle at its configured closing time and make feedback read-only.
Description: Close the cycle automatically regardless of retrospective activity, and reject new submissions, edits, and deletions after closure. Make the closure operation safe to retry and show the cycle’s closed status clearly.

## 19. Provide administrator-only cycle history
Goal: Let the administrator review archived cycles while members cannot browse past feedback.
Description: Add an administrator-only history page listing completed cycles and their dates, with each archived board preserving feedback, author, and category. Enforce the restriction on the server for both list and detail pages.

## 20. Add authorization and visibility coverage for core workflows
Goal: Verify the role and feedback visibility rules with automated tests.
Description: Add tests for administrator-only member management and history, member access limits, pre-retrospective privacy, submit-before-view behavior, author-only edits, and closed-cycle immutability. Cover both allowed and denied requests so access rules are checked independently of page presentation.

## 21. Document deployment and scheduled-process operation
Goal: Give an operator enough information to deploy and run the MVP reliably.
Description: Document required services, environment configuration, migrations, static files, web process, Celery worker, and Celery Beat scheduler. Include a concise release checklist and explain how to confirm recurring cycle transitions are running.
