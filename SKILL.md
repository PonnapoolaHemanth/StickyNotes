---
name: weekly-sticky-notes
description: Generates a single-file Weekly Notes web app where each '+' action creates a 7-page weekly note (Monday to Sunday) with per-day pages and instant localStorage auto-save. Make sure to use this skill whenever the user asks for a weekly notes app, week planner, 7-day journal, day-by-day notebook, or a Monday-to-Sunday notes tool, even if they don't name this skill or say "sticky notes".
---

# Weekly 7-Page Notes Builder

Build a minimalist, single-file web application (`index.html`) in the workspace root using vanilla HTML, CSS, and JavaScript with zero external dependencies.

## Core Workflow & UI Structure
1. **Weeks Overview (Home View):**
   - Clean light dot-grid background with a top bar containing a title and a **"+ New Week"** button.
   - Displays created weekly notes as cards showing the week label (defaulting to the current Monday–Sunday date range, editable inline), a quick preview of notes across the week, how many of the 7 days have entries, and a **Delete** button (with confirmation).
   - Clicking a week card opens that weekly note's 7-day view.

2. **Inside a Weekly Note (7-Day View):**
   - Top bar includes a **"← All Weeks"** back button, editable week title, and a **"Copy Week"** button that copies all days with content to the clipboard.
   - **7 Day Tabs:** `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday`, `Saturday`, `Sunday` in order.
   - Show a visual indicator on tabs that contain text, and highlight the active tab clearly.
   - Clicking a day tab switches immediately to that day's full-height writing area (`<textarea>` with placeholder like `"Write notes for Monday..."`).

## Persistence & Reliability
- Persist all weeks and all 7 day contents automatically to `localStorage` on every keystroke (`input` event), displaying a subtle `"Saved"` status badge.
- Handle missing or corrupted `localStorage` data safely so the app never crashes on load.
- Keep everything self-contained inside `index.html` so it opens directly in any browser or live preview.

## Implementation Notes
- Wrap every `localStorage` read/write in `try/catch`; fall back to an empty list if data is missing, invalid JSON, or the wrong shape.
- Render user text with `textContent` / `value`, never `innerHTML`.
- Compute the default week label from the local date (Monday start), e.g. "Nov 23 – Nov 29, 2026".
- Use `navigator.clipboard.writeText` with a hidden-textarea `execCommand('copy')` fallback, and confirm with a brief "Copied" message.
- Show a friendly empty state on the home view when no weeks exist.

## Execution Steps
1. Create or overwrite `index.html` with the complete application code.
2. Open the local preview or provide the local server/file link so the user can test it immediately.
