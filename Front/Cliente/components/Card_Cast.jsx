import Card_func from '@/components/Card_Func';

export default function Card_cast(props) {
  const { employees = [] } = props;  // Valor padrão para evitar undefined

  return (
    <div className="container mt-4">
      <div className="row">
        {employees.length > 0 ? employees.map((user, index) => (
          <div className="col-12 col-sm-6 col-md-4 col-lg-3 mb-4" key={index}>
            <Card_func 
              avatar={user.avatar} 
              first_name={user.first_name}
              last_name={user.last_name}
              email={user.email}
            />
          </div>
        )) : (
          <p>Nenhum funcionário encontrado.</p>
        )}
      </div>
    </div>
  );
}