# Week 7 Write-up
Tip: To preview this markdown file
- On Mac, press `Command (⌘) + Shift + V`
- On Windows/Linux, press `Ctrl + Shift + V`

## Instructions

Fill out all of the `TODO`s in this file.

## Submission Details

Name: **TODO** \
SUNet ID: **TODO** \
Citations: **TODO**

This assignment took me about **TODO** hours to do. 


## Task 1: Add more endpoints and validations
a. Links to relevant commits/issues
> https://github.com/Daniel-N0/modern-software-dev-assignments/commit/7f336685d3414c86af02c17f3c24893d33e7712e & > PR: https://github.com/Daniel-N0/modern-software-dev-assignments/pull/1

b. PR Description
> This PR implements Task 1 by adding new API endpoints, improving validation, and enhancing error handling for the notes feature. A DELETE endpoint (/notes/{note_id}) was introduced to allow removal of notes. Input validation was improved using Pydantic Field constraints to enforce minimum and maximum lengths. Error handling was enhanced by returning appropriate HTTP status codes such as 404 for missing resources and 422 for validation errors. Additionally, database operations were improved by replacing flush() with commit() to ensure data persistence.

c. Graphite Diamond generated code review
> Graphite Diamond did not identify any critical issues in the code. The implementation was considered clean and aligned with best practices. Minor improvements such as code consistency and structure were implicitly satisfied, and no major changes were required.

## Task 2: Extend extraction logic
a. Links to relevant commits/issues
> https://github.com/Daniel-N0/modern-software-dev-assignments/commit/7f336685d3414c86af02c17f3c24893d33e7712e & > PR: https://github.com/Daniel-N0/modern-software-dev-assignments/pull/2

b. PR Description
> This PR implements Task 2 by enhancing the action item extraction logic with more flexible and comprehensive keyword-based detection. Improvements include adding keyword-based detection, making the logic case-insensitive, preserving existing rules such as "todo:" prefix and "!" suffix, improving schema validation using Pydantic Field constraints, adding Optional typing for patch operations, and fixing SQLite teardown issues using engine.dispose().

c. Graphite Diamond generated code review
> Graphite Diamond did not identify any issues in the code. The implementation was considered clean, well-structured, and aligned with best practices, with no critical improvements required.

## Task 3: Try adding a new model and relationships
a. Links to relevant commits/issues
> TODO

b. PR Description
> TODO

c. Graphite Diamond generated code review
> TODO

## Task 4: Improve tests for pagination and sorting
a. Links to relevant commits/issues
> TODO

b. PR Description
> TODO

c. Graphite Diamond generated code review
> TODO

## Brief Reflection 
a. The types of comments you typically made in your manual reviews (e.g., correctness, performance, security, naming, test gaps, API shape, UX, docs).
> TODO 

b. A comparison of **your** comments vs. **Graphite’s** AI-generated comments for each PR.
> TODO

c. When the AI reviews were better/worse than yours (cite specific examples)
> TODO

d. Your comfort level trusting AI reviews going forward and any heuristics for when to rely on them.
>TODO 



