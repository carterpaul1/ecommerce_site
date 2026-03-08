export default function Orders(){

const orders=[
{
id:1,
date:"2026-03-02",
total:299
}
]

return(

<div className="pt-32 max-w-4xl mx-auto px-6">

<h1 className="text-3xl font-semibold mb-10">
Order History
</h1>

{orders.map(order=>(

<div key={order.id} className="glass p-6 rounded-2xl mb-4 flex justify-between">

<div>

<p className="font-medium">
Order #{order.id}
</p>

<p className="text-sm text-gray-600">
{order.date}
</p>

</div>

<span className="font-bold">
${order.total}
</span>

</div>

))}

</div>

)

}