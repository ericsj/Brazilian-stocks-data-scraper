import StockDataCard from '../StockDataCard'
import NotFoundCard from '../NotFoundCard'
import { StyledStockDataSearchResult } from './styles'
import React from 'react'

const StockDataSearchResult = ({ yahooData, hasSearched, fundamentusData }) => {
  React.useEffect(() =>{
    console.log({yahooData, fundamentusData, hasSearched})
  })
  return(
    hasSearched && (
      <StyledStockDataSearchResult>
        {yahooData
            ? <StockDataCard primary title='Yahoo' data={yahooData} />
            : <NotFoundCard source='Yahoo' />}
        {fundamentusData
            ? <StockDataCard title='Fundamentus' data={fundamentusData} />
            : <NotFoundCard source='Fundamentus' />}
      </StyledStockDataSearchResult>
    )
  )
}

export default StockDataSearchResult
