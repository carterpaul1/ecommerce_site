export default function Checkout(){

return(

<div className="pt-32 max-w-3xl mx-auto px-6">

<div className="glass p-10 rounded-3xl shadow-xl">

<h2 className="text-2xl font-semibold mb-6">
Checkout
</h2>

<form className="space-y-4">

<input
placeholder="Full Name"
className="w-full p-3 rounded-xl border"
/>

<input
placeholder="Email"
className="w-full p-3 rounded-xl border"
/>

<input
placeholder="Address"
className="w-full p-3 rounded-xl border"
/>

<input
placeholder="Card Number"
className="w-full p-3 rounded-xl border"
/>

<button className="w-full bg-black text-white py-3 rounded-xl mt-4">
Place Order
</button>

</form>

</div>

</div>

)

}