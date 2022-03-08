import React from 'react'
import SearchInputAndButton from './components/SearchInputAndButton';
import StockDataSearchResult from './components/StockDataSearchResult'
import Wrapper from './components/Wrapper'
import BigText from './components/BigText'
import api from './services/api'

function App() {
  const [fundamentusData, setFundamentusData] = React.useState()
  const [acronym, setAcronym] = React.useState()
  const [yahooData, setYahooData] = React.useState()
  const [hasSearched, setHasSearched] = React.useState(false)

  const searchStockData = (acronym) => {
    setAcronym(acronym)
    setHasSearched(true)
    api
      .get(`/stock-data/yahoo/${acronym}`)
      .then(response => {
        console.log(response.data?.[0])
        setYahooData(response.data?.[0])
      })
      .catch(err => {
        setFundamentusData()
        console.log('Something went wrong\n', err)
      })
    api
      .get(`/stock-data/fundamentus/${acronym}`)
      .then(response => {
        setFundamentusData(response.data?.[0])
      })
      .catch(err => {
        setFundamentusData()
        console.log('Something went wrong\n', err)
      })
  }

  return (
    <div className="App">
      <Wrapper>
        <BigText style={{fontWeight: 400}}>{"Search stock data"}</BigText>
        <SearchInputAndButton searchStockData={searchStockData}/>
        {acronym && <BigText>{acronym}</BigText>}
        <StockDataSearchResult
          hasSearched={hasSearched}
          fundamentusData={fundamentusData}
          yahooData={yahooData}
        />
      </Wrapper>
    </div>
  );
}

export default App;
