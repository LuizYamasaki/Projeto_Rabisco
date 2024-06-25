import Card_Prods from "./Card_Prods";

export default function Card_List({ produtos }) {
    return (
        <div className="container mt-4">
            <div className="row">
                {produtos.map((produto, index) => (
                    <div className="col-12 col-sm-6 col-md-4 col-lg-3 mb-4" key={index}>
                        <Card_Prods
                            img={produto[5]}
                            nome={produto[1]}
                            descricao={produto[2]}
                            preco={produto[3]}
                            quantidade={produto[4]}
                        />
                    </div>
                ))}
            </div>
        </div>
    );
}
