import React from 'react'
import { StyledSearchInputAndButton } from './styles'
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';

const SearchInputAndButton = () => (
  <StyledSearchInputAndButton>
    <TextField size="small" />
    <Button variant="contained">Search</Button>
  </StyledSearchInputAndButton>
)

export default SearchInputAndButton
