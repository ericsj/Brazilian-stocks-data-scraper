import { StyledStockDataCard } from './styles'
import Text from '../Text'
import Title from '../Title'

const StockDataCard = ({ primary, title, data }) => (
  <StyledStockDataCard primary={primary}>
    <Title>{title}</Title>
    {data.map((content, index) => (
      <Text key={index}>{content}</Text>))
    }
  </StyledStockDataCard>
)

export default StockDataCard
