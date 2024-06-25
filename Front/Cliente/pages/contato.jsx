import Headerb from '../components/Headerb'
import Titulo from '../components/Titulo'
import Card_cast from '@/components/Card_Cast'

import { useState, useEffect } from 'react'
import { getContato } from '@/services/apiFunc'
import Card_func from '@/components/Card_Func'

export default function employees() {

  const [employees, setEmployees] = useState([])

  async function buscaFunci(){
    try {
      const data = await getContato()
      setEmployees(data)
      console.log(employees)

    } catch (error) {
      console.error(`Erro ao buscar os Funcionarios`, error)
    }
  }

  useEffect(()=>{
    buscaFunci()
  },)

  return (
    <>
      <Headerb/>
      <Titulo texto="Conheça nossos Funcionarios!"/>
      <Card_cast employees={employees}/>
      
    </>
  )
}
