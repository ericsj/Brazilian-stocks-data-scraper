import React from 'react'
import { StyledNotFoundCard } from './styles'
import Text from '../Text'

const NotFoundCard = ({ source }) => {
    return(
      <StyledNotFoundCard>
        <Text>{`No data found from ${source}`}</Text>
      </StyledNotFoundCard>
    )
  }

export default NotFoundCard
