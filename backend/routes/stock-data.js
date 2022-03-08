const express = require('express')
const router = express.Router()
const stockDataController = require('../controllers/stockData')

router.post('/', stockDataController.addStockData)
router.get('/', stockDataController.findStockData)
router.get('/yahoo', stockDataController.getYahooStockData)
router.get('/fundamentus', stockDataController.getFundamentusStockData)
router.put('/:id', stockDataController.updateStockData)
router.delete('/:id', stockDataController.deleteById)

module.exports = router
