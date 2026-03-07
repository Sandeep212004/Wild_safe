Currently all the logic and UI are written inside App.js, which makes the file very large and hard to maintain.

Refactor the code by creating a new file called app2.js.

Requirements:
1. app2.js should contain only the layout and structural components of the application.
2. No business logic, API calls, or data processing should exist in app2.js.
3. Move logic into reusable components inside the components folder.
4. Reuse existing components from the components directory wherever possible.
5. If some logic does not belong to an existing component, create a new component inside the components folder.
6. The behavior of the application should remain exactly the same as App.js.

Goal:
Keep app2.js clean and minimal, focusing only on layout and composition of components.
