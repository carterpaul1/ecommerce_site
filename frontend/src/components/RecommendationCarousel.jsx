import ProductCard from "./ProductCard"

export default function RecommendationCarousel({products}){

return(

<div className="mt-16">

<h2 className="text-2xl font-semibold mb-6">
Recommended For You
</h2>

<div className="grid grid-cols-1 md:grid-cols-3 gap-6">

{products.map(product =>(

<ProductCard key={product._id} product={product}/>

))}

</div>

</div>

)

}