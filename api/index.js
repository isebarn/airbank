import express from 'express'
import { PrismaClient } from '@prisma/client'

const prisma = new PrismaClient()
const app = express()

app.use(express.json())

app.post('/data', async (req, res) => {
  const transactions = await prisma.transactions.findMany({
    where: {
      transactionDate: {
        gte: new Date(req.body[0]),
        lt:  new Date(req.body[1])
      },
    },
  })
  res.json(transactions)
})

/**
* logic for our api will go here
*/
export default {
  path: '/api',
  handler: app
}