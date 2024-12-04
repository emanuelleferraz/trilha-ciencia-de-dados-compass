-- EXERCÍCIOS ########################################################################

-- (Exercício 1) Identifique quais as marcas de veículo mais visitada na tabela sales.funnel
select prod.brand, count(fun.visit_page_date) as visit_brand
from sales.funnel as fun
left join sales.products as prod
	on fun.product_id = prod.product_id
group by prod.brand
order by visit_brand desc

-- (Exercício 2) Identifique quais as lojas de veículo mais visitadas na tabela sales.funnel

select str.store_name, count(fun.visit_page_date) as visit_store
from sales.funnel as fun
left join sales.stores as str
	on fun.store_id = str.store_id
group by str.store_name
order by visit_store desc

-- (Exercício 3) Identifique quantos clientes moram em cada tamanho de cidade (o porte da cidade
-- consta na coluna "size" da tabela temp_tables.regions)

select
	reg.size,
	count(*) as client_count_city
from sales.customers as cus
left join temp_tables.regions as reg
	on lower(cus.city) = lower(reg.city)
	and lower(cus.state) = lower(reg.state)
group by reg.size
order by client_count_city desc
