wildsafe
import React from "react";

function Filters({ filters, setFilters, onSearch }) {
  return (
    <div style={{ marginBottom: "20px" }}>
      <input
        placeholder="Cluster"
        value={filters.cluster}
        onChange={(e) =>
          setFilters({ ...filters, cluster: e.target.value })
        }
      />

      <input
        placeholder="Namespace"
        value={filters.namespace}
        onChange={(e) =>
          setFilters({ ...filters, namespace: e.target.value })
        }
      />

      <input
        placeholder="Pod"
        value={filters.pod}
        onChange={(e) =>
          setFilters({ ...filters, pod: e.target.value })
        }
      />

      <button onClick={onSearch}>Search</button>
    </div>
  );
}

export default Filters;
