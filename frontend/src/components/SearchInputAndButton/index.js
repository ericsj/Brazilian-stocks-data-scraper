import React from 'react'
import { StyledSearchInputAndButton } from './styles'
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';

const SearchInputAndButton = ({ searchStockData }) => {
  const [stockAcronym, setStockAcronym] = React.useState('')
  
  const handleSearch = () => {
    if(stockAcronym) searchStockData(stockAcronym)
  }
  
  const handleChange = (event) => {
    setStockAcronym(event.target.value)
  }

  return (
    <StyledSearchInputAndButton>
      <TextField size="small" value={stockAcronym} onChange={handleChange}/>
      <Button type='submit' variant="contained" onClick={handleSearch}>Search</Button>
    </StyledSearchInputAndButton>
  )
}

export default SearchInputAndButton
