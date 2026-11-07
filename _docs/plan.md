# Weekly Team Feedback Tool
## Product Requirements Specification (PRD)

**Version:** 0.1  
**Status:** Initial MVP specification  
**Platform:** Web application

---

## 1. Product Overview

The Weekly Team Feedback Tool is a web application designed to improve continuous team communication and reflection through structured weekly feedback cycles and team retrospectives.

The application uses the Start / Stop / Continue methodology.

Team members submit feedback individually throughout the week. At a scheduled time, a retrospective begins, allowing team members to review and discuss feedback collectively.

The application prioritizes simplicity, ease of use, and a predictable weekly workflow.

## 2. Product Goals

The primary goals are:

1. Make weekly feedback collection easier.
2. Make team retrospectives more effective.
3. Improve continuous team communication and reflection.

## 3. MVP Scope

### Included
- One team per installation.
- Team administration.
- Member invitations by email.
- Admin and member roles.
- Automatic recurring weekly cycles.
- Start / Stop / Continue feedback submission.
- Feedback editing and deletion.
- Scheduled retrospective activation.
- Shared retrospective feedback board.
- Weekly cycle closure.
- Historical cycle archiving.

### Excluded
- Multiple teams.
- Anonymous feedback.
- Notifications.
- Action-item management.
- Advanced analytics and reporting.
- Project management functionality.
- Advanced retrospective facilitation tools.
- Custom role and permission management.

## 4. User Roles

### 4.1 Team Admin

The admin is responsible for managing the team.

Permissions:
- Participate in feedback cycles like any other member.
- Invite members through email.
- Remove members.
- Configure the weekly schedule.
- Select the team timezone.
- Access historical feedback cycles.

Restrictions:
- Cannot change member roles or permissions.
- Cannot view other members' feedback before the retrospective begins, subject to the same participation rules.

### 4.2 Team Member

Permissions:
- Submit feedback.
- Edit and delete personal feedback until the weekly cycle ends.
- View other members' feedback when the retrospective is active and their own submission is complete.
- Participate in team retrospectives.

Restrictions:
- Cannot manage team membership.
- Cannot configure the weekly schedule.
- Cannot access historical cycles.

## 5. Weekly Feedback Cycle

The application must automatically create recurring weekly feedback cycles according to the schedule configured during initial team setup.

### 5.1 Feedback Categories

Every cycle contains three categories:

- **Start:** Things the team should start doing.
- **Stop:** Things the team should stop doing.
- **Continue:** Things the team should continue doing.

Each category has one text field per member.

Requirements:
- Members may leave individual categories empty.
- At least one category must contain feedback before submission is accepted.
- Feedback is associated with its author.
- Feedback is not anonymous.
- Members can edit or delete their submissions until the weekly cycle ends.

### 5.2 Feedback Visibility

Before the retrospective begins:
- Feedback content is hidden from other members.
- Participation status is hidden from other members.
- Members cannot view other members' submissions.

When the retrospective begins:
- Submitted feedback becomes available for team discussion.
- Each member must submit their own feedback before viewing other members' feedback.
- Members who have not submitted can still submit during the retrospective.

## 6. Retrospective

The retrospective begins automatically at its configured weekly time.

Requirements:
- All team members can participate.
- The admin participates like any other member.
- Feedback is displayed in a shared board.
- Feedback is grouped into Start, Stop, and Continue.
- All available feedback is displayed together rather than requiring a guided category-by-category process.
- Members can continue submitting feedback during the retrospective.
- Members can edit or delete their feedback until the weekly cycle ends.

The retrospective does not require an action-item management system in the MVP.

## 7. Weekly Cycle Closure

Each cycle ends at a fixed scheduled time, regardless of whether the retrospective has finished.

When the cycle ends:
- Feedback submissions are closed.
- Editing and deletion are disabled.
- The cycle is archived.
- Historical feedback becomes accessible to the admin only.

## 8. Team Setup and Membership

The first admin account is created through a predefined setup process.

During team setup, the admin:
- Establishes the team.
- Configures the recurring weekly schedule.
- Selects the team's timezone.

The admin can invite members through email and remove existing members.

There is one designated admin. Role promotion and custom permission management are outside MVP scope.

## 9. Scheduling and Timezone

The weekly schedule is configured once during team setup and repeats automatically.

The team selects its timezone during setup.

All cycle scheduling and retrospective activation must respect the selected team timezone.

The exact weekly start, retrospective, and closing times must be configurable as part of setup.

## 10. Notifications

The MVP does not include:
- Email notifications for weekly events.
- In-app notifications.
- Reminder systems.

Email invitations remain supported as part of team onboarding.

## 11. Historical Data

Completed cycles are archived.

Only the team admin can access historical cycles.

Team members cannot browse previous cycles.

Historical records should preserve:
- Cycle dates.
- Team feedback.
- Feedback authors.
- Feedback categories.

## 12. Core User Journey

1. Admin completes initial team setup.
2. Admin configures the weekly schedule and timezone.
3. Admin invites team members.
4. A weekly cycle starts automatically.
5. Members submit their individual feedback.
6. The retrospective starts automatically.
7. Members submit their own feedback if they have not already done so.
8. Members review and discuss the shared feedback board.
9. The cycle closes automatically.
10. Feedback is archived and becomes accessible to the admin.

## 13. MVP Design Principles

- Simple and intuitive interface.
- Minimal configuration.
- Clear weekly cycle status.
- No unnecessary features.
- Consistent user experience for admin and members.
- Responsive web interface.
- Clear separation between feedback submission and retrospective visibility.

## 14. Acceptance Criteria

The MVP is considered functionally complete when:

1. An admin can complete initial team setup.
2. The admin can invite and remove members.
3. The team can configure a recurring weekly schedule and timezone.
4. Weekly cycles start automatically.
5. Members can submit feedback in the three categories.
6. Empty submissions are rejected.
7. Members can edit and delete their feedback until cycle closure.
8. Feedback remains hidden before the retrospective.
9. Participation status remains hidden before the retrospective.
10. The retrospective activates automatically.
11. Members must submit their own feedback before viewing other members' feedback.
12. All team members can participate in the retrospective.
13. Feedback is grouped by category.
14. The cycle closes automatically at the configured time.
15. Feedback becomes read-only after closure.
16. Historical cycles are accessible only to the admin.
17. The application does not generate email or in-app event notifications.

---

**End of initial MVP specification.**