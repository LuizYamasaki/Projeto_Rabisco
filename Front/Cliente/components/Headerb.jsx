import React, { useState } from 'react';
import Link from 'next/link';
import styles from '../styles/Headerb.module.css';

export default function Headerb({ onSearchResults }) {
    const [search, setSearch] = useState("");

    const handleSearch = async (e) => {
        e.preventDefault();
        try {
            const response = await fetch(`http://127.0.0.1:5000/produto/busca?q=${search}`);
            if (!response.ok) {
                throw new Error('Erro ao buscar os produtos');
            }
            const result = await response.json();
            onSearchResults(result);
        } catch (error) {
            console.error('Erro:', error);
        }
    };

    return (
        <nav className="navbar navbar-expand-lg bg-dark" data-bs-theme="dark">
            <div className="container-fluid">
                <img src="logo/rabisco.png" className={styles.img} />
                <Link className="navbar-brand ms-1 fs-2" href="#">Rabisco</Link>
                <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span className="navbar-toggler-icon"></span>
                </button>
                <div className="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul className="navbar-nav me-auto mb-2 mb-lg-0">
                        <li className="nav-item">
                            <Link className="nav-link active fs-4" aria-current="page" href="/">Home</Link>
                        </li>
                        <li className="nav-item">
                            <Link className="nav-link active fs-4" aria-current="page" href="/produtos">Produtos</Link>
                        </li>
                        <li className="nav-item">
                            <Link className="nav-link active fs-4" aria-current="page" href="/contato">Contato</Link>
                        </li>
                    </ul>
                    <form className="d-flex" role="search" onSubmit={handleSearch}>
                        <input className="form-control me-2" type="search" placeholder="Search" aria-label="Search" value={search} onChange={(e) => setSearch(e.target.value)} />
                        <button className="btn btn-light" type="submit">Search</button>
                    </form>
                </div>
            </div>
        </nav>
    );
}
