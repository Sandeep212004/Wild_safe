wildsafe
import React from "react";

import React from "react";

function PodTable({ data }) {
  if (!data.length) return <p>No data</p>;

  return (
    <table border="1">
      <thead>
        <tr>
          {Object.keys(data[0]).map((key) => (
            <th key={key}>{key}</th>
          ))}
        </tr>
      </thead>

      <tbody>
        {data.map((row, i) => (
          <tr key={i}>
            {Object.values(row).map((val, j) => (
              <td key={j}>{val}</td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default PodTable;
