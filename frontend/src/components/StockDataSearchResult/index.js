import StockDataCard from '../StockDataCard'
import { StyledStockDataSearchResult } from './styles'

const StockDataSearchResult = ({ fundamentusData, yahooData }) => (
  <StyledStockDataSearchResult>
    {yahooData.length && <StockDataCard primary title='Yahoo' data={yahooData} />}
    {fundamentusData.length && <StockDataCard title='Fundamentus' data={fundamentusData} />}
  </StyledStockDataSearchResult>
)

export default StockDataSearchResult
