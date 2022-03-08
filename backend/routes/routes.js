
const express = require('express');
const router = express.Router();
const stockDataRouter = require('./stock-data');

router.use('/stock-data', stockDataRouter);
module.exports = router;