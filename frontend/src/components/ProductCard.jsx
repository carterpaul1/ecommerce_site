export default function ProductCard({product}){

return(

<div className="glass rounded-3xl p-5 hover:shadow-2xl hover:-translate-y-1 transition duration-300">

<img
src={product.image}
className="rounded-xl mb-4 h-52 w-full object-cover"
/>

<h2 className="text-lg font-semibold">
{product.name}
</h2>

<p className="text-gray-600 text-sm mt-1">
{product.description}
</p>

<div className="flex justify-between items-center mt-4">

<span className="text-lg font-bold">
${product.price}
</span>

<button className="bg-black text-white px-4 py-2 rounded-full text-sm hover:opacity-80">
Add to Cart
</button>

</div>

</div>

)

}