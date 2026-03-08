import ProductCard from "../components/ProductCard"
import RecommendationCarousel from "../components/RecommendationCarousel"

export default function Home(){

const products=[
{
id:1,
name:"Air Headphones",
price:299,
image:"https://images.unsplash.com/photo-1518444028785-8fbcd101ebb9",
description:"Spatial audio headphones"
},
{
id:2,
name:"Smart Watch",
price:399,
image:"https://images.unsplash.com/photo-1516574187841-cb9cc2ca948b",
description:"Advanced fitness tracking"
}
]

return(

<div className="pt-32 max-w-6xl mx-auto px-6">

<section className="text-center mb-20">

<h1 className="text-5xl font-semibold tracking-tight mb-6">
The Future of Shopping
</h1>

<p className="text-gray-600 max-w-xl mx-auto">
Discover curated products powered by intelligent recommendations.
</p>

</section>

<section className="grid grid-cols-1 md:grid-cols-3 gap-8">

{products.map(product =>(
<ProductCard key={product.id} product={product}/>
))}

</section>

<RecommendationCarousel products={products}/>

</div>

)

}