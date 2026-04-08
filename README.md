Refactor the compliance dashboard UI to improve usability, responsiveness, and visual hierarchy.

Requirements:

Remove horizontal scrolling from the ITOP2 and IDAM5 summary sections.

Replace scrollable containers with a responsive CSS grid or flex layout.

Ensure all summary cards are visible in a single glance on desktop screens.

Use breakpoints:

Desktop: 4–6 cards per row

Tablet: 2–3 cards per row

Mobile: 1 card per row

Merge ITOP2 and IDAM5 summaries into a unified "Overview" section.

Either group them with headings or combine into a single set of key metrics.

Prioritize important metrics like "Total Violations" and "Non-Compliant".

Redesign summary cards:

Add clear visual hierarchy (larger cards for critical metrics).

Include icons for each metric.

Use consistent color coding:

Red for high risk

Yellow for warnings

Green for healthy metrics

Add hover effects and subtle shadows.

Improve chart section:

Add labels and percentages inside donut charts.

Ensure consistent color mapping across charts.

Add tooltips and legends for clarity.

Improve spacing and alignment.

Enhance the "Top Risky Applications" section:

Add ranking numbers (#1, #2, etc.)

Show percentage or severity indicator

Improve bar chart readability

Improve table UX:

Make table header sticky

Enable sorting on columns

Highlight rows with high non-compliance

On row click, dynamically update the "Application Details" panel

General UI improvements:

Add consistent padding and spacing between sections

Use a max-width container to avoid stretched layout

Improve typography (font sizes, weights)

Ensure accessibility (contrast, readable text)

Ensure the entire dashboard is fully responsive and visually balanced without requiring horizontal scrolling.
