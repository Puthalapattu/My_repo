import { useMemo } from "react";
import "./app.css";
import movies from "./DummyData.json";
import BasicTable from "./components/UsersTable";

function App() {
  const data = useMemo(() => movies, []);

  /** @type import('@tanstack/react-table').ColumnDef<any> */
  const dataColumns = [
    {
      header: "Sno",
      accessorKey: "sno",
    },
    {
      header: "Name",
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
  const columns = [
    {
      header: "ID",
      accessorKey: "id",
      footer: "ID",
    },
    {
      header: "Name",
      accessorKey: "first_name",
    },
    {
      header: "First name",
      accessorKey: "first_name",
      footer: "First name",
    },
    {
      header: "Last name",
      accessorKey: "last_name",
      footer: "Last name",
    },
    {
      header: "Email",
      accessorKey: "email",
      footer: "Email",
    },
    {
      header: "Gender",
      accessorKey: "gender",
      footer: "Gender",
    },
    {
      header: "Date of birth",
      accessorKey: "dob",
      footer: "Date of birth",
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
