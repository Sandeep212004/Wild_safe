I have a React dashboard application where App.js has grown to more than 1200 lines and currently contains routing logic, layout rendering, state management, API calls, data processing, and UI logic.

I want to refactor the code so that App.js becomes very small and only acts as the main layout and router.

Refactor the code with the following goals:

1. Move all dashboard-specific logic into dedicated view components inside the existing components folder.
2. Move API calls into the existing src/api layer.
3. Move data aggregation or transformation logic into helper functions.
4. Ensure App.js only:
   - defines the main layout (Header + Sidebar)
   - manages high-level navigation or routing
   - renders the appropriate view component
5. Each view component should handle its own state and data fetching if needed.
6. Reuse the existing components already present in the project such as:
   - Dashboard
   - GBGFView
   - PlatformView
   - ApplicationSearchView
   - Kci views
   - Kpi views
7. Avoid duplicating logic across components.
8. Maintain the current UI and functionality exactly as it is.
9. Use functional React components and hooks.
10. Ensure the final App.js file is under 150 lines.

Provide:
- the refactored App.js
- any helper wrapper components that should be created
- updated imports
