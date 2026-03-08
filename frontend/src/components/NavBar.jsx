import { Link } from "react-router-dom"

export default function Navbar(){

return(

<nav className="glass fixed top-5 left-1/2 -translate-x-1/2 w-[90%] max-w-6xl rounded-2xl shadow-lg px-6 py-4 flex justify-between items-center">

<h1 className="text-xl font-semibold tracking-tight">
NeoStore
</h1>

<div className="flex gap-6 text-sm">

<Link to="/" className="hover:text-blue-500 transition">
Home
</Link>

<Link to="/orders" className="hover:text-blue-500 transition">
Orders
</Link>

<Link to="/checkout" className="hover:text-blue-500 transition">
Cart
</Link>

</div>

</nav>

)

}