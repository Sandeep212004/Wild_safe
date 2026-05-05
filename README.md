wildsafe
import React, { useState, useEffect } from "react";
import { fetchPods } from "./services/api";
import Filters from "./components/Filters";
import PodTable from "./components/PodTable";

function App() {
  const [data, setData] = useState([]);
  const [filters, setFilters] = useState({
    cluster: "",
    namespace: "",
    pod: "",
  });

  // Load initial data
  useEffect(() => {
    loadData();
  }, []);

  const loadData = async () => {
    const res = await fetchPods(filters);
    setData(res);
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>IKP Metrics Dashboard</h2>

      <Filters
        filters={filters}
        setFilters={setFilters}
        onSearch={loadData}
      />

      <PodTable data={data} />
    </div>
  );
}

export default App;
