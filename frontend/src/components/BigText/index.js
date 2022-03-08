import React from 'react'
import { StyledAcronym } from './styles'

const BigText = ({ children, ...props }) => (
  <StyledAcronym {...props}>{children}</StyledAcronym>
)

export default BigText
