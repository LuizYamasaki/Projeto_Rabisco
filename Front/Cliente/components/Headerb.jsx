import Link from 'next/link';
import { useState } from 'react';
import styles from '../styles/Headerb.module.css';

export default function Headerb(props) {
  const [search, setSearch] = useState("");
    console.log(search)

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
            <li>
              {props.title}
            </li>
          </ul>
          <form className="d-flex" role="search">
            <input className="form-control me-2" type="search" placeholder="Search" aria-label="Search" value={search} onChange={(e) => setSearch(e.target.value)} />
            <button className="btn btn-light" type="submit">Search</button>
          </form>
        </div>
      </div>
    </nav>
  );
}
