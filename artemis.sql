/*
Escreva uma consulta SQL que mostre a lista de todos os clientes e seus respectivos pedidos,
mesmo que o cliente não tenha feito nenhum pedido. A tabela resultante deve conter as colunas:
Nome, PedidoID, DataPedido e ValorTotal.
*/

SELECT 
    c.Nome,
    p.PedidoID,
    p.DataPedido,
    p.ValorTotal
FROM 
    Clientes c
LEFT JOIN 
    Pedidos p ON c.ClienteID = p.ClienteID;

/*
Escreva uma consulta SQL que exiba o total de pedidos realizados e o valor total de pedidos por
cliente, apenas para os clientes que possuem pedidos registrados. A tabela resultante deve conter as
colunas: Nome, QuantidadePedidos e ValorTotalPedidos.
*/

SELECT 
    c.Nome,
    COUNT(p.PedidoID) AS QuantidadePedidos,
    SUM(p.ValorTotal) AS ValorTotalPedidos
FROM 
    Clientes c
INNER JOIN 
    Pedidos p ON c.ClienteID = p.ClienteID
GROUP BY 
    c.Nome;

/*
Escreva uma consulta SQL que exiba os pedidos que não possuem pagamentos registrados.
A tabela resultante deve conter as colunas: PedidoID, DataPedido e ValorTotal.
*/

SELECT 
    p.PedidoID,
    p.DataPedido,
    p.ValorTotal
FROM 
    Pedidos p
LEFT JOIN 
    Pagamentos pg ON p.PedidoID = pg.PedidoID
WHERE 
    pg.PagamentoID IS NULL;
