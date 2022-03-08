const Sequelize = require('sequelize')
const sequelize = require('../config/sequelize')

const StockData = require('./stockData')
const stockData = StockData(sequelize, Sequelize.DataTypes)

const db = {
  stockData,
  sequelize
}

module.exports = db
