const express = require('express')
const cors = require('cors')
const router = require('./routes/routes')
const { sequelize : db } = require('./models')

const app = express()
app.use(express.json())
app.use(cors())
app.use('/', router)

db.authenticate().then(() => {
  console.log('Database connected...');
}).catch(err => {
  console.log('Error: ' + err);
})

db.sync().then(() => {
  console.log('Db synced')
}).catch(err => console.log("Error: " + err))

app.listen(5000, () => {
  console.log('Server up and running on port 5000')
})
