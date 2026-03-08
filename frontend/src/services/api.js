import axios from "axios"

const API=axios.create({
baseURL:"http://localhost:8000"
})

export const getProducts=()=>API.get("/products")

export const createOrder=(data)=>API.post("/orders",data)

export const getOrders=()=>API.get("/orders")