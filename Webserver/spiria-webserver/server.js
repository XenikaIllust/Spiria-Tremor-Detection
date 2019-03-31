const express = require('express');
const pg = require('pg');
const bodyparser = require('body-parser');
const helmet = require('helmet');
const cors = require('cors')

const routes = require('/routes/')

const app = express();
const router = express.Router();

app.use(bodyparser.json());
app.use(cors());
