export default function CartDrawer({cart,open,setOpen}){

return(

<div className={`fixed top-0 right-0 h-full w-96 glass shadow-2xl transform transition-transform ${open ? "translate-x-0":"translate-x-full"}`}>

<div className="p-6">

<h2 className="text-xl font-semibold mb-6">
Your Cart
</h2>

{cart.map(item =>(

<div key={item.id} className="flex justify-between mb-4">

<span>{item.name}</span>

<span>${item.price}</span>

</div>

))}

<button className="w-full bg-black text-white py-3 rounded-xl mt-6">
Checkout
</button>

</div>

</div>

)

}