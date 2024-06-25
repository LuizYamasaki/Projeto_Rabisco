import employees from "@/pages/contato"

export default function Card_func(props) {
  return (
    <div className="card p-3 text-center h-100">
      <img src={props.avatar} className="card-img-top h-100" alt={props.first_name} />
      <div className="card-body d-flex flex-column justify-content-between">
        <h5 className="card-title">{props.first_name}</h5>
        <p className="card-text min-vh-50">{props.last_name}</p>
        <div className="card-button p-3">
          <a href="#" className="btn btn-primary ">{props.email}</a>
        </div>
        
      </div>
      
    </div>
  )
}
Card_func.defaultProps = {
  first_name: 'Con',
  last_name: 'tato',
  email: 'contato@gmail.com',
}