import {BrowserRouter,Routes,Route} from "react-router-dom"

import Navbar from "./components/Navbar"
import Home from "./pages/Home"
import ProductPage from "./pages/ProductPage"
import Checkout from "./pages/Checkout"
import Orders from "./pages/Orders"

export default function App(){

return(

<BrowserRouter>

<Navbar/>

<Routes>

<Route path="/" element={<Home/>}/>
<Route path="/product/:id" element={<ProductPage/>}/>
<Route path="/checkout" element={<Checkout/>}/>
<Route path="/orders" element={<Orders/>}/>

</Routes>

</BrowserRouter>

)

}