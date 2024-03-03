import {
  flexRender,
  getCoreRowModel,
  getFilteredRowModel,
  getPaginationRowModel,
  getSortedRowModel,
  useReactTable,
} from "@tanstack/react-table";
import { useState } from "react";
import "bootstrap/dist/css/bootstrap.css";
import "../app.css";

function BasicTable({ data, columns }) {
  const [sorting, setSorting] = useState([]);
  const [search, setSearch] = useState("");

  const table = useReactTable({
    data,
    columns,
    getCoreRowModel: getCoreRowModel(),
    getPaginationRowModel: getPaginationRowModel(),
    getSortedRowModel: getSortedRowModel(),
    getFilteredRowModel: getFilteredRowModel(),
    // setPageSize: 20,
    state: {
      sorting: sorting,
      globalFilter: search,
    },
    onSortingChange: setSorting,
    onGlobalFilterChange: setSearch,
  });

  //   console.log("table state:", table.pageSize);
  //   console.log("data length:", data.length);

  return (
    <div className="container">
      <input
        type="text"
        value={search}
        placeholder="Search Name or location"
        onChange={(e) => setSearch(e.target.value)}
      />
      <table
        className="table table-striped table-hover"
        style={"color: black;"}
      >
        <thead>
          {table.getHeaderGroups().map((headerGroup) => (
            <tr key={headerGroup.sno}>
              {headerGroup.headers.map((header) => (
                <th
                  key={header.sno}
                  onClick={header.column.getToggleSortingHandler()}
                >
                  {header.isPlaceholder ? null : (
                    <div>
                      {flexRender(
                        header.column.columnDef.header,
                        header.getContext()
                      )}
                      {
                        { asc: "🔽", desc: "🔼" }[
                          header.column.getIsSorted() ?? null
                        ]
                      }
                    </div>
                  )}
                </th>
              ))}
            </tr>
          ))}
        </thead>

        <tbody>
          {table.getRowModel().rows.map((row) => (
            <tr key={row.sno}>
              {row.getVisibleCells().map((cell) => (
                <td key={cell.sno}>
                  {flexRender(cell.column.columnDef.cell, cell.getContext())}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
      <div className="pages">
        <button onClick={() => table.setPageIndex(0)}>First page</button>
        <button
          disabled={!table.getCanPreviousPage()}
          onClick={() => table.previousPage()}
        >
          Previous page
        </button>
        <button
          disabled={!table.getCanNextPage()}
          onClick={() => table.nextPage()}
        >
          Next page
        </button>
        <button onClick={() => table.setPageIndex(table.getPageCount() - 1)}>
          Last page
        </button>
        <select
          value={table.options.state.pagination.pageSize}
          onChange={(e) => table.setPageSize(e.target.value)}
          placeholder="Select page Size"
        >
          {[20, 15, 10].map((pageSizeEl) => {
            return (
              <option key={pageSizeEl} value={pageSizeEl}>
                {pageSizeEl}
              </option>
            );
          })}
        </select>
      </div>
    </div>
  );
}

export default BasicTable;
