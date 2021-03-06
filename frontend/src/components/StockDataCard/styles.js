import styled from 'styled-components'

export const StyledStockDataCard = styled.div`
  display: flex;
  flex-direction: column;
  width: 300px;
  height: 150px;
  padding: 15px;
  border-radius: 10px;
  background-color: ${({ primary }) => primary ? 'blue' : 'grey'};
`