const express = require('express');
const { Client } = require('pg');
require('dotenv').config()

const database = process.env.database

const app = express();
const port = 5000;

const client = new Client({
    host: "127.0.0.1",
    port: 5432,
    database: database,
});

client.connect();

app.get('/pl_calendar', async (req, res) => {
    const { rows }  = await client.query(`SELECT * from pl_calendar`) 
    res.send(rows)

})

app.listen(port, () => {
    console.log(`Listening on port ${port}`)
})

