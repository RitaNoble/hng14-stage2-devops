const express = require('express');
const axios = require('axios');
const app = express();

const API_URL = process.env.REACT_APP_API_URL || "http://localhost:8000";

app.use(express.json());

app.post('/submit', async (req, res) => {
  try {
    const response = await axios.post(`${API_URL}/jobs`);
    res.json(response.data);
  } catch {
    return res.status(500).json({ error: "something went wrong" });
  }
});

app.get('/status/:id', async (req, res) => {
  try {
    const response = await axios.get(`${API_URL}/jobs/${req.params.id}`);
    res.json(response.data);
  } catch {
    return res.status(500).json({ error: "something went wrong" });
  }
});

app.listen(3001, () => {
  console.log('Frontend running on port 3001');
});

app.get('/', (req, res) => {
  res.json({ status: "frontend running" });
});
