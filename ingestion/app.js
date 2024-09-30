
const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const axios = require('axios');

app.use(bodyParser.json());

app.post('/ingest', async (req, res) => {
    try {
        const data = req.body;
        await axios.post('http://backend:8000/api/ingest', data); // Forward to backend API
        res.status(201).send('Data ingested successfully');
    } catch (error) {
        res.status(500).send('Error ingesting data');
    }
});

app.listen(5000, () => {
    console.log('Ingestion service listening on port 5000');
});
