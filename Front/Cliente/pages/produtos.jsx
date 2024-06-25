import React, { useState, useEffect } from 'react';
import Headerb from '../components/Headerb';
import Titulo from '../components/Titulo';
import Card_List from '../components/Card_List';

export default function Produtos() {
    const [data, setData] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [searchResults, setSearchResults] = useState([]);

    useEffect(() => {
        async function fetchData() {
            try {
                const response = await fetch('http://127.0.0.1:5000/produto');
                if (!response.ok) {
                    throw new Error('Erro ao buscar os dados');
                }
                const result = await response.json();
                setData(result);
            } catch (error) {
                setError(error.message);
            } finally {
                setLoading(false);
            }
        }
        fetchData();

        const interval = setInterval(fetchData, 1000);

        return () => clearInterval(interval);
    }, []);

    const handleSearchResults = (results) => {
        setSearchResults(results);
    };

    if (loading) return <div>Loading...</div>;
    if (error) return <div>Error: {error}</div>;

    return (
        <>
            <Headerb onSearchResults={handleSearchResults} />
            <Titulo texto="Conheça nossos produtos!" />
            <Card_List produtos={searchResults.length > 0 ? searchResults : data} />
        </>
    );
}
