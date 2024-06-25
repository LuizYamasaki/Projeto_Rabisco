import axios from "axios";

const api = axios.create({baseURL: 'https://reqres.in/api' });

export async function getContato() {
    try {
        const response = await api.get('/users?page=1');
        const response_page = await api.get('/users?page=2');
        const page1 = response.data.data;
        const page2 = response_page.data.data;

        const pages = [...page1,...page2];
        return pages;

    } catch (error) {
        console.error(`Erro ao buscar os funcionarios: ${error.message}`);
    }
}
