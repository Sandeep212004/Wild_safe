I have a React dashboard application where the App.js file has grown to more than 1200 lines. 
It currently contains UI rendering, state management, API calls, data processing, charts, and tables all in one file.

Refactor this code into a clean, maintainable, component-based architecture.

Requirements:

1. Break the large App.js file into multiple smaller reusable React components based on logical responsibilities.
2. Identify logical sections of the UI and extract them into separate component files.
3. Move API calls into a dedicated service layer.
4. Move complex data processing or aggregation logic into utility/helper files.
5. Keep App.js minimal and focused on application layout and high-level state management.
6. Use modern React practices with functional components and hooks.
7. Pass data between components using props and keep state where it logically belongs.
8. Ensure no functionality is lost during the refactor.
9. Preserve the existing UI and behavior of the dashboard.
10. Organize the project into a scalable folder structure inside src (for example: components, pages, services, utils, etc).
