import React from 'react'
import { StyledStockDataCard } from './styles'
import Text from '../Text'
import Title from '../Title'

const StockDataCard = ({ primary, title, data }) => {
    const [formattedData, setFormattedData] = React.useState([])
    React.useEffect(() => {
      const { name, price, sector, priceProfitRatio, netWorth } = data
      setFormattedData({
        Name: name,
        Price: price,
        Sector: sector,
        'Price / profit': priceProfitRatio,
        'Net worth': netWorth
      })
    }, [data])

    return(
      <StyledStockDataCard primary={primary}>
        <Title>{title}</Title>
        {Object.entries(formattedData).map(([key, value], index) => (
          <Text key={index}>{`${key}: ${value}`}</Text>))
        }
      </StyledStockDataCard>
    )
  }

export default StockDataCard
