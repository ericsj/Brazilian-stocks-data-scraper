const Sequelize = require('sequelize')
const databaseConfig = require('./database')

const db = new Sequelize(databaseConfig)

module.exports = db
