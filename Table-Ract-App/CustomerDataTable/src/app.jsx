import { useMemo } from "react";
import "./app.css";
import dumData from "./DummyData.json";
import BasicTable from "./components/UsersTable";

function App() {
  const data = useMemo(() => dumData, []);

  /** @type import('@tanstack/react-table').ColumnDef<any> */
  const dataColumns = [
    {
      header: "Sno",
      accessorKey: "sno",
    },
    {
      header: "Customer Name",
      accessorKey: "name",
    },
    {
      header: "Age",
      accessorKey: "age",
    },
    {
      header: "Phone",
      accessorKey: "phone",
    },
    {
      header: "Location",
      accessorKey: "location",
    },
    {
      header: "Created Date",
      accessorKey: "date",
    },
    {
      header: "Created Time",
      accessorKey: "time",
    },
  ];

  return (
    <>
      <h1>Customer Data</h1>
      <BasicTable data={data} columns={dataColumns} />
    </>
  );
}

export default App;
