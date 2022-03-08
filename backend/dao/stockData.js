const { stockData } = require('../models')

let stockDataDao = {
  findAll: findAll,
  create: create,
  findById: findById,
  customSearch: customSearch,
  deleteById: deleteById,
  updateStockData: updateStockData
}

function findAll() {
  return stockData.findAll()
}

function findById(id) {
  return stockData.findByPk(id)
}

function customSearch(source, acronym) {
  return stockData.findAll({
    where: { source, acronym }
  })
}

function deleteById(id) {
  return stockData.destroy({ where: { id: id } })
}

function create(newStockData) {
  return stockData.create(newStockData)
}

function updateStockData(newStockData, id) {
  let updatedStockData = {
      source: newStockData.source,
      acronym: newStockData.acronym,
      name: newStockData.name,
      sector: newStockData.sector,
      priceProfitRatio: newStockData.priceProfitRatio,
      netWorth: newStockData.netWorth
  }
  return stockData.update(updatedStockData, { where: { id: id } })
}
module.exports = stockDataDao