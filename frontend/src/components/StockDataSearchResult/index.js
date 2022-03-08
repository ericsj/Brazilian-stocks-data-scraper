import StockDataCard from '../StockDataCard'
import { StyledStockDataSearchResult } from './styles'

const dataPrimary = [
  'name: petrobras',
  'ac: petr'
]
const dataSecondary = [
  'name: gol',
  'ac: goll'
]

const StockDataSearchResult = (props) => (
  <StyledStockDataSearchResult>
    <StockDataCard primary title='Yahoo' data={dataPrimary} />
    <StockDataCard data={dataSecondary}/>
  </StyledStockDataSearchResult>
)

export default StockDataSearchResult
