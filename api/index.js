const express = require('express')
const app = express()
app.use(express.json());

app.put('/Yahoo', (req, res) => {
  console.log(req.body)
  res.status(200).send()
})

app.listen(5000, (err) => {
  if (!err) console.log('Server up and running on port 5000')
})