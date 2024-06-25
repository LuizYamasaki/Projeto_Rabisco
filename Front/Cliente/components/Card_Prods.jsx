import Produtos from "@/pages/produtos"

export default function Card_Prods(props) {
  return (
    <div className="card p-3 text-center h-100">
      <img src={props.img} className="card-img-top h-100" alt={props.nome} />
      <div className="card-body d-flex flex-column justify-content-between">
        <h5 className="card-title">{props.nome}</h5>
        <p className="card-text min-vh-50">{props.descricao}</p>
        <div className="card-button p-3">
          <a href="#" className="btn btn-primary ">R$ {props.preco}</a>
        </div>
        
      </div>
      <div className="card-footer">
        <p className="card-text">{props.quantidade} Unidade(s) em estoque</p>
      </div>
    </div>
  )
}
Card_Prods.defaultProps = {
  nome: 'Produto',
  descricao: 'Descrição do produto',
  quantidade: 0,
  preco: 0.00
}