import React from 'react'
import SearchInputAndButton from './components/SearchInputAndButton';
import StockDataSearchResult from './components/StockDataSearchResult'
import Wrapper from './components/Wrapper'
import api from './services/api'

function App() {
  const [fundamentusData, setFundamentusData] = React.useState([])
  const [yahooData, setYahooData] = React.useState([])

  const searchStockData = (acronym) => {
    api
      .get(`/stock-data/yahoo/${acronym}`)
      .then(response => {
        setYahooData(response.data)
      })
      .catch(err => {
        console.log('Something went wrong\n', err)
      })
    api
      .get(`/stock-data/fundamentus/${acronym}`)
      .then(response => {
        setFundamentusData(response.data)
      })
      .catch(err => {
        console.log('Something went wrong\n', err)
      })
  }

  return (
    <div className="App">
      <Wrapper>
        <SearchInputAndButton searchStockData={searchStockData}/>
        <StockDataSearchResult
          fundamentusData={fundamentusData}
          yahooData={yahooData}
        />
      </Wrapper>
    </div>
  );
}

export default App;
