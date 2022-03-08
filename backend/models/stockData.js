const stockData = (sequelize, DataTypes) => {
  const StockData = sequelize.define('StockData', {
    id: {
      type: DataTypes.INTEGER,
      autoIncrement: true,
      allowNull: false,
      primaryKey: true
    },
    source: {
      type: DataTypes.STRING
    },
    acronym: {
      type: DataTypes.STRING
    },
    name: {
      type: DataTypes.STRING
    },
    sector: {
      type: DataTypes.STRING
    },
    priceProfitRatio: {
      type: DataTypes.DOUBLE
    },
    netWorth: {
      type: DataTypes.BIGINT
    }
  })
  return StockData
}

module.exports = stockData
