const express = require('express')
const router = express.Router()
const stockDataController = require('../controllers/stockData')

router.post('/', stockDataController.addStockData)
router.get('/', stockDataController.findStockData)
router.get('/Yahoo/:acronym', stockDataController.getYahooStockData)
router.get('/Fundamentus/:acronym', stockDataController.getFundamentusStockData)
router.put('/:id', stockDataController.updateStockData)
router.delete('/:id', stockDataController.deleteById)

module.exports = router
