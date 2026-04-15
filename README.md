I want to optimize performance significantly while keeping the DataFrame approach.

⸻

Step 1: Optimize DataFrame preprocessing (IMPORTANT)
	•	Modify _build_dataset() to preprocess and store:
	•	Lowercased application name column (e.g., _normalized_app)
	•	Precomputed status group column (e.g., _status_group)
	•	Ensure this preprocessing runs only once when dataset is loaded

⸻

Step 2: Optimize filtering logic
	•	Update apply_filters():
	•	Remove dataframe.copy() to avoid full DataFrame duplication
	•	Use precomputed _normalized_app instead of .str.lower() each time
	•	Use _status_group column instead of recalculating status
	•	Avoid expensive .apply() where possible

⸻

Step 3: Add backend pagination
	•	Implement a helper function:
    def paginate(df, page, limit):
    start = (page - 1) * limit
    end = start + limit
    return df.iloc[start:end]
  •	Ensure only paginated rows are returned to frontend

⸻

Step 4: Add fast summary computation
	•	Implement a function:
    def compute_summary(df):
    return {
        "total": len(df),
        "compliant": (df['_status_group'] == 'compliant').sum(),
        "non_compliant": (df['_status_group'] == 'nonCompliant').sum(),
        "out_of_scope": (df['_status_group'] == 'outOfReviewScope').sum()
    }
  •	Ensure summary is computed on filtered dataset (not paginated)

⸻

Step 5: Optimize serialize_dataset()
	•	Modify it to:
	•	Apply filters
	•	Compute summary
	•	Apply pagination
	•	Return only required columns (DISPLAY_FIELDS)
	•	Avoid sending full DataFrame

⸻

Step 6: Update Flask route
	•	Accept query params:
	•	page
	•	limit
	•	applicationName
	•	statusGroup
	•	statusDetail
	•	Pass pagination + filters to service layer

⸻

Step 7: Optimize memory and performance
	•	Avoid unnecessary .copy()
	•	Avoid repeated .fillna().astype(str).str.lower()
	•	Reuse cached dataset (_default_cache, _upload_cache)
	•	Ensure preprocessing is cached, not recomputed

⸻

Step 8: Optional improvements
	•	Add simple in-memory caching for repeated filter queries
	•	Ensure thread safety using existing locks
