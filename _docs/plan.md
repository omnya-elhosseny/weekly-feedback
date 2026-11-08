# Weekly Team Feedback Tool
## Product Requirements Specification (PRD)

**Version:** 0.2
**Status:** MVP scope
**Platform:** Web application

---

## 1. Product Overview

The Weekly Team Feedback Tool is a web application for structured Start / Stop / Continue feedback and team retrospectives. Each cycle is started and ended by the team administrator. Members submit feedback individually, and the administrator opens the retrospective when the team is ready.

The MVP prioritizes a simple, manually controlled cycle with clear privacy and access rules. Recurring schedules, automatic cycle transitions, email invitations, and worker processes are post-MVP.

## 2. Product Goals

1. Make weekly feedback collection easier.
2. Make team retrospectives more effective.
3. Improve continuous team communication and reflection.

## 3. MVP Scope

### Included
- One team per installation.
- Initial team and admin setup.
- Admin-created member accounts that are confirmed and usable immediately; no invitation email is sent.
- Admin and member roles.
- Admin-controlled cycle start, retrospective opening, and cycle closure.
- Start / Stop / Continue feedback submission.
- Feedback editing and deletion until the admin closes the cycle.
- Shared retrospective feedback board.
- Historical cycle archiving, accessible to the admin only.
- PostgreSQL configured and run locally with Docker.

### Post-MVP
- Email invitations and invitation acceptance links.
- Configurable recurring weekly schedule and team timezone.
- Automatic recurring cycle creation and transitions.
- Background worker and scheduler configuration.

### Excluded
- Multiple teams.
- Anonymous feedback.
- Notifications and reminders.
- Action-item management.
- Advanced analytics and reporting.
- Project management functionality.
- Advanced retrospective facilitation tools.
- Custom role and permission management.

## 4. User Roles

### 4.1 Team Admin

The admin manages the team and cycle lifecycle.

Permissions:
- Participate in feedback cycles like any other member.
- Create and remove member accounts.
- Start a cycle, open its retrospective, and close it.
- Access historical feedback cycles.

Restrictions:
- Cannot change member roles or permissions.
- Cannot view other members' feedback before the retrospective begins, subject to the same participation rules.

### 4.2 Team Member

Permissions:
- Submit feedback.
- Edit and delete personal feedback until the admin closes the cycle.
- View other members' feedback when the retrospective is active and their own submission is complete.
- Participate in team retrospectives.

Restrictions:
- Cannot manage team membership or cycle state.
- Cannot access historical cycles.

## 5. Feedback Cycle

The MVP supports one active cycle at a time. The admin starts a cycle and later opens the retrospective and closes the cycle using explicit actions. A cycle has a start time, retrospective-open time, and close time recorded by the application; it does not repeat automatically.

### 5.1 Feedback Categories

Every cycle contains three categories:
- **Start:** Things the team should start doing.
- **Stop:** Things the team should stop doing.
- **Continue:** Things the team should continue doing.

Members may leave individual categories empty, but at least one category must contain feedback before submission is accepted. Feedback is attributed to its author and can be edited or deleted until cycle closure.

### 5.2 Feedback Visibility

Before the admin opens the retrospective, feedback content and participation status are hidden from other members. Each member can view only their own submission.

After the retrospective opens, submitted feedback becomes available for discussion, but a member must submit their own feedback before viewing other members' feedback. Members may still submit during the retrospective.

## 6. Retrospective

The admin opens the retrospective manually. All team members can participate. Feedback appears together on a shared board grouped by Start, Stop, and Continue. Members can continue submitting and editing feedback until the cycle is closed.

The retrospective does not require an action-item management system in the MVP.

## 7. Cycle Closure and History

The admin closes the cycle manually. On closure, submissions become read-only and the cycle is archived. Only the admin can access historical cycles; members cannot browse previous cycles.

Historical records preserve cycle dates, feedback, authors, and categories.

## 8. Team Setup and Membership

The first admin account is created through a predefined setup process. The admin establishes the team and can create and remove member accounts from the admin interface. Member accounts are confirmed and usable immediately when created; onboarding email and invitation acceptance are not part of the MVP.

There is one designated admin. Role promotion and custom permission management are outside MVP scope.

## 9. Post-MVP Scheduling

The MVP does not configure a recurring schedule or team timezone. The admin controls each cycle’s start, retrospective opening, and closure directly. Post-MVP work may add recurring schedule settings, timezone handling, automatic cycle creation and transitions, and background scheduling services.

## 10. Notifications

The MVP does not include email invitations, email notifications, in-app notifications, or reminders.

## 11. Core User Journey

1. Admin completes initial team setup.
2. Admin creates member accounts; members can sign in immediately.
3. Admin starts a feedback cycle.
4. Members submit individual feedback.
5. Admin opens the retrospective.
6. Members review and discuss the shared board after submitting their own feedback.
7. Admin closes the cycle.
8. Feedback is archived and becomes accessible to the admin.

## 12. MVP Design Principles

- Simple and intuitive interface.
- Clear cycle status and explicit admin controls.
- Minimal configuration.
- Responsive web interface using Django templates, HTML, and plain CSS.
- Clear separation between feedback submission and retrospective visibility.

## 13. Acceptance Criteria

The MVP is functionally complete when:
1. An admin can complete initial team setup.
2. The admin can create and remove member accounts without sending invitation emails.
3. An admin can start, open the retrospective for, and close a cycle manually.
4. Members can submit feedback in the three categories; entirely empty submissions are rejected.
5. Members can edit and delete their feedback until cycle closure.
6. Feedback and participation status remain hidden before retrospective opening.
7. Members must submit their own feedback before viewing other members' feedback.
8. All team members can participate in the retrospective.
9. Feedback is grouped by category on the shared board.
10. Feedback becomes read-only after the admin closes the cycle.
11. Historical cycles are accessible only to the admin.
12. The application does not send invitation, notification, or reminder emails.
13. Local development can run PostgreSQL using Docker.

---

**End of MVP specification.**
