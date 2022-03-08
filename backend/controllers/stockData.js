const stockDataDao = require('../dao/stockData')

let stockData = {
    addStockData: addStockData,
    findStockData: findStockData,
    findStockDataById: findStockDataById,
    getYahooStockData: getYahooStockData,
    getFundamentusStockData: getFundamentusStockData,
    updateStockData: updateStockData,
    deleteById: deleteById
}

function addStockData(req, res) {
    let stockData = req.body
    stockDataDao.create(stockData)
        .then((data) => {
            res.send(data)
        })
        .catch((error) => {
            console.log(error)
        })
}

function findStockDataById(req, res) {
    stockDataDao.findById(req.params.id)
        .then((data) => {
            res.send(data)
        })
        .catch((error) => {
            console.log(error)
        })
}

function getYahooStockData(req, res) {
  stockDataDao.customSearch('yahoo', req.params.acronym)
        .then((data) => {
            res.send(data)
        })
        .catch((error) => {
            console.log(error)
        })
}

function getFundamentusStockData(req, res) {
    stockDataDao.customSearch('fundamentus', req.params.acronym)
        .then((data) => {
            res.send(data)
        })
        .catch((error) => {
            console.log(error)
        })
}

function deleteById(req, res) {
    stockDataDao.deleteById(req.params.id)
        .then((data) => {
            res.status(200).json({
                message: "Stock data deleted successfully",
                stockData: data
            })
        })
        .catch((error) => {
            console.log(error)
        })
}

function updateStockData(req, res) {
    stockDataDao.updateStockData(req.body, req.params.id)
        .then((data) => {
            res.status(200).json({
                message: "Stock data updated successfully",
                stockData: data
            })
        })
        .catch((error) => {
            console.log(error)
        })
}

function findStockData(req, res) {
    stockDataDao.findAll()
        .then((data) => {
            res.send(data)
        })
        .catch((error) => {
            console.log(error)
        })
}

module.exports = stockData