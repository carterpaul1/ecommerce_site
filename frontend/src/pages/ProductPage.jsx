export default function ProductPage(){

return(

<div className="pt-32 max-w-5xl mx-auto px-6">

<div className="grid md:grid-cols-2 gap-12">

<img
src="https://images.unsplash.com/photo-1518444028785-8fbcd101ebb9"
className="rounded-3xl shadow-xl"
/>

<div>

<h1 className="text-3xl font-semibold mb-4">
Air Headphones
</h1>

<p className="text-gray-600 mb-6">
High fidelity spatial audio headphones with noise cancelation.
</p>

<p className="text-2xl font-bold mb-6">
$299
</p>

<button className="bg-black text-white px-8 py-3 rounded-full">
Add to Cart
</button>

</div>

</div>

</div>

)

}