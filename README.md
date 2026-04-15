wildsa
My current Flask backend reads data using pandas.read_excel(), which is causing very slow initial load times (~1.5–2 minutes for large files ~200k rows).

I want to optimize the data loading process.

⸻

Step 1: Replace Excel reading with CSV
	•	Convert the Excel file to CSV once (offline or during upload)
	•	Replace:
pd.read_excel(…)
with:
pd.read_csv(…)
	•	Use optimized parameters:
	•	low_memory=True
	•	dtype=str (to avoid type inference overhead)

⸻

Step 2: Cache processed dataset to disk
	•	After first load and preprocessing, save processed DataFrame as:
	•	pickle (.pkl) OR parquet (.parquet)
	•	On next startup:
	•	Load directly from cached file instead of reprocessing Excel

⸻

Step 3: Optimize header detection
	•	Avoid iterating with iterrows()
	•	Use vectorized approach:
	•	count non-empty cells using df.notna().sum(axis=1)

⸻

Step 4: Optimize preprocessing
	•	Apply normalization using vectorized pandas operations only
	•	Avoid Python loops wherever possible

⸻

Step 5: Lazy load dataset
	•	Load dataset only once when server starts
	•	Store in global cache
	•	Do NOT reload on every request

⸻

Step 6: Optional (best performance)
	•	Use Parquet format:
df.to_parquet(“data.parquet”)
df = pd.read_parquet(“data.parquet”)

⸻

Expected Result:
	•	Initial load reduced from ~1.7 minutes → <10 seconds
	•	Subsequent requests near-instant
	•	No repeated heavy preprocessing

Update the code accordingly and explain changes.
