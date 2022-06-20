import { useState } from "react";
import { BiCog } from "react-icons/bi";
import Container from "react-bootstrap/Container";
import Navbar from "react-bootstrap/Navbar";
import Offcanvas from "react-bootstrap/Offcanvas";


const CustomNavbar = () => {
    const [overlay, setOverlay] = useState(false);

    const handleClose = () => setOverlay(false);
    const handleShow = () => setOverlay(true);

    return (
        <Navbar bg="light" expand="lg">
            <Container fluid>
                <Navbar.Brand href="#">RC Tools</Navbar.Brand>
                <Navbar.Text id="navbarScroll" className="justify-end">
                    <a href="#" onClick={handleShow} className="cursor-pointer">
                        <BiCog className="hover:cursor-pointer" />
                    </a>
                    <Offcanvas show={overlay} onHide={handleClose} placement="end">
                        <Offcanvas.Header closeButton>
                            <Offcanvas.Title>Offcanvas</Offcanvas.Title>
                        </Offcanvas.Header>
                        <Offcanvas.Body>
                            Some text as placeholder. In real life you can have the elements you
                            have chosen. Like, text, images, lists, etc.
                        </Offcanvas.Body>
                    </Offcanvas>
                </Navbar.Text>
            </Container>
        </Navbar>
    );
};

export default CustomNavbar;
