const { stockData } = require('../models')

let stockDataDao = {
  findAll: findAll,
  create: create,
  findById: findById,
  findBySource: findBySource,
  deleteById: deleteById,
  updateStockData: updateStockData
}

function findAll() {
  return stockData.findAll()
}

function findById(id) {
  return stockData.findByPk(id)
}

function findBySource(source) {
  return stockData.findAll({
    where: { source }
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