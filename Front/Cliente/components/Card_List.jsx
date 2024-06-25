import Card_Prods from "./Card_Prods";

export default function Card_List(props) {
    const {produtos} = props
    return (
        <div className="container mt-4">
                <div className="row">
                    {/* ESTRUTURA DE REPETIÇÃO MAP */}
                    {produtos.map(function (produtos, index){
                        return(
                            <div className="col-12 col-sm-6 col-md-4 col-lg-3 mb-4" key={index}>
                                <Card_Prods 
                                    img ={produtos[5]} 
                                    nome={produtos[1]}
                                    descricao={produtos[2]}
                                    preco={produtos[3]}
                                    quantidade={produtos[4]}
                                />
                    </div>
                        )
                    })}
                </div>
            </div>
    )
}

