import React from 'react'
import { Link } from 'react-router-dom';
import { Sidenav, Nav } from 'rsuite';
import './Navbar.css';

function Navbar() {

  return (
      <div class="sidenav" style={{ width: 240 }}>
          <Sidenav defaultOpenKeys={['1']}>
              <Sidenav.Body>
                  <Nav activeKey="1">
                      <Nav.Menu eventKey="1" title="Presupuesto">
                          <Nav.Item eventKey='1-1'>Configuracion</Nav.Item>
                          <Nav.Item eventKey='1-2'>Formulación presupuestaria</Nav.Item>
                          <Nav.Item eventKey='1-3'>Modificación presupuestaria</Nav.Item>
                          <Nav.Item eventKey='1-4'>Programación física</Nav.Item>
                          <Nav.Item eventKey='1-5'>Reportes</Nav.Item>
                      </Nav.Menu>
                      <Nav.Menu eventKey="2" title="CAS"></Nav.Menu>
                      <Nav.Menu eventKey="3" title="Planificación"></Nav.Menu>
                      <Nav.Menu eventKey="4" title="Contrataciones"></Nav.Menu>
                      <Nav.Menu eventKey="5" title="Portal"></Nav.Menu>
                      <Nav.Menu eventKey="6" title="Contabilidad"></Nav.Menu>
                      <Nav.Menu eventKey="7" title="Tesorería"></Nav.Menu>
                      <Nav.Menu eventKey="8" title="Bienes Físicos"></Nav.Menu>
                      <Nav.Menu eventKey="9" title="Inversión Pública"></Nav.Menu>
                      <Nav.Menu eventKey="10" title="Crédito Público"></Nav.Menu>
                      <Nav.Menu eventKey="11" title="Ingresos Públicos"></Nav.Menu>
                      <Nav.Menu eventKey="12" title="Recursos Humanos"></Nav.Menu>
                  </Nav>
              </Sidenav.Body>
              <div class="footer">
                  <img src="../public/SoloLogo.png" width="25" height="25" align="left" />
                  (0221)429-4484/4509 <br /> pa@es.gov.ar
              </div>
          </Sidenav>
      </div>
  )
}

export default Navbar