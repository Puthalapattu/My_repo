import pkg from "pg";

const { Client } = pkg;

const client = new Client({
  host: "localhost",
  port: 5432,
  user: "postgres",
  password: "Deepak@2552003",
  database: "postgres",
});

let UserData = "";

client.connect();

client.query(`SELECT * FROM Users`, (err, res) => {
  if (!err) {
    console.log(res.rows);
    UserData = res.rows;
    console.log("assignment Complete");
  } else {
    console.log("Error:" + err.message);
  }
  client.end;
});

export default UserData;
