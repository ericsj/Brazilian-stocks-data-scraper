import React from 'react'
import SearchInputAndButton from './components/SearchInputAndButton';
import StockDataSearchResult from './components/StockDataSearchResult'
import Wrapper from './components/Wrapper'

function App() {
  return (
    <div className="App">
      <Wrapper>
        <SearchInputAndButton />
        <StockDataSearchResult />
      </Wrapper>
    </div>
  );
}

export default App;
