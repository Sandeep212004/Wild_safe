wildsafe
Refactor my existing React dashboard UI to look modern and minimal WITHOUT changing any business logic, API calls, or data structure.

Requirements:
- Keep all existing functionality exactly the same
- Only improve UI/UX and styling

Design updates:
1. Use a clean, minimal design with lots of whitespace
2. Replace bright colors with a soft palette (light gray background, white cards, muted text, one primary color like indigo or blue)
3. Convert all Pie Charts into modern Donut Charts (use innerRadius, spacing, and soft colors)
4. Replace at least one pie chart with a horizontal bar chart for better readability
5. Improve all cards:
   - Add border radius (12px–16px)
   - Add subtle shadow
   - Increase padding
   - Use better typography (larger numbers, smaller labels)
6. Use consistent spacing and alignment across the dashboard
7. Add hover effects and smooth transitions
8. Use a modern font like Inter or system-ui
9. Use reusable components (e.g., StatCard, ChartCard)

Tech constraints:
- Keep using React (no framework change)
- Prefer Tailwind CSS for styling (or clean CSS modules if already used)
- If charts are used (Recharts or similar), only modify their appearance, not data logic

Output:
- Updated React components
- Clean reusable UI components
- Improved styling only

Do NOT:
- Change props structure
- Change data fetching
- Change backend logic
